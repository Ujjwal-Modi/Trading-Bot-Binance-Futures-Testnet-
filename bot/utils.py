import typer

def display_order(order):

    if "algoId" in order:
        typer.echo(f"Algo ID: {order.get('algoId')}")
        typer.echo(f"Algo Status: {order.get('algoStatus')}")
        typer.echo(f"Algo Type: {order.get('algoType')}")
        typer.echo(f"Order Type: {order.get('orderType')}")
        typer.echo(f"Symbol: {order.get('symbol')}")
        typer.echo(f"Side: {order.get('side')}")

    else:
        typer.echo(f"Order ID: {order.get('orderId')}")
        typer.echo(f"Status: {order.get('status')}")
        typer.echo(f"Symbol: {order.get('symbol')}")
        typer.echo(f"Side: {order.get('side')}")
        typer.echo(f"Type: {order.get('type')}")
        typer.echo(f"Quantity: {order.get('origQty')}")
        typer.echo(f"Executed Qty: {order.get('executedQty', 'N/A')}")
        typer.echo(f"Avg Price: {order.get('avgPrice', 'N/A')}")

def display_error(title, message, color):
    typer.secho(
        f"\n❌ {title}",
        fg=color,
        bold=True
    )
    typer.echo("-" * 30)
    typer.echo(message)