import requests

from bot.client import signed_request
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):

    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "quantity": quantity
        }

        response = signed_request(
            "POST",
            "/fapi/v1/order",
            params
        )

        logger.info(f"Market order success: {response}")

        return response

    except requests.exceptions.ConnectionError:
        logger.error("Network error while connecting to Binance")
        raise Exception("Network error. Please check your internet connection.")

    except requests.exceptions.Timeout:
        logger.error("Request timed out")
        raise Exception("Request timed out.")

    except requests.exceptions.HTTPError as e:
        logger.error(f"API Error: {e}")
        raise Exception(f"Binance API Error: {e}")

    except Exception as e:
        logger.exception("Unexpected error")
        raise


def place_limit_order(symbol, side, quantity, price):

    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "quantity": quantity,
            "price": price,
            "timeInForce": "GTC"
        }

        response = signed_request(
            "POST",
            "/fapi/v1/order",
            params
        )

        logger.info(f"Limit order success: {response}")

        return response

    except requests.exceptions.ConnectionError:
        logger.error("Network error while connecting to Binance")
        raise Exception("Network error. Please check your internet connection.")

    except requests.exceptions.Timeout:
        logger.error("Request timed out")
        raise Exception("Request timed out.")

    except requests.exceptions.HTTPError as e:
        logger.error(f"API Error: {e}")
        raise Exception(f"Binance API Error: {e}")

    except Exception:
        logger.exception("Unexpected error")
        raise

def place_stop_limit_order(
    symbol,
    side,
    quantity,
    price,
    stop_price
):

    try:
        params = {
            "algoType": "CONDITIONAL",
            "symbol": symbol,
            "side": side,
            "type": "STOP",
            "quantity": quantity,
            "price": price,
            "triggerPrice": stop_price,
            "timeInForce": "GTC"
        }

        response = signed_request(
            "POST",
            "/fapi/v1/algoOrder",
            params
        )

        logger.info(
            f"Stop Limit order success: {response}"
        )

        return response

    except requests.exceptions.ConnectionError:
        logger.error(
            "Network error while connecting to Binance"
        )
        raise Exception(
            "Network error. Please check your internet connection."
        )

    except requests.exceptions.Timeout:
        logger.error("Request timed out")
        raise Exception("Request timed out.")

    except Exception:
        logger.exception("Unexpected error")
        raise