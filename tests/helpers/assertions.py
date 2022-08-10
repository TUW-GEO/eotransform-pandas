import pandas as pd


def assert_data_frame_eq(actual, expected):
    pd.testing.assert_frame_equal(actual, expected)
