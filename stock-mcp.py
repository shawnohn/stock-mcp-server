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


@mcp.tool()
def buy_stock(symbol: str, quantity: int) -> str:
    """Buys a stock for a given symbol and quantity
    Args:
        symbol (str): The symbol of the company to buy stock for
        quantity (int): The quantity of stock to buy
    Returns:
        str: A string containing the result of the transaction
    """
    return f"Bough {quantity} shares of {symbol}"


@mcp.tool()
def sell_stock(symbol: str, quantity: int) -> str:
    """Sells a stock for a given symbol and quantity
    Args:
        symbol (str): The symbol of the company to sell stock for
        quantity (int): The quantity of stock to sell
    Returns:
        str: A string containing the result of the transaction
    """
    return f"Sold {quantity} shares of {symbol}"


@mcp.prompt()
def analyze_stock(symbol: str, last_year_profit: str, company_info: str) -> str:
    return f"""
    You are a stock analyst. You are given a stock symbol and you need to analyze the stock.
    Here is the income statement:
    {last_year_profit}
    Here is the company info:
    {company_info}
    Here is the symbol:
    {symbol}
    Make sure to analyze the income statement and company info to give a detailed analysis of the stock.
    Make a recommendation on whether to buy, sell, or hold the stock.
    """


if __name__ == "__main__":
    mcp.run()
