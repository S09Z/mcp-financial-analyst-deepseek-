from mcp.server.fastmcp import FastMCP
from finance_crew import run_financial_analysis

# create FastMCP instance
mcp = FastMCP("financial-analyst")

@mcp.tool()
def analyze_stock(query: str) -> str:
    """Analyzes stock market data based on query and generates
       executable Python code for analysis and visualization"""
    result = run_financial_analysis(query)
    return result

@mcp.tool()
def run_code_and_show_plot() -> str:
    """Execute code and generate a plot"""
    with open('stock_analyis.py', 'r') as f:
        exec(f.read())

if __name__ == "__main__":
    mcp.run(transport="stdio")