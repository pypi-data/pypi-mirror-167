from pathlib import Path

import numpy as np
import pandas as pd
from pandas.api.types import is_timedelta64_dtype


def _load_pmsss_reference_table(path, ds='PDDS', duration='DD', sep='\t'):
    df = pd.read_csv(path, sep=sep)
    df = df.rename(columns=lambda x: x.replace(ds, 'PMSSS'))
    df = pd.wide_to_long(df, 'PMSSS', i=duration, j=ds, sep='.', suffix=r'\d\.\d')
    return df


def PMSSS(df, ref='narcoms', ds='pdds', duration='dd'):
    if isinstance(ref, str):
        datadir = Path(__file__).parent / 'data'
        ref = (datadir / 'pmsss' / ref).with_suffix('.tsv')

    if isinstance(ref, Path):
        ref = _load_pmsss_reference_table(ref)

    df = df[[duration, ds]].copy()
    if is_timedelta64_dtype(df[duration]):
        df[duration] = df[duration] // np.timedelta64(1, 'Y')

    df[duration] = np.floor(df[duration]).clip(upper=30)
    results = df.merge(ref, left_on=[duration, ds],
                       right_index=True, how='left')
    return results.PMSSS
