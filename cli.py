import typer

from bot.orders import (
    place_market_order,
    place_limit_order,
    place_stop_limit_order,
)

from bot.validators import (
    validate_side,
    validate_order_type,
     validate_positive_number
)

from bot.client import get_price

from bot.utils import display_order, display_error


app = typer.Typer()

@app.command()
def menu():
    try:

        typer.secho(
            "\n🚀 Binance Futures Trading Bot",
            fg=typer.colors.CYAN,
            bold=True
        )

        print("\nSelect Order Type")
        typer.secho("\n[1] Market Order", fg=typer.colors.GREEN)
        typer.secho("[2] Limit Order", fg=typer.colors.BLUE)
        typer.secho("[3] Stop Limit Order", fg=typer.colors.RED)
        choice = typer.prompt("Enter choice")

        symbol = typer.prompt("Enter Symbol").upper()
        side = validate_side(typer.prompt("Enter Side (BUY/SELL)"))

        quantity =float(
            typer.prompt("Enter Quantity")
        )
        quantity = validate_positive_number(quantity, "Quantity")

        current_price = get_price(symbol)
        print(f"\nCurrent Price: {current_price}")


        if choice == "1":

            order = place_market_order(
                symbol,
                side,
                quantity
            )

        elif choice == "2":

            price = float(
                typer.prompt("Enter Limit Price  (e.g. 120000)")
            )
            price = validate_positive_number(price, "Price")

            order = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        elif choice == "3":

            stop_price = float(
                typer.prompt("Enter Stop Price")
            )

            price = float(
                typer.prompt("Enter Limit Price")
            )

            price = validate_positive_number(price, "Price")
            stop_price = validate_positive_number(stop_price, "Stop Price")

            order = place_stop_limit_order(
                symbol,
                side,
                quantity,
                price,
                stop_price
            )

        else:
            typer.secho(
                "Invalid choice",
                fg=typer.colors.RED
            )
            return

        typer.secho("\n✅ SUCCESS", fg=typer.colors.GREEN, bold=True)
        typer.echo("-" * 30)
        display_order(order)

    except ValueError as e:
        display_error("INVALID INPUT", str(e), typer.colors.YELLOW)

    except ConnectionError:
        display_error("NETWORK ERROR", "Unable to connect to Binance.", typer.colors.RED)

    except Exception as e:
        display_error("FAILED", str(e), typer.colors.RED)

@app.command(help="Place a Futures Market, Limit or Stop-Limit Order")
def trade(
    symbol: str = typer.Argument(..., help="Trading symbol e.g. BTCUSDT"),
    side: str = typer.Argument(..., help="BUY or SELL"),
    order_type: str = typer.Argument(..., help="MARKET, LIMIT or STOP_LIMIT"),
    quantity: float = typer.Argument(..., help="Order quantity"),

    price: float = typer.Option(
        None,
        help="Required for LIMIT and STOP_LIMIT orders"
    ),

    stop_price: float = typer.Option(
        None,
        help="Required for STOP_LIMIT orders"
    )
):

    try:

        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_positive_number(quantity, "Quantity")

        typer.secho("\n📋 Order Request", fg=typer.colors.BLUE, bold=True)
        typer.echo("-" * 30)
        typer.echo(f"Symbol: {symbol}")
        typer.echo(f"Side: {side}")
        typer.echo(f"Type: {order_type}")
        typer.echo(f"Quantity: {quantity}")

        if order_type == "STOP_LIMIT":

            price = validate_positive_number(price, "Price")
            stop_price = validate_positive_number(stop_price, "Stop Price")

            order = place_stop_limit_order(
                    symbol,
                    side,
                    quantity,
                    price,
                    stop_price
            )


        elif order_type == "LIMIT":

            price = validate_positive_number(price, "Price")

            order = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        else:

            order = place_market_order(
                symbol,
                side,
                quantity
            )

        typer.secho("\n✅ SUCCESS", fg=typer.colors.GREEN, bold=True)
        typer.echo("-" * 30)
        display_order(order)

    except ValueError as e:
        display_error("INVALID INPUT", str(e), typer.colors.YELLOW)

    except ConnectionError:
        display_error("NETWORK ERROR", "Unable to connect to Binance.", typer.colors.RED)

    except Exception as e:
        display_error("FAILED", str(e), typer.colors.RED)


if __name__ == "__main__":
    app()