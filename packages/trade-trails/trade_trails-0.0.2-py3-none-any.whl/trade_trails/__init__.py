from unittest.main import MAIN_EXAMPLES
import pandas as pd
from datetime import datetime
import colorama
from colorama import Fore


class futureobject:
    # Future Close Price
    # Fetching Future Close Price from Future Dataset based on Given Time by User
    def close_price(self, time, dataframe):
        """Checking if time param matches our format and return boolean value (True or false)"""
        time = str(time)
        if type(time) == str:
            """if value is not changed in datetime format then it will convert in time format"""
            time = datetime.strptime(time, "%H:%M:%S").time()
            dataframe = dataframe[(dataframe.EXPIRY == dataframe.EXPIRY.min()) & (dataframe.TIME == time)]
        else:
            raise Exception("{} Type is not a String, time format Type should be String '%HH:%MM:%SS'".format(time))
        close_price = dataframe.CLOSE.iloc[0]    #fetching future Close price
        return close_price
FutureClose = futureobject()



class OptionData:
    def __init__(self, dataframe, time="09:20:59", option_type="CE", strike="0000", base_price=200):
        self.dataframe = dataframe 
        self.time = time
        self.option_type = option_type
        self.strike = strike
        self.base_price = base_price
    
    # ATM (At The Money)
    # Fetching ATM(At The Money Strike) and Close price of Call and Put on ATM Strike
    def atm(self):
        """Checking if time param matches our format and return boolean value (True or false)"""
        time = str(self.time)
        if type(time) == str:
            """if value is not changed in datetime format then it will convert in time format"""
            time = datetime.strptime(time, "%H:%M:%S").time()
            call_dataframe = self.dataframe[(self.dataframe.EXPIRY == self.dataframe.EXPIRY.min()) & (self.dataframe.TIME == time) & (self.dataframe.OPTION_TYPE=="CE")]  
            put_dataframe = self.dataframe[(self.dataframe.EXPIRY == self.dataframe.EXPIRY.min()) & (self.dataframe.TIME == time) & (self.dataframe.OPTION_TYPE=="PE")]
        else:
            raise Exception(Fore.RED + "{} Type is not a String, time format Type should be String '%HH:%MM:%SS'".format(self.time))
        """ATM logic"""
        merge_dataframe = pd.merge(call_dataframe[['STRIKE_PRICE','CLOSE']], put_dataframe[['STRIKE_PRICE','CLOSE']], how='inner', left_on=['STRIKE_PRICE'], right_on=['STRIKE_PRICE'], suffixes=['1','2'])
        merge_dataframe['SUBTRACT_VALUE'] = abs(merge_dataframe['CLOSE1']-merge_dataframe['CLOSE2'])
        min_value = merge_dataframe['SUBTRACT_VALUE'].min()
        min_value_dataframe = merge_dataframe[merge_dataframe['SUBTRACT_VALUE'] == min_value]
        atm = min_value_dataframe.STRIKE_PRICE.iloc[0]
        """fetching Call/Put Price on ATM strikes"""
        call_atm_dataframe = call_dataframe[call_dataframe['STRIKE_PRICE'] == atm]
        call_atm_price = call_atm_dataframe.CLOSE.iloc[0]
        put_atm_dataframe = put_dataframe[put_dataframe['STRIKE_PRICE'] == atm]
        put_atm_price = put_atm_dataframe.CLOSE.iloc[0]
        return [{'atm':atm, 'call_atm_price':call_atm_price, 'put_atm_price':put_atm_price}]
    
    # Call Price
    # Call price Function return put price which is fetching Close price of given Time and Particular Strike 
    def call_price(self):
        time = datetime.strptime(str(self.time), "%H:%M:%S").time()
        min_expiry_filter = self.dataframe[(self.dataframe.EXPIRY == self.dataframe.EXPIRY.min()) &  (self.dataframe.OPTION_TYPE == "CE")]
        time_filter = min_expiry_filter[min_expiry_filter.TIME == time]
        if len(time_filter) > 0:
            strike_filter = time_filter[time_filter.STRIKE_PRICE == str(self.strike)]
            if len(strike_filter) > 0:
                call_price = strike_filter.CLOSE.iloc[0]
            else:
                raise ValueError(Fore.RED + ' ** Check your Strike {} input may be it is in wrong format. format Should be in "XXXXX", Without any space **'.format(self.strike))
        else:
            raise ValueError(Fore.RED + ' ** Check your Time {} input may be it is in wrong format. format Should be in "HH:MM:SS". \nMaybe Input Time might not be availble in our Dataset **'.format(self.time))        
        return call_price
    
    # Put Price
    # Put price Function return put price which is fetching Close price of given Time and Particular Strike 
    def put_price(self):
        time = datetime.strptime(str(self.time), "%H:%M:%S").time()
        min_expiry_filter = self.dataframe[(self.dataframe.EXPIRY == self.dataframe.EXPIRY.min()) &  (self.dataframe.OPTION_TYPE == "PE")]
        time_filter = min_expiry_filter[min_expiry_filter.TIME == time]
        if len(time_filter) > 0:
            strike_filter = time_filter[time_filter.STRIKE_PRICE == str(self.strike)]
            if len(strike_filter) > 0:
                put_price = strike_filter.CLOSE.iloc[0]
            else:
                raise ValueError(Fore.RED + ' ** Check your Strike {} input may be it is in wrong format. format Should be in "XXXXX", Without any space **'.format(self.strike))
        else:
            raise ValueError(Fore.RED + ' ** Check your Time {} input may be it is in wrong format. format Should be in "HH:MM:SS". \nMaybe Input Time might not be availble in our Dataset **'.format(self.time))      
        return put_price
    
    # Nearest Base Price 
    # Nearest Base Price Function Which will retrun CLose price of Nearest Base price on a Particular Strike Price
    def nearest_base_price(self):
        time = datetime.strptime(str(self.time), "%H:%M:%S").time()
        min_expiry_filter = self.dataframe[self.dataframe.EXPIRY == self.dataframe.EXPIRY.min()]
        time_filter = min_expiry_filter[min_expiry_filter.TIME == time]
        if len(time_filter) > 0:
            option_type_filter = time_filter[time_filter.OPTION_TYPE == str(self.option_type).upper()]
            if len(option_type_filter) > 0:
                base_price_filter = option_type_filter[option_type_filter.CLOSE >= self.base_price].sort_values('CLOSE')
                nearest_base_price = base_price_filter.CLOSE.iloc[0]
                nearest_base_price_strike = base_price_filter.STRIKE_PRICE.iloc[0]
            else:
                raise ValueError(Fore.RED + ' ** Check your option_type input may be it is in wrong format. format Should be in "CE" or "PE", Without any space **')
        else:
            raise ValueError(Fore.RED + ' ** Check your Time {} input may be it is in wrong format. format Should be in "HH:MM:SS". \nMaybe Input Time might not be availble in our Dataset **'.format(self.time))       
        return [{"nearest_base_price": nearest_base_price, "nearest_base_price_strike": nearest_base_price_strike}]
    
    # Best Of Three Combinations
    # Which will return Call and Put Entry Price and Strike Price
    def best_of_three(self):
        time = str(self.time)
        if type(time) == str:
            time = datetime.strptime(time, "%H:%M:%S").time()
            call_df = self.dataframe[(self.dataframe.EXPIRY == self.dataframe.EXPIRY.min()) & (self.dataframe.OPTION_TYPE == "CE") & (self.dataframe.TIME == time) & (self.dataframe.CLOSE >= self.base_price)].sort_values('CLOSE')
            put_df = self.dataframe[(self.dataframe.EXPIRY == self.dataframe.EXPIRY.min()) & (self.dataframe.OPTION_TYPE == "PE") & (self.dataframe.TIME == time) & (self.dataframe.CLOSE >= self.base_price)].sort_values('CLOSE')
            C1, C2 = call_df.CLOSE.iloc[0], call_df.CLOSE.iloc[1]
            P1, P2 = put_df.CLOSE.iloc[0], put_df.CLOSE.iloc[1]
            """Best 3 Combinations """
            combination1, combination2, combination3 = round(abs(C1 - P1), 2), round(abs(C1 - P2), 2), round(abs(P1 - C2), 2)
            min_comb=min(combination1,combination2,combination3)           # Best Combination
            if min_comb == combination1:
                ce_entry_price, pe_entry_price = C1, P1
            elif min_comb == combination2:
                ce_entry_price, pe_entry_price = C1, P2
            else:
                ce_entry_price, pe_entry_price = C2, P1
            """Fetching Strike """
            if ce_entry_price == C1:
                ce_strike = call_df['STRIKE_PRICE'].iloc[0]
            elif ce_entry_price == C2:
                ce_strike =call_df['STRIKE_PRICE'].iloc[1]
            if pe_entry_price == P1:
                pe_strike = put_df['STRIKE_PRICE'].iloc[0]
            elif pe_entry_price == P2:
                pe_strike = put_df['STRIKE_PRICE'].iloc[1]
        else:
            raise Exception(Fore.RED + "{} Type is not a String, time format Type should be String '%HH:%MM:%SS'".format(self.time))
        return [{'call_strike':ce_strike, 'call_entry_price': ce_entry_price, 'put_strike':pe_strike, 'put_entry_price': pe_entry_price}]
    
    
    
    
