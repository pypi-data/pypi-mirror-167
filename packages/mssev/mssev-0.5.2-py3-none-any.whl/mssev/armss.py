from pathlib import Path

import numpy as np
import pandas as pd
from pandas.api.types import is_timedelta64_dtype


def _load_armss_reference_table(path, ds='EDSS', age='Age', sep='\t'):
    df = pd.read_csv(path, sep=sep)
    df = df.rename(columns=lambda x: x.replace(ds, 'ARMSS'))
    df = pd.wide_to_long(df, 'ARMSS', i=age, j=ds, sep='.', suffix=r'\d\.\d')
    return df


def ARMSS(df, ref='manouchehrinia', ds='edss', age='ageatedss'):
    if isinstance(ref, str):
        datadir = Path(__file__).parent / 'data'
        ref = (datadir / 'armss' / ref).with_suffix('.tsv')

    if isinstance(ref, Path):
        ref = _load_armss_reference_table(ref)

    df = df[[ds, age]].copy()
    if is_timedelta64_dtype(df[age]):
        df[age] = df[age] // np.timedelta64(1, 'Y')

    df[age] = np.floor(df[age]).clip(upper=75)
    results = df.merge(ref, left_on=[age, ds],
                       right_index=True, how='left')
    return results.ARMSS
