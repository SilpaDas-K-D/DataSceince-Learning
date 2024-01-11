''' ........Write a program to crawl google weather page and send details to email........'''

import requests

import smtplib 
from scrapy import Selector

city = "Thrissur"
url = "https://www.google.com/search?q=weather" + city 
response = requests.get(url)

if response.status_code == 200:
    response = Selector(text=response.text)

current_temp  = response.xpath('.//div[@class="BNeawe iBp4i AP7Wnd"]/text()').get()
print(f"Current Temperature is {current_temp}")

current_weather = response.xpath('.//div[@class="BNeawe tAd8D AP7Wnd"]/text()').get()
if current_weather : 
    current_weather = current_weather.split(' ')
print(f"Current weather is {current_weather[-1]}")

smtp_object = smtplib.SMTP('smtp.gmail.com', 587) 
smtp_object.starttls() 
          
# Authentication 
smtp_object.login("YOUR EMAIL", "PASSWORD") 
subject = "Weather Reminder"
body = f" Weather condition for today is {current_weather} and temperature is {current_temp} in {city}." 
msg = f"Subject:{subject}\n\n{body}.encode('utf-8') "
    
# sending the mail 
smtp_object.sendmail("FROM EMAIL", "TO EMAIL", msg)
    
# terminating the session 
smtp_object.quit() 
print("Email Sent!") 

