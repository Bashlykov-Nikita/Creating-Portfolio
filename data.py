import pandas as pd
import yfinance as yf

index_names = [
    "SP500",
    "Nasdaq100",
    "DowJones",
    "CAC40",
    "FTSE100",
    "DAX",
    "HSI",
    "Nikkei225",
]

icr_d = {
    name: f"https://github.com/Bashlykov-Nikita/Companies-Returns/blob/main/data/{name}_d.csv?raw=true"
    for name in index_names
}


icr_m = {
    name: f"https://github.com/Bashlykov-Nikita/Companies-Returns/blob/main/data/{name}_m.csv?raw=true"
    for name in index_names
}


def get_returns_df(url: str) -> pd.DataFrame:
    return pd.read_csv(url, index_col=0)


def get_mkt_cap(url: str) -> pd.DataFrame:
    """Retrieve market capitalization data for companies listed in the provided URL.

    Args:
        url (str): URL to the CSV file containing company returns data.

    Returns:
        pandas.DataFrame: DataFrame with market capitalization values for each company.
    """
    mkt_cap_df = []
    comp_names = get_returns_df(url).columns
    for company in comp_names:
        buff = yf.Ticker(company).info["marketCap"]
        mkt_cap_df.append(buff)

    return pd.DataFrame(mkt_cap_df, index=comp_names)
