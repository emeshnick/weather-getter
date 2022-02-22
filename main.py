import requests
from bs4 import BeautifulSoup

def getdata(url):
  res = requests.get(url)
  return res.text


htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/")

soup = BeautifulSoup(htmldata, 'html.parser')

current_temp = soup.find("span", {"class": "CurrentConditions--tempValue--3a50n"}).text

chances_rain = soup.find("div", {"class": "HourlyWeatherCard--TableWrapper--1IGDr" }).find("span", {"class": "Column--precip--2ck8J"}).text[14:18]

print(chances_rain)

