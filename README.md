Product Availability Tracker

    This app is a product availability tracker that monitors a specific product's availability on an e-commerce website, such as MediaMarkt. When the product becomes available (indicated by the "Add to Cart" button), the app sends a real-time notification via Telegram to alert the user.


Features

    Periodically checks product availability on the target website.
    Detects the presence of the "Add to Cart" button.
    Sends instant Telegram notifications when the product becomes available.
    Configurable via environment variables.


Requirements

    Python 3.9 or higher
    Dependencies listed in requirements.txt



Installation

1. Clone the Repository

git clone https://github.com/DinefGH/product-availability-tracker.git
cd product-availability-tracker


2. Create a Virtual Environment

python -m venv venv
venv\Scripts\activate  # For Windows: 
source venv/bin/activate  # For Linux/Mac


3. Install Dependencies

pip install -r requirements.txt


4. Set Up the Environment Variables
Create a .env file in the root directory and add the following variables:

# Target product URL
PRODUCT_URL=https://www.mediamarkt.de/de/product/_canon-powershot-g7-x-mark-ii-2106262.html

# Telegram bot credentials
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id

# Interval for checks in seconds (default: 300)
CHECK_INTERVAL=300


5. Run the Script

python bot.py


How It Works
1. Monitoring:
    The script fetches the product page periodically.
    It searches for the "Add to Cart" button (id="pdp-add-to-cart-button").

2. Notification:
    When the button is found, the app sends a Telegram notification to the user with the product link.


Customization

    Interval: Adjust the CHECK_INTERVAL value in the .env file for faster or slower checks.
    Target URL: Update the PRODUCT_URL in the .env file to monitor a different product.


Contributing

    Contributions are welcome! Feel free to submit issues or pull requests to improve the app.