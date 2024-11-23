# Item Stock Checker and Email Notification Script

This Python script automates the process of checking if an item is in stock on a specified website and sends an email notification if the item is available.

## Features

- Scrapes a website to check stock status using BeautifulSoup.
- Sends an email notification if the item is in stock.
- Configurable via environment variables for flexibility.

## Requirements

- Python 3.6 or newer
- The following Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `smtplib`
  - `email`
  - `python-dotenv`

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install dependencies**:

   ```bash
   pip install requests beautifulsoup4 python-dotenv
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory and define the following variables:

   ```env
   url=<URL of the webpage>
   stockSelector=<CSS selector for stock status>
   itemNameSelector=<CSS selector for item name>
   sizeSelector=<CSS selector for size>
   TO_EMAIL=<Recipient email address>
   FROM_EMAIL=<Sender email address>
   SMTP_PORT=<SMTP server port, e.g., 587>
   LOGIN=<Email login username>
   PASSWORD=<Email login password> # Use an app password for Gmail
   ```

4. **Run the script**:
   ```bash
   python script_name.py
   ```

## Usage

1. Define the product page URL and the appropriate CSS selectors for:

   - Stock status
   - Item name
   - Size

2. Ensure email credentials are set in the `.env` file.

3. Run the script to check the stock and send notifications when applicable. For best usage, use something like github workflows to automate the task and notification.

## Code Workflow

### 1. Scraping the Website

The `check_item_in_stock` function:

- Fetches the webpage content using the `requests` library.
- Parses the HTML content using `BeautifulSoup`.
- Extracts the stock status, item name, and size from the page using CSS selectors.
- If the item is in stock, it returns a success message with the item details. Otherwise, it returns a message stating the item is out of stock.

### 2. Sending an Email

The `send_email` function:

- Sends an email using Gmail's SMTP server (`smtp.gmail.com`).
- The email is configured using the details from the `.env` file, including the sender and recipient addresses, subject, and message body.
- The email is sent securely using TLS encryption, and an App Password is used for authentication.

### 3. Environment Variables

Sensitive information like email credentials and webpage details is stored securely in the `.env` file. The `dotenv` library is used to load these environment variables into the script.

### 4. Main Logic

- The script runs the `check_item_in_stock` function to scrape the webpage and check stock status.
- If the item is in stock, it triggers the `send_email` function to notify the user.
- The script only sends an email if the item is available for purchase, ensuring unnecessary notifications are avoided.

---

## Environment Variables Example

```env
url=https://example.com/product-page
stockSelector=.stock-status
itemNameSelector=.item-name
sizeSelector=.size
TO_EMAIL=recipient@example.com
FROM_EMAIL=sender@example.com
SMTP_PORT=587
LOGIN=your-email@example.com
PASSWORD=your-email-password
```

## Troubleshooting

### Gmail SMTP Authentication

- Use a Gmail **App Password** instead of your regular password for authentication.
- Follow this guide to [create an App Password for Gmail](https://support.google.com/accounts/answer/185833?hl=en).

### Selectors Not Working

- Ensure the CSS selectors (`stockSelector`, `itemNameSelector`, `sizeSelector`) match the structure of the target webpage.
- Use your browser's developer tools to inspect elements and verify the correct selectors.

### Dependencies Not Installed

- Verify that all required Python libraries are installed by running the following command:
