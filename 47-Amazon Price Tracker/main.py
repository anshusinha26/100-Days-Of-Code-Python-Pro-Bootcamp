# -------------------- MODULES -------------------- 
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
from dotenv import load_dotenv

load_dotenv()

# -------------------- GETTING DATA FROM AMAZON --------------------
amEndpoint = "https://www.amazon.in/Logitech-MX-Master-3S-Chrome-Graphite/dp/B0B11LJ69K/ref=sr_1_3"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15",
    "Accept-Language": "en-IN,en-GB;q=0.9,en;q=0.8"
}

try:
    amResponse = requests.get(url=amEndpoint, headers=headers)
    amResponse.raise_for_status()

    amWebpage = amResponse.text
    soup = BeautifulSoup(amWebpage, "lxml")

    # Check if CAPTCHA page is present
    if "captcha" in amWebpage.lower():
        print("CAPTCHA page detected. Unable to retrieve product information.")
    else:
        # Attempt to find the product title
        productNameTag = soup.find(name="span", id="productTitle")
        if productNameTag:
            productName = productNameTag.getText().strip()
        else:
            print("Product title not found.")
            productName = "Unknown Product"

        # Attempt to find the product price
        productPriceTag = soup.find(name="span", class_="a-price-whole")
        if productPriceTag:
            productPrice = productPriceTag.getText().replace(",", "")
            productPrice = float(productPrice)
        else:
            print("Product price not found.")
            productPrice = None

        print(f"Product: {productName}")
        print(f"Price: ₹{productPrice if productPrice else 'Not available'}")

        # -------------------- SENDING EMAIL --------------------
        MY_EMAIL = os.getenv("SENDER")
        PASSWORD = os.getenv("PASSWORD")
        receiver = os.getenv("RECEIVER")

        preferredPrice = 14000.0  # Example threshold for sending email

        if productPrice and productPrice < preferredPrice:
            message = MIMEMultipart()
            message["Subject"] = "Amazon price alert 🤑"
            message["From"] = MY_EMAIL
            message["To"] = receiver

            body = f"{productName} is now priced at ₹{productPrice}"
            message.attach(MIMEText(body, "plain"))

            # Adding image to email
            imageURL = "https://m.media-amazon.com/images/I/61ni3t1ryQL._SL1500_.jpg"
            imageResponse = requests.get(imageURL)
            image = MIMEImage(imageResponse.content)
            image.add_header('Content-Disposition', 'attachment', filename='mouse.jpg')
            message.attach(image)

            with smtplib.SMTP("smtp.gmail.com", port=587, timeout=25) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=receiver, msg=message.as_string())
            print("Email sent successfully.")
        elif productPrice is None:
            print("Price not available; email not sent.")
        else:
            print(f"Price is higher than preferred price of ₹{preferredPrice}. Email not sent.")

except requests.RequestException as e:
    print(f"Error fetching data from Amazon: {e}")
