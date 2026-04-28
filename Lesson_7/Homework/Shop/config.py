# config.py
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    USERNAME = os.getenv('SAUCE_USERNAME')
    PASSWORD = os.getenv('SAUCE_PASSWORD')
    TOTAL_PRICE = os.getenv('EXPECTED_TOTAL')
