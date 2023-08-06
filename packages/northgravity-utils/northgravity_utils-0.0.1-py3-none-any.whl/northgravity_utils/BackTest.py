# Libraies
import numpy as np
import pandas as pd
import logging

from .utils import *

log = logging.getLogger()

class BackTest:
    def __init__(self, min_tick=0.5, usd_per_tick=12.5, transaction_cost=0):
        self.min_tick = min_tick
        self.usd_per_tick = usd_per_tick
        self.transaction_cost = transaction_cost

    def long_back_test(self, df: pd.DataFrame, number_of_contracts: float, open_col: str, trading_signal_col: str):
        """Function that create long backtest.

        Args:
            df (pd.DataFrame):                  data, in which there is a column with the price and the signal
            number_of_contracts (int):          number of contracts needed to calculate long backtest
            open_col (str):                     name of price column
            trading_signal_col (str):           name of sifnal column

        Returns:
            df (pd.DataFrame):                  dataframe with long back test results
            bt_score (float):                   annualized profit
        """

        # Prepare dataframe
        df = df.sort_index()
        df = df[[open_col, trading_signal_col]]
        df.columns = ['Price', 'A-Score']

        # *** LONG CONTRACTS ***
        df['Position'] = df['A-Score'].apply(lambda x: state(x, number_of_contracts))
        df['LONG_Position'] = (df['A-Score'].apply(lambda x: abs(x) if x > 0 else 0) / 100 * number_of_contracts).apply(lambda x: int(x))
        df['Enter LONG'] = df['LONG_Position'].diff().fillna(df.iloc[0, 3]).apply(lambda x: x if x > 0 else 0)
        df['Exit LONG'] = np.abs(df['LONG_Position'].diff().apply(lambda x: x if x < 0 else 0))

        price = df['Price'].values.tolist()
        position = df['LONG_Position'].values.tolist()
        enter_position = df['Enter LONG'].values.tolist()

        df['Avg Price LONG'] = average(price, position, enter_position)
        df['Transaction_LONG'] = df.apply(lambda x: transaction_fee(x['Enter LONG'], x['Exit LONG'], self.transaction_cost), axis=1)
        df['P&L LONG'] = (df['Price'] - df['Avg Price LONG']) * df['Exit LONG'] / self.min_tick * self.usd_per_tick - df['Transaction_LONG']

        # *** SHORT CONTRACTS ***
        df['SHORT_Position'] = (df['A-Score'].apply(lambda x: abs(x) if x < 0 else 0) / 100 * number_of_contracts).apply(lambda x: int(x))
        df['Enter SHORT'] = df['SHORT_Position'].diff().fillna(df.iloc[0, 9]).apply(lambda x: x if x > 0 else 0)
        df['Exit SHORT'] = np.abs(df['SHORT_Position'].diff().apply(lambda x: x if x < 0 else 0))

        position = df['SHORT_Position'].values.tolist()
        enter_position = df['Enter SHORT'].values.tolist()
        df['Avg Price SHORT'] = average(price, position, enter_position)

        df['Transaction_SHORT'] = df.apply(lambda x: transaction_fee(x['Enter SHORT'], x['Exit SHORT'], self.transaction_cost), axis=1)
        df['P&L SHORT'] = (df['Avg Price SHORT'] - df['Price']) * df['Exit SHORT'] / self.min_tick * self.usd_per_tick - df['Transaction_SHORT']

        df = df[['P&L LONG', 'P&L SHORT']]
        df['P&L'] = df['P&L LONG'] + df['P&L SHORT']
        df['Running P&L'] = df['P&L'].cumsum()
        df['Running P&L'] = df['Running P&L'].astype('int64')

        # Get the profit & risk final Profit or loss after the validation period
        profit = df['Running P&L'].iloc[-1]
        risk = df['P&L'].std()

        # Risk weighted profit
        bt_score = round(profit / risk, 2)

        return df, bt_score

    def short_back_test(self, df: pd.DataFrame, open_col: str, trading_signal_col: str, is_sharpe_ratio=False):
        """Function that create short backtest.

        Args:
            df (pd.DataFrame):                  data, in which there is a column with the price and the signal
            open_col (str):                     name of price column
            trading_signal_col (str):           name of signal column
            is_sharpe_ratio (bool, optional):   if True - returns sharpe ratio, else - returns annualized profit

        Returns:
            annualized profit (float):          annualized profit per stock market year (is_sharpe_ratio=False)
            sharpe ratio (float):               sharpe ratio (is_sharpe_ratio=True)
        """

        # Prepare dataframe
        df = df.sort_index()
        df = df[[open_col, trading_signal_col]]
        df.columns = ['Price', 'Signal']

        price_diffs = np.diff(df['Price'])
        daily_profits = price_diffs * df['Signal'][:-1] / self.min_tick * self.usd_per_tick
        returns = daily_profits / df['Price'][0]

        if is_sharpe_ratio:
            # Sharpe ratio
            return round((np.mean(returns) / np.std(returns)) * np.sqrt(252), 2)
        else:
            # Annualized profit
            if len(df) < 252:
                log.warning("Annual profit inferred from a small sample size.")
            return round(np.sum(daily_profits) / (len(df)/252), 2)
            