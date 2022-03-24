# The Weather Scraper (🌩⛈🌤🌞🌨)
Need High-resolution Weather Data for Analytics or Machine-learning in a pandas dataframe? Seek no more.

## Overview
The Weather Scraper downloads high-resolution weather data (often 5 min. intervals) from Wunderground's public weather stations around the world for you.
Outputs to CSV or as a pandas dataframe if you import this as a module.

#### Install dependencies
```python
pip install pandas
```

#### TL;DR
```python
python weather_scraper.py
```  

### How to run TWS?
First, find  the weather stations you are looking for.  
Then you just have to update 1 config file before running TWS. 

1. Go to https://www.wunderground.com/wundermap and zoom in to your location  
    🌞 Click on a weather station and then click on the **Station ID**  (the Station Summary page will open)  
    🌞 Open and copy all Station IDs you need  

2. Set the weather_station ids inside **stations.txt**  
    🌞 *one id per line!*  

If you want to download data from [ISYDNE1240](https://www.wunderground.com/dashboard/pws/ISYDNE1240/table/2022-03-24/2022-03-24/daily) between 2022-03-23 8:53:00 and 2022-03-24 1 21:49:00 in metric units your config.py will look like this:
```
#scrape_station(stationid, start, end, units='metric')
start = dt.datetime(2022, 3, 23, 8, 53)
end   = dt.datetime(2022, 3, 24, 21, 49)
scrape_station('ISYDNE1240', start, end, units='metric')
```

Now you are ready to run your downloads:
```sh
$ python weather_scraper.py
```
Wait until TWS finishes writing your data to files with this naming pattern ***Weather data stationid From start To end.csv***!  

You resulting CSV file will look something like this (if you format it nicely)  

![CSV example](https://raw.githubusercontent.com/Karlheinzniebuhr/the-weather-scraper/master/resources/csv.JPG)
