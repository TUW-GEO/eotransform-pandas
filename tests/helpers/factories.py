import pandas as pd


def make_dataset(index, **columns):
    df = pd.DataFrame(data=columns)
    df.set_index(index, inplace=True)
    return df
