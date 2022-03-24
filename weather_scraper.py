# Made with love by Karl
# Contact me on Telegram: @karlpy
# Converted to pandas by hamsolo4744

import datetime as dt
import pandas as pd
from util.UnitConverter import ConvertToSystem


def scrape_station(stationid, start, end=None, units='metric', dropna = True):
    base =  r'https://www.wunderground.com/dashboard/pws/{0}/table/{1}/{1}/daily'
    datef = '%Y-%m-%d'
    blank = dt.datetime.strptime('','')
    toprow = False

    if end == None:
        #only allow one row
        end = start
        toprow = True

    datelist = [[base.format(stationid, (start+dt.timedelta(days=i)).strftime(datef)), start+dt.timedelta(days=i)] for i in range((end-start).days + 1)]
    df = pd.DataFrame()
    for url, date in datelist:
        temp = pd.read_html(url)[-1][1:] #its the last table on the page and the first row is NaN
        # 12:05 PM
        try:
            temp['Time'] = [dt.datetime.strptime(i, '%I:%M %p') for i in temp['Time']]
            temp['td'] = temp['Time']-blank # blank time is 1900, 1, 1, so we subtract that from time to zero the date
            temp['Datetime'] = temp['td']+date # add the time to the date and you get datetime
            temp.drop(['Time','td'], axis=1, inplace=True)
            df = df.append(temp, ignore_index=True)
        except TypeError:
            print("No data for {} on {}".format(stationid, date.strftime(datef)))
            continue

    #print(df)
    df = df.set_index('Datetime')
    converter = ConvertToSystem(units)
    df = converter.clean_and_convert(df)
    if toprow:
        return df[df.index > start].head(1)
    else:
        return df[(df.index > start) & (df.index < end)]

if __name__ == '__main__':    
    start = dt.datetime(2022, 3, 23, 8)
    end   = dt.datetime(2022, 3, 23, 10)
    savepath = r'Weather data {} From {} To {}.csv'
    dtformat = '%Y-%m-%d %H-%M'
    with open('stations.txt', 'r', encoding='utf8') as f:
        stations = [i.strip() for i in f.read().split('\n')]
    for stationid in stations:
        try:
            scrape_station(stationid, start,end).to_csv(savepath.format(stationid, start.strftime(dtformat), end.strftime(dtformat)))
        except KeyError:
            print('Skipped {} due to KeyError, didnt read table'.format(stationid))
        except Exception as e:
            print('Skipped {} due to {}'.format(stationid, e))