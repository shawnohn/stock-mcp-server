from mcp.server.fastmcp import FastMCP

mcp = FastMCP("StockMCPServer")


@mcp.resource("market://stock, {symbol}")
def get_stock_price(symbol: str) -> str:
    """Get the current stock price
    Args:
        symbol (str): The symbol of the company to get the stock price for
    Returns:
        str: The current stock price
    """
    return f"The current stock price for {symbol} is $100"


@mcp.resource("market://state")
def get_market_state() -> str:
    """Get the current market state
    Returns:
        str: The current market state
    """
    return "The market is open"


if __name__ == "__main__":
    mcp.run()
