import pandas as pd


def sort_date(df: pd.DataFrame, add_cols=True) -> pd.DataFrame:
    df = df.set_index('date').to_period('D')
    if add_cols:
        df['dayofweek'] = df.index.dayofweek
        df['week'] = df.index.week
        df['dayofyear'] = df.index.dayofyear
        df['year'] = df.index.year

    return df