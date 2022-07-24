import smtplib
import requests
from bs4 import BeautifulSoup

MY_EMAIL = "harmelikyan@yahoo.com"
PASSWORD = "fepjyawayltdzziy"

response = requests.get("https://www.amazon.co.uk/Logitech-Calling-Recording-Microphones-Adjustable/dp/B006A2Q81M/ref="
                        "sr_1_5?crid=2F9WKTW3G9GWN&keywords=webcam&qid=1654348260&sprefix=webcam%2Caps%2C71&sr=8-5",
                        headers={"Accept-Language":"en-US,en;q=0.9,hy;q=0.8",
                                 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                                               "(KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
})
resp_to_text = response.text
soup = BeautifulSoup(resp_to_text, "html.parser")
price = soup.find(name='span', class_="a-offscreen")
price_num = float(price.getText()[1:])
product_name = "Logitech C920 HD Pro Webcam, Full HD 1080p/30fps Video Calling, Clear Stereo Audio, " \
               "HD Light Correction, Works with Skype, Zoom, FaceTime, Hangouts, PC/Mac/Laptop/Macbook/Tablet - Black"
product_link = "https://www.amazon.co.uk/Logitech-Calling-Recording-Microphones-Adjustable/dp/B006A2Q81M/ref=sr_" \
               "1_5?crid=2F9WKTW3G9GWN&keywords=webcam&qid=1654348260&sprefix=webcam%2Caps%2C71&sr=8-5"
target_price = 30

if price_num >= target_price:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs='harut92222@gmail.com',
                            msg=f"The {product_name}\nlink {product_link}\nHas dropped to {price_num}")
        print(f"The {product_name}\nlink {product_link}\nHas dropped to {price_num}")
