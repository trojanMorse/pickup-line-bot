import requests
from bs4 import BeautifulSoup
import smtplib

from time import time, sleep

URL = 'http://www.pickuplinegen.com/'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find()
    title = soup.find(id="content").get_text()
    print(title)

    # isAvailability = soup.find(id="availability").get_text().strip()
    # print("Is available ", isAvailability)
    # if "unavailable" in isAvailability:
    #     subject = "Product still not available"
    #     send_email(subject)
    #     return
    # price = soup.find(id="priceblock_ourprice").get_text()
    # price = price[:-3]
    # price = price.replace(",", "")
    # converted_price = float(price[2:len(price)])
    # subject = "Price changes"
    # if converted_price < 10000:
    #     send_email(subject)

    # print(converted_price)
    # print(title)


def send_email(subject):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('kavandeveloper@gmail.com', 'iwjfnlmxvhmgjncx')

    body = "Check price, link: "+URL

    msg = f"Subject: {subject} \n\n {body}"

    server.sendmail(
        'kavandeveloper@gmail.com',
        'kavandeveloper@gmail.com',
        msg
    )

    print("email has been sent")

    server.quit()


while True:
    check_price()
