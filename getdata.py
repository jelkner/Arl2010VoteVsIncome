"""Tools to get and clean project data

Copyright 2017 Jeffrey Elkner
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import pandas as pd


def ReadCSV(url):
    """Reads a CSV file from a URL into a Pandas Dataframe.

    url: string url

    returns: Dataframe
    """
    df = pd.io.parsers.read_csv(url)

    return df


def ReadArlingtonData(df):
    """Extract Arlington data from a DataFrame.

    df: pandas DataFrame

    returns: DataFrame with rows containing Arlington
    """


def main():
    pass


if __name__ == '__main__':
    main()
