from pathlib import Path

import numpy as np
import pandas as pd
from pandas.api.types import is_timedelta64_dtype


def _load_msss_reference_table(path, ds='EDSS', duration='DD', sep='\t'):
    df = pd.read_csv(path, sep=sep)
    df = df.rename(columns=lambda x: x.replace(ds, 'MSSS'))
    df = pd.wide_to_long(df, 'MSSS', i=duration, j=ds, sep='.', suffix=r'\d\.\d')
    return df


def MSSS(df, ref='roxburgh', ds='edss', duration='dd'):
    if isinstance(ref, str):
        datadir = Path(__file__).parent / 'data'
        ref = (datadir / 'msss' / ref).with_suffix('.tsv')

    if isinstance(ref, Path):
        ref = _load_msss_reference_table(ref)

    df = df[[duration, ds]].copy()
    if is_timedelta64_dtype(df[duration]):
        df[duration] = df[duration] // np.timedelta64(1, 'Y')

    df[duration] = np.floor(df[duration]).clip(upper=30)
    results = df.merge(ref, left_on=[duration, ds],
                       right_index=True, how='left')
    return results.MSSS


def PedMSSS(df, **kwargs):
    return MSSS(df, ref='santoro', **kwargs)
