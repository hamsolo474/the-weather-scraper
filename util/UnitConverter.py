import re

class ConvertToSystem:
    supported_systems = ["metric", "imperial"]
    round_to_decimals = 2
    extract_numbers_pattern = "\d*\.\d+|\d+"

    def __init__(self, system):
        if system not in self.supported_systems:
            raise ValueError('unit system not supported')
        else:
            self.system = system

    def temperature(self, col):
        for field in col:
            try:
                fahrenheit = float(re.findall(self.extract_numbers_pattern, field)[0])
                if self.system == "metric":
                    celsius = (fahrenheit - 32) * 5/9
                    return round(celsius, self.round_to_decimals)
                else:
                    return fahrenheit
            except Exception as e:
                print(f'{e}! probably caused by an empty row in the data')
                return None

    def humidity(self, col):
        for field in col:
            try:
                humidity = float(re.findall(self.extract_numbers_pattern, field)[0])
                return humidity
        
            except Exception as e:
                print(f'{e}! probably caused by an empty row in the data')
                return None

    def speed(self, col):
        for field in col:
            try:
                mph = float(re.findall(self.extract_numbers_pattern, field)[0])
                if self.system == "metric":
                    kmh = mph * 1.609
                    return round(kmh, self.round_to_decimals)
                else:
                    return mph

            except Exception as e:
                print(f'{e}! probably caused by an empty row in the data')
                return None

    def pressure(self, col):
        for field in col:
            try:
                inhg = float(re.findall(self.extract_numbers_pattern, field)[0])
                if self.system == "metric":
                    hpa = inhg * 33.86389
                    return round(hpa, self.round_to_decimals)
                else:
                    return inhg
                
            except Exception as e:
                print(f'{e}! probably caused by an empty row in the data')
                return None
    
    def precipitation(self, col):
        for field in col:
            try:
                inches = float(re.findall(self.extract_numbers_pattern, field)[0])
                if self.system == "metric":
                    mm = inches * 25.4
                    return round(mm, self.round_to_decimals)
                else:
                    return inches
                
            except Exception as e:
                print(f'{e}! probably caused by an empty row in the data')
                return None

    def uv(self, col):
        for field in col:
            try:
                measure = float(re.findall(self.extract_numbers_pattern, field)[0])
                return measure
            
            except Exception as e:
                print(f'{e}! probably caused by an empty row in the data')
                return None

    def solar(self, col):
        for field in col:
            try:
                measure = float(re.findall(self.extract_numbers_pattern, field)[0])
                return measure
            
            except Exception as e:
                print(f'{e}! probably caused by an empty row in the data')
                return None

    def clean_and_convert(self, df):
        #converted_dict_list = []
        print(len(df))
        for key in df.columns:
        #    converted_dict = {}
            if   key == 'Temperature':
                df['Temperature']  = self.temperature(df['Temperature'])
            elif key == 'Dew Point':
                df['Dew Point']    = self.temperature(df['Dew Point'])
            elif key == 'Humidity':
                df['Humidity']     = self.humidity(df['Humidity'])
            elif key == 'Speed':
                df['Speed']        = self.speed(df['Speed'])
            elif key == 'Gust':
                df['Gust']         = self.speed(df['Gust'] )
            elif key == 'Pressure':
                df['Pressure']     = self.pressure(df['Pressure'])
            elif key == 'Precip. Rate.':
                df['Precip. Rate.']  = self.precipitation(df['Precip. Rate.'])
            elif key == 'Precip. Accum.':
                df['Precip. Accum.'] = self.precipitation(df['Precip. Accum.'])
            elif key == 'Solar':
                df['Solar']        = self.solar(df['Solar'] )
        if self.system == 'metric':
            df.rename(columns={'Temperature': 'Temperature_C',	'Dew Point': 'Dew_Point_C',	'Humidity': 'Humidity_%',	'Wind': 'Wind',	'Speed': 'Speed_kmh',	'Gust': 'Gust_kmh',	'Pressure': 'Pressure_hPa',	'Precip. Rate.': 'Precip_Rate_mm',	'Precip. Accum.': 'Precip_Accum_mm',	'UV': 'UV',   'Solar': 'Solar_w/m2'}, inplace=True)
        elif self.system == 'imperial':
            df.rename(columns={'Temperature': 'Temperature_F',	'Dew Point': 'Dew_Point_F',	'Humidity': 'Humidity_%',	'Wind': 'Wind',	'Speed': 'Speed_mph',	'Gust': 'Gust_mph',	'Pressure': 'Pressure_in',	'Precip. Rate.': 'Precip_Rate_in',	'Precip. Accum.': 'Precip_Accum_in',	'UV': 'UV',   'Solar': 'Solar_w/m2'}, inplace=True)
            #converted_dict_list.append(converted_dict)

        return df