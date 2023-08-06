import pandas as pd
import numpy as np
import northgravity as ng
import datetime

from pandas.tseries.offsets import BDay, DateOffset
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, mean_absolute_error

import logging
log = logging.getLogger()



class DataHandler:
    def __init__(self):
        self.th = ng.TaskHandler()
        self.dh = ng.DatalakeHandler()

    # -------------------------------------
    # Datasets related methods
    # -------------------------------------

    def train_test_split(self, features_df_raw, target_df_raw, val=True):
        '''Split the input data (Features and Target) sets based on 'Split_Labes' column.
        
        Params: 
            - val:  True - split the given datasets into train, validation, test sets
                    False - split the given datasets into train and test sets

        Returns:
            - Dictionary containing: X_train, y_train, X_val, y_val, X_test, y_test (Dataframes) in val=True mode 
                                    or X_train, y_train, X_test, y_test (Dataframes) in val=False mode 
        '''

        log.info(f'Features shape: {features_df_raw.shape} \n Target shape: {target_df_raw.shape}')
        
        # Check if features and target have the same number of rows and identically defined split into train/val/test
        if features_df_raw.shape[0] != target_df_raw.shape[0]:
            raise Exception(f'Target and features shape mismatch. \
                            {features_df_raw.shape[0]} != {target_df_raw.shape[0]}')

        if all(features_df_raw.index != target_df_raw.index):
            raise Exception(f'Target and features datetime range mismatch.\
                            {features_df_raw.index} != {target_df_raw.index}')

        assert 'Split_Label' in features_df_raw.columns, \
                'Split_Label column not found in Features Dataset. Use Train/Test Split task'

        assert 'Split_Label' in target_df_raw.columns, \
                'Split_Label column not found in Target Dataset. Use Train/Test Split task'

        assert all(features_df_raw['Split_Label'].unique()) == all(target_df_raw['Split_Label'].unique()), \
                'Different splits found in Split_Label column! Features Dataset contains {}, while Target Dataset contains {}' \
                .format(features_df_raw['Split_Label'].unique(), target_df_raw['Split_Label'].unique())
                
        assert all(features_df_raw['Split_Label'].unique() == ["Train", "Val", "Test"]), \
                'Split Label does not contain Train/Val/Test split, which is needed for this task!'


        if val:
        # Prepare features train/val/test datasets
            X_train = features_df_raw.loc[features_df_raw['Split_Label']=='Train'].drop(columns='Split_Label')
            X_val = features_df_raw.loc[features_df_raw['Split_Label']=='Val'].drop(columns='Split_Label')
            X_test = features_df_raw.loc[features_df_raw['Split_Label']=='Test'].drop(columns='Split_Label')

            # Prepare target train/val/test datasets
            y_train = target_df_raw.loc[target_df_raw['Split_Label']=='Train'].drop(columns='Split_Label')
            y_val = target_df_raw.loc[target_df_raw['Split_Label']=='Val'].drop(columns='Split_Label')
            y_test = target_df_raw.loc[target_df_raw['Split_Label']=='Test'].drop(columns='Split_Label')

            # Remove nans that may exist in target validation set as a result of shifting in the process of label creation
            whole_val = pd.concat([X_val, y_val], axis=1).dropna(subset=[y_val.columns[-1]])
            X_val = whole_val[X_val.columns]
            y_val = whole_val[y_val.columns] 

            log.info(f'Training dataset shape: features - {X_train.shape}, target - {y_train.shape}')
            log.info(f'Training dataset shape: features - {X_val.shape}, target - {y_val.shape}')
            log.info(f'Training dataset shape: features - {X_test.shape}, target - {y_test.shape}')

            # Create dict containing all features and targets datasets
            data_dict = {'Train': [X_train, y_train],
                        'Val': [X_val, y_val],
                        'Test': [X_test, y_test]}

        else:
            X_train = features_df_raw.loc[features_df_raw['Split_Label']!='Test'].drop(columns='Split_Label')
            X_test = features_df_raw.loc[features_df_raw['Split_Label']=='Test'].drop(columns='Split_Label')

            # Prepare target train/test datasets
            y_train = target_df_raw.loc[target_df_raw['Split_Label']!='Test'].drop(columns='Split_Label')
            y_test = target_df_raw.loc[target_df_raw['Split_Label']=='Test'].drop(columns='Split_Label')

            # Remove nans that may exist in target train set as a result of shifting in the process of label creation
            whole_train = pd.concat([X_train, y_train], axis=1).dropna(subset=[y_train.columns[-1]])
            X_train = whole_train[X_train.columns]
            y_train = whole_train[y_train.columns] 

            log.info(f'Training dataset shape: features - {X_train.shape}, target - {y_train.shape}')
            log.info(f'Training dataset shape: features - {X_test.shape}, target - {y_test.shape}')

            # Create dict containing all features and targets datasets
            data_dict = {'Train': [X_train, y_train],
                        'Test': [X_test, y_test]}

        return data_dict



    # -------------------------------------
    # Dates handling methods
    # -------------------------------------

    def get_date_col(self, dataset):
        ''' The function detects DateTime columns (even if it's set to index) and returned them as pd.Series 
            (if one column was detected) or pd.Dateframe (if >1 DateTime columns were detected), 
            parses them to datetime64[ns] format.
        
        Returns:
            - pd.DateFrame or pd.Series containing only columns with the date values extracted from a passed dataset
        '''

        dataset = dataset.reset_index(level=0)

        date_col_list = []
        for col in dataset.columns:
            if dataset[col].dtype == object:
                try:
                    dataset[col] = pd.to_datetime(dataset[col])
                    date_col_list.append(col)
                except ValueError:
                    pass
            elif np.issubdtype(dataset[col].dtypes, np.datetime64):
                date_col_list.append(col)

        if date_col_list == []:
            log.warn('There is no DateTime data in passed dataset!')

        log.info('{} date col detected in a given dataset: {}'.format(len(date_col_list), date_col_list))

        return dataset[date_col_list]



    def prep_prediction_date(self, target_idx, period):
        ''' Gets the frequency of the target time index and shifts it by period value for test and forecast datasets preparation.
        Func based on the pandas infer_freq which returns a string of offset aliases defining
        the data frequention (https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases)
        NOTE: if the targets date frequencies are hours or minutes dates are shifted by days anyway 
                - forecasts are not prepared for hours/minutes

        Returns:
            - pandas TimeIndex shifted by given period according to the targets frequency          
        '''

        assert type(target_idx) is pd.DatetimeIndex, 'The index of target dataframe in not the pd.DatetimeIndex type!'

        # gets the pandas offset alias if there is no missing dates in target index
        data_freq = pd.infer_freq(target_idx[:10])
        if data_freq not in ['', None]:
            data_freq = data_freq.split('-')[0]

            if data_freq == 'B':
                indexes = target_idx + BDay(period)
            elif data_freq == 'D':
                indexes = target_idx + DateOffset(days=period)
            elif data_freq == 'W':
                indexes = target_idx + DateOffset(weeks=period)
            elif data_freq in ['M', 'SM', 'BM', 'CBM', 'MS', 'SMS', 'BMS']:
                indexes = target_idx + DateOffset(months=period)
            elif data_freq in ['Y', 'A', 'BA', 'BY', 'AS', 'YS', 'BAS', 'BYS']:
                indexes = target_idx + DateOffset(years=period)
            else:
                indexes = target_idx + DateOffset(days=period)
                log.info('The frequency of the time date did not recognize! Days frequency assigned')
            
            log.info('Datetime frequency: {}'.format(data_freq))

        else:
            # if lack of dates in target index calculates the the difference between dates in days
            # and assign proper pandas offset alias 
            data_freq_days = target_idx.to_series().diff().mode()[0].days
            if data_freq_days == 1:
                indexes = target_idx + DateOffset(days=period)
            elif data_freq_days == 7 :
                indexes = target_idx + DateOffset(weeks=period)
            elif data_freq_days in [30, 31]:
                indexes = target_idx + DateOffset(months=period)
            elif data_freq_days in [365, 366]:
                indexes = target_idx + DateOffset(years=period)
            else:
                indexes = target_idx + DateOffset(days=period)
                log.info('The frequency of the time date did not recognize! Days frequency assigned')
            
            log.info('Datetime frequency: {}'.format(data_freq_days))
        
        return indexes



    def forecast_date_format(self, prep_target_idx):
        ''' The function prepares the forecast date in DataPrep required format based on passed pd.DataFrame/pd.Series/pd.DatetimeIndex.
            Passed input prep_target_idx should be the same as passed to the test dataset (already preprocessed by prep_prediction_date function).

        Returns:
            - Timestamp with prediction date in formats: - '%Y-%m-%d' for daily, weekly, monthly ect. data
                                                         - '%Y-%m-%dT%H:%M:%S' for hourly data
        '''

        try:
            prep_target_idx = pd.to_datetime(prep_target_idx)
        except:
            raise TypeError('Passed index column is not the datetime type and cannot be converted into datetime format!')

        # check the data frequency is hourly/minutes or daily/weekly/etc. and change the date format accordingly
        if str(prep_target_idx[0]).split(' ')[1] != '00:00:00':
            forecast_date = datetime.datetime.strptime(str(prep_target_idx[-1]),
                                                            "%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%dT%H:%M:%S')
        else:
            forecast_date = datetime.datetime.strptime(str(prep_target_idx[-1]),
                                                            "%Y-%m-%d %H:%M:%S").strftime('%Y-%m-%d')
        log.info(f'Forecast Date: {forecast_date}')

        return forecast_date

    

    def holiday_shift(self, datetime_col, holiday_list):
        ''' The function changes the dates in passed pd.DataFrame/pd.Series/pd.DatetimeIndex to the following business days 
            if there are holidays according the holiday_list.
        
        Returns:
            - pd.DataFrame/pd.Series with shifted dates values.
        '''

        date_df  = pd.DataFrame(datetime_col.copy())

        assert type(holiday_list[0]) in [pd.DatetimeIndex, pd.Timestamp], 'Passed holiday list is not in a pd.Timestamp format!'

        assert np.issubdtype(date_df.dtypes, np.datetime64) or \
                    np.issubdtype(date_df.dtypes, pd.DatetimeIndex), 'Passed dataframe column is not the datetime type!'


        # remove holidays dates from date column
        rem_hol = date_df[~date_df.isin(holiday_list)].dropna()
        num_dates = date_df.isin(holiday_list).sum()[0]
        log.info('{} holidays found in given date column'.format(num_dates))

        # add business days to the end of the column in the same number as number of deleted holidays
        dates2add = pd.DataFrame(pd.date_range(date_df.iloc[-1][0], periods=num_dates+1, freq="B")[1:])
        dates2add.columns = rem_hol.columns

        while dates2add.isin(holiday_list).sum()[0] > 0:
            if num_dates == 1:
                dates2add = pd.DataFrame(dates2add + BDay(1))
                dates2add.columns = rem_hol.columns
            else:    
                num_dates = dates2add.isin(holiday_list).sum()[0]
                new_dates2add = dates2add[~dates2add.isin(holiday_list)].dropna()
                new_dates2add.columns = rem_hol.columns
                # add new dates with deleted holidays
                rem_hol = pd.concat([rem_hol, new_dates2add]).reset_index(drop=True)
                # add next bdays in number of secondly deleted holidays
                dates2add = pd.DataFrame(pd.date_range(new_dates2add.iloc[-1][0], periods=num_dates+1, freq="B")[1:])
                dates2add.columns = rem_hol.columns
        
        # return column with business days added
        rem_hol = pd.concat([rem_hol, dates2add]).reset_index(drop=True)
        log.info('Shifted date column: {}'.format(rem_hol))

        return rem_hol



    def date_shift(self, datetime_col, period, freq='B'):
        '''The function changes the dates in passed pd.DataFrame or pd.Series to the following date in a given frequency. 
        
        Returns:
            - pd.DataFrame/pd.Series with shifted dates values.
        '''

        date_df  = pd.DataFrame(datetime_col.copy())
        assert np.issubdtype(date_df.dtypes, np.datetime64) or \
                    np.issubdtype(date_df.dtypes, pd.DatetimeIndex), 'Passed dataframe column is not the datetime type!'


        if freq == 'B':
            shifted_df = date_df + BDay(period)
            frq_type = 'Business Day'
        elif freq == 'D':
            shifted_df = date_df + DateOffset(days=period)
            frq_type = 'Week Day'
        elif freq == 'BW':
            shifted_df = date_df + BDay(period*5)
            frq_type = 'Business Week'            
        elif freq == 'W':
            shifted_df = date_df + DateOffset(weeks=period)
            frq_type = 'Week'
        elif freq == 'M':
            shifted_df = date_df + DateOffset(months=period)
            frq_type = 'Month'
        elif freq == 'Q':
            shifted_df = date_df + DateOffset(months=3*period)
            frq_type = 'Quarter'
        elif freq in ['Y', 'A']:
            shifted_df = date_df + DateOffset(years=period)
            frq_type = 'Year'
        else:
            shifted_df = date_df + DateOffset(days=period)
            frq_type = 'Business Day'
            log.info('The frequency of the time date did not recognize! Days frequency assigned')
        

        if period == 1:
            log.info('Given dates shifted by {} {}'.format(period, frq_type))
        else:
            log.info('Given dates shifted by {} {}s'.format(period, frq_type))

        return shifted_df



    # -------------------------------------
    # Model's results related methods
    # -------------------------------------

    def get_scores_classification(self, actual, predicted):
        '''The function calculates the classification metrics based on the comparison of predicted and actual values.
           To calculate Accuracy, Precision, Recall and F1 the sklearn.metrics are used.

        Returns:
            - Dictionary containing four base metrics: Accuracy, Precision, Recall and F1 
        '''

        # Compute ACC, PREC, RECALL and F1 score over the predicted values
        acc = round(accuracy_score(actual, predicted), 2)
        prec = round(precision_score(actual, predicted, average="macro"),2)
        recall = round(recall_score(actual, predicted, average = "macro"), 2)
        f1 = round(f1_score(actual, predicted, average="macro"), 2)

        scores_dict = {'Accuracy': acc, 'Precision':prec, 'Recall': recall, 'F1': f1}
        log.info('Calculated scores -> Accuracy: {}, Precision: {}, Recall: {}, F1: {}'.format(acc, prec, recall, f1))
        
        return scores_dict


    def get_scores_regression(self, actual, predicted):
        '''The function calculates the regression metrics based on the comparison of predicted and actual values.
           To calculate Mean Squared Error, Root Mean Squared Error, Mean Absolute Percentage Error 
           and Mean Absolute Error the sklearn.metrics are used.
        
        Returns:
            - Dictionary containing four base metrics: MSE, RMSE, MAPE and MAE.
        '''

        # Compute MSE, RMSE, MAPE score over the predicted values
        mse = round(mean_squared_error(actual, predicted), 2)
        rmse = round(mse ** 0.5, 2)
        mape = round(mean_absolute_percentage_error(actual, predicted), 2)
        mae = round(mean_absolute_error(actual, predicted), 2)
        
        scores_dict = {'MSE': mse, 'RMSE': rmse, 'MAPE': mape, 'MAE': mae}
        log.info('Calculated scores -> MSE: {}, RMSE: {}, MAPE: {}, MAE: {}'.format(mse, rmse, mape, mae))
        
        return scores_dict