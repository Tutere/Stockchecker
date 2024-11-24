import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os

# importing necessary functions from dotenv library
from dotenv import load_dotenv
load_dotenv()

# # Scraping function
def check_item_in_stock(url, stockSelector, itemNameSelector, sizeSelector):
    """
    Scrapes the website and checks if the item is in stock.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        stockStatusElement = soup.select_one(stockSelector)  # Use the CSS selector
        itemNameElement = soup.select_one(itemNameSelector)
        sizeElement = soup.select_one(sizeSelector)
        if stockStatusElement and itemNameElement and sizeElement:
            print("Elements found. Item: " +  itemNameElement.text.strip() + " Size: " + sizeElement.text.strip() + " Stock level: " + stockStatusElement.text.strip())
            in_stock = bool("Add to Cart" in stockStatusElement.text.strip())
            return {
                "status": in_stock,
                "message": itemNameElement.text.strip() + " is in stock. Check it out here: " + url if in_stock else "Item is out of stock"
            }
        else:
            print("Elements not found. Check your selectors.")
            return {
                "status": False,
                "message": "Elements not found. Check your selectors."
            }
    else:
        print("Failed to fetch webpage. Status code:", response.status_code)
        return {
            "status": False,
            "message": "Failed to fetch webpage. Status code: " + response.status_code
        }


# Email function
def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, login, password):
    """
    Sends an email notification.
    """
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(login, password)  # Log in using the app password
            server.sendmail(from_email, to_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

# # Main function
def main():
    url = f"{os.getenv('URL')}"
    stockSelector = f"{os.getenv('STOCK_SELECTOR')}"
    itemNameSelector = f"{os.getenv('ITEM_NAME_SELECTOR')}"
    sizeSelector = f"{os.getenv('SIZE_SELECTOR')}"
    

    # Check stock and set email fields
    result = check_item_in_stock(url, stockSelector,itemNameSelector, sizeSelector)
    email_details = {
        "subject": "Item In Stock Notification",
        "body": f"{result['message']}",
        "to_email": f"{os.getenv('TO_EMAIL')}", 
        "from_email": f"{os.getenv('FROM_EMAIL')}", 
        "smtp_server": "smtp.gmail.com",
        "smtp_port": f"{os.getenv('SMTP_PORT')}", 
        "login": f"{os.getenv('LOGIN')}", 
        "password": f"{os.getenv('PASSWORD')}" 
    }

    # Send email logic
    if result['message'] != "Item is out of stock":
        send_email(**email_details)
    else:
        print("Item out of stock and no issues with request so email not sent.")

if __name__ == "__main__":
    main()