import os
import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

BASE_URL = "https://demo-fapi.binance.com"

def signed_request(method, endpoint, params=None):

    if params is None:
        params = {}

    params["timestamp"] = int(time.time() * 1000)

    query_string = "&".join(
        [f"{k}={v}" for k, v in params.items()]
    )

    signature = hmac.new(
        API_SECRET.encode(),
        query_string.encode(),
        hashlib.sha256
    ).hexdigest()

    params["signature"] = signature

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    if method.upper() == "GET":
        response = requests.get(
            f"{BASE_URL}{endpoint}",
            params=params,
            headers=headers
        )
    else:
        response = requests.post(
            f"{BASE_URL}{endpoint}",
            params=params,
            headers=headers
        )

    if not response.ok:
        print(response.text)   # temporary debugging
        raise Exception(response.text)

    return response.json()

def get_price(symbol):
    response = signed_request(
        "GET",
        "/fapi/v1/ticker/price",
        {"symbol": symbol}
    )
    return float(response["price"])