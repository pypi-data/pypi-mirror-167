import io
import pandas as pd
import numpy as np
import northgravity as ng

import logging
log = logging.getLogger()



class FileHandler:
    def __init__(self):
        self.th = ng.TaskHandler()
        self.dh = ng.DatalakeHandler()


    # -------------------------------------
    # Task Input and Output related methods
    # -------------------------------------
    def feature_download(self):
        ''' Function to download 'Features Dataset' from DataLake and convert it into pandas DataFrame.

        Returns:
            - Dataframe loaded.
        '''

        log.info('*** DOWNLOAD THE FEATURES DATASET ***')
        f_df_temp_io = self.th.download_from_input_parameter(arg_name='Features Dataset', 
                                                           dest_file_name=None, save=False)
        features_df_raw = pd.read_csv(f_df_temp_io, index_col=0, parse_dates=True, infer_datetime_format=True) 
        features_df_raw.sort_index(inplace=True)
        log.info("Features Dataset loaded.")

        return features_df_raw



    def target_download(self):
        ''' Function to download 'Target Dataset' from DataLake and convert it into pandas DataFrame.

        Returns:
            - Dataframe loaded.
        '''
        log.info('*** DOWNLOAD THE TARGET DATASET ***')
        t_df_temp_io = self.th.download_from_input_parameter(arg_name='Target Dataset', 
                                                           dest_file_name=None, save=False)
        target_df_raw = pd.read_csv(t_df_temp_io, index_col=0, parse_dates=True, infer_datetime_format=True) 
        target_df_raw.sort_index(inplace=True)
        log.info("Target Dataset loaded.")

        return target_df_raw



    def forecast_upload(self, forecast_df, group_name, model_out_name):
        ''' Function to upload the model output (forecast_dataset) to specified group on DataLake.
        ''' 

        log.info('*** UPLOADING THE FORECAST FILE ***')

        forecast_io = io.BytesIO(forecast_df.to_csv(index=False).encode())
        self.th.upload_to_output_parameter(output_name='Forecast Dataset',
                                           file=forecast_io,
                                           group_name=group_name,
                                           file_type='NCSV',
                                           file_upload_name='forecast_dataset_{}.csv'.format(model_out_name.lower()))

        log.info('Forecast Dataset uploaded to {} as forecast_dataset_{}.csv'.format(group_name, model_out_name.lower()))

    

    def test_upload(self, test_df, group_name, model_out_name):
        ''' Function to upload the model output (test_dataset) to specified group on DataLake.
        ''' 

        log.info('*** UPLOADING THE TEST FILE ***')

        test_io = io.BytesIO(test_df.to_csv(index=True).encode())
        self.th.upload_to_output_parameter(output_name='Test Dataset',
                                        file=test_io,
                                        group_name=group_name,
                                        file_type='SOURCE',
                                        file_upload_name='test_dataset_{}.csv'.format(model_out_name.lower()))

        log.info('Test Dataset uploaded to {} as test_dataset_{}.csv'.format(group_name, model_out_name.lower()))



    def drivers_upload(self, drivers_df, group_name, model_out_name):
        ''' Function to upload the model output (drivers_dataset) to specified group on DataLake.
        ''' 

        log.info('*** UPLOADING THE DRIVERS FILE ***')

        drivers_io = io.BytesIO(drivers_df.to_csv(index=False).encode())
        self.th.upload_to_output_parameter(output_name='Drivers Dataset',
                                           file=drivers_io,
                                           group_name=group_name,
                                           file_type='NCSV',
                                           file_upload_name='drivers_dataset_{}.csv'.format(model_out_name.lower()))

        log.info('Drivers Dataset uploaded to {} as forecast_dataset_{}.csv'.format(group_name, model_out_name.lower()))    


    # -------------------------------------
    # Files related methods
    # -------------------------------------

    def ncsv2horizontal(self, raw_df):
        ''' Function to convert the ncsv type files into the horizontal type

        Returns:
            - pd.DateFrame horizontal type
        '''

        index_format = raw_df.index.dtype
        # check if the index is parsed to the date
        assert index_format == 'object', 'The DataFrame index is not an object but {}. Please ensure that you have passed NCSV file, or set the index manually.'.format(index_format)

        df = raw_df.copy()
        df.reset_index(inplace=True)
        # drop metadata
        df.drop(columns=[col for col in df.columns if ('(MD-DB)' in col) or ('(MD-S)' in col) or ('(MD-I)' in col) or ('(MD-D)' in col)], inplace=True)

        # first date column in dataframe - everything before is symbol, everything after are values
        first_date_col = [col for col in df.columns if col.lower().startswith('date')][0]
        loc_first_date_col = df.columns.get_loc(first_date_col)
        # all columns before date
        symbol_df = df.iloc[:, :loc_first_date_col]
        # all columns after (not including) date
        values_cols = df.iloc[:, loc_first_date_col+1:].columns

        # concat all columns values in symbol columns
        symbol = symbol_df.astype(str).apply(lambda x: ' '.join(x), axis=1)
        df.drop(columns=symbol_df, inplace=True)
        df['symbol'] = symbol
        
        # get to horizontal layout
        df_horizontal = df.set_index([first_date_col, symbol])[values_cols].unstack()
        # rename columns and flatten so it's *symbol: value*, not the other way around
        df_horizontal.columns = df_horizontal.columns.get_level_values(1) + ': ' +  df_horizontal.columns.get_level_values(0)
        df_horizontal.index = pd.to_datetime(df_horizontal.index)

        # remove empty columns
        df_horizontal.dropna(how='all', axis=1, inplace=True)
        df = df_horizontal

        df.sort_index(inplace=True)
        log.info('Horizontal datatset loaded: {}'.format(df.tail(10)))

        return df