class StopLoss:
    def __init__(self, dataframe, entry_time, exit_time, option_type , strike, stoploss_price):
        self.dataframe = dataframe
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.option_type = option_type
        self.strike = strike
        self.stoploss_price = stoploss_price
    
    def sell_stop_loss(self):
        entry_time = datetime.strptime(str(self.entry_time), "%H:%M:%S").time()
        exit_time = datetime.strptime(str(self.exit_time), "%H:%M:%S").time()
        min_expiry_filter = self.dataframe[(self.dataframe.EXPIRY == self.dataframe.EXPIRY.min())]
        time_filter = min_expiry_filter[(min_expiry_filter.TIME > entry_time) & (min_expiry_filter.TIME <= exit_time)].sort_values('TIME')
        if len(time_filter) > 0:
            option_type_filter = time_filter[time_filter.OPTION_TYPE == (self.option_type).upper()]
            if len(option_type_filter) > 0:
                strike_filter = option_type_filter[option_type_filter.STRIKE_PRICE == str(self.strike)].sort_values('TIME')
                if len(strike_filter) > 0:
                    # Stop Loss Checking Here With HIGH
                    stop_loss_check_df = strike_filter[strike_filter.HIGH > self.stoploss_price].sort_values('TIME')
                    if len(stop_loss_check_df) > 0:
                        exit_time = stop_loss_check_df.TIME.iloc[0]
                        exit_price = self.stoploss_price
                    else:
                        exit_time = strike_filter.TIME.iloc[-1]
                        exit_price = strike_filter.CLOSE.iloc[-1]
                else:
                    raise ValueError(Fore.RED + ' ** Check your Strike {} input may be it is in wrong format. format Should be in "XXXXX", Without any space **'.format(self.strike))
            else:
                raise ValueError(Fore.RED + ' ** Check your option_type {} input may be it is in wrong format. format Should be in "CE" or "PE", Without any space **'.format(self.option_type))
        else:
            raise ValueError(Fore.RED + ' ** Check your Time {} input may be it is in wrong format. format Should be in "HH:MM:SS". \nMaybe Input Time might not be availble in our Dataset **'.format(self.time))     
        return [{f'{self.option_type}_exit_time': exit_time, f'{self.option_type}_exit_price': exit_price}]
    
    def buy_stop_loss(self):
        entry_time = datetime.strptime(str(self.entry_time), "%H:%M:%S").time()
        exit_time = datetime.strptime(str(self.exit_time), "%H:%M:%S").time()
        min_expiry_filter = self.dataframe[(self.dataframe.EXPIRY == self.dataframe.EXPIRY.min())]
        time_filter = min_expiry_filter[(min_expiry_filter.TIME > entry_time) & (min_expiry_filter.TIME <= exit_time)].sort_values('TIME')
        if len(time_filter) > 0:
            option_type_filter = time_filter[time_filter.OPTION_TYPE == (self.option_type).upper()]
            if len(option_type_filter) > 0:
                strike_filter = option_type_filter[option_type_filter.STRIKE_PRICE == str(self.strike)].sort_values('TIME')
                if len(strike_filter) > 0:
                    # Stop Loss Checking Here With low
                    stop_loss_check_df = strike_filter[strike_filter.LOW < self.stoploss_price].sort_values('TIME')
                    if len(stop_loss_check_df) > 0:
                        exit_time = stop_loss_check_df.TIME.iloc[0]
                        exit_price = self.stoploss_price
                    else:
                        exit_time = strike_filter.TIME.iloc[-1]
                        exit_price = strike_filter.CLOSE.iloc[-1]
                else:
                    raise ValueError(Fore.RED + ' ** Check your Strike {} input may be it is in wrong format. format Should be in "XXXXX", Without any space **'.format(self.strike))
            else:
                raise ValueError(Fore.RED + ' ** Check your option_type {} input may be it is in wrong format. format Should be in "CE" or "PE", Without any space **'.format(self.option_type))
        else:
            raise ValueError(Fore.RED + ' ** Check your Time {} input may be it is in wrong format. format Should be in "HH:MM:SS". \nMaybe Input Time might not be availble in our Dataset **'.format(self.time))       
        return [{f'{self.option_type}_exit_time': exit_time, f'{self.option_type}_exit_price': exit_price}]
        
        
class FileName:
    def __init__(self, date, instrument="BANKNIFTY"):
        self.instrument = instrument
        self.date = date
        
    def filename(self):
        try:
            dates = datetime.strptime(str(self.date), '%Y-%m-%d').date()
        except:
            dates = datetime.strptime(str(self.date), '%Y/%m/%d').date()
        years = dates.year
        months = dates.month
        days = dates.day
        if months < 10:
            add_months = f"0{months}"
        else:
            add_months = months
        if days < 10:
            add_days = f"0{days}"
        else:
            add_days = days

        if str(self.instrument) == "BANKNIFTY":
            current_filenames = f"BN_{add_days}{add_months}{years}.pkl"
        else:
            current_filenames = f"{self.instrument}_{add_days}{add_months}{years}.pkl"
            
        return [{'filename': current_filenames, 'year':years, 'month': months}]