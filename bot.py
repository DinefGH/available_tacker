import requests
from bs4 import BeautifulSoup
import asyncio
import os
from dotenv import load_dotenv
from telegram import Bot


load_dotenv()
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 300))
product_url = os.getenv("PRODUCT_URL")

async def check_availability():
    url = os.getenv("PRODUCT_URL")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
    
        add_to_cart_button = soup.find("button", {"id": "pdp-add-to-cart-button"})
        
        if add_to_cart_button:
            print("Product is available: Add-to-cart button with ID 'pdp-add-to-cart-button' found!")
            await notify_user()
        else:
            print("Add-to-cart button not found. Product is likely unavailable.")
    else:
        print(f"Failed to fetch the product page. Status code: {response.status_code}")

async def notify_user():
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    bot = Bot(token=bot_token)

    message = f"The product is available! Check it here: {product_url}"

    await bot.send_message(chat_id=chat_id, text=message)
    print("Notification sent via Telegram!")

async def run_checker():
    while True:
        await check_availability()
        await asyncio.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    print(f"Bot started, checking availability every {CHECK_INTERVAL} seconds...")
    asyncio.run(run_checker())
