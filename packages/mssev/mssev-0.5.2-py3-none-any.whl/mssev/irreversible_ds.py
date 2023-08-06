import numpy as np
import pandas as pd


def irreversible_ds(df, pid='pid', ds='edss', t='date'):
    results = pd.Series([], dtype=df[ds].dtype)
    grouped = df.sort_values(t, ascending=False).groupby(pid)
    for _, rows in grouped:
        idss = rows[ds].cummin()
        results = pd.concat([results, idss])
    return results.loc[df.index]
