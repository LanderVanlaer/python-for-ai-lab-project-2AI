import pandas as pd

import os

import time


def store_model_performance(
    model_name: str,
    R2_score: float,
    mae: float,
    avarage_predication_time: float,
    parameters: dict
):
    COLUMNS = {
        "name": str,
        "R2_score": float,
        "mean_absolute_error": float,
        "avarage_predication_time": float,
        "parameters": object,
    }
    
    filepath = os.path.relpath(
        os.path.join(
            os.path.dirname(__file__),
            "../pickles/dataframe.store_model_performance.pickle")
    ).replace(os.sep, '/')

    if os.path.exists(filepath):
        df = pd.read_pickle(filepath)
    else:
        # https://stackoverflow.com/a/59085030/13165967
        df = pd.DataFrame({c: pd.Series(dtype=t) for c, t in COLUMNS.items()})

    df = pd.concat(
        [
            df,
            pd.DataFrame([{
                "name": model_name,
                "R2_score": R2_score,
                "mean_absolute_error": mae,
                "parameters": parameters,
                "avarage_predication_time": avarage_predication_time,
            }])
        ], ignore_index=True)

    df.to_pickle(filepath)
