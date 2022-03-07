import requests
from bs4 import BeautifulSoup

def getdata(url):
  res = requests.get(url)
  return res.text

# Gets the html from the weather.com link
htmldata = getdata("https://weather.com/en-IN/weather/today/l/9997af9d31e8bd8419a6acaccbb4e26a4010f26b7425354247dccdd32f5c147f")

soup = BeautifulSoup(htmldata, 'html.parser')

current_temp = soup.find("span", {"class": "CurrentConditions--tempValue--3a50n"}).text

current_precipitation = soup.find("div", {"class": "HourlyWeatherCard--TableWrapper--1IGDr" }).find("span", {"class": "Column--precip--2ck8J"}).text[14:18]

print("current temp is ", current_temp, " and the chance of precipitation is ", current_precipitation)

