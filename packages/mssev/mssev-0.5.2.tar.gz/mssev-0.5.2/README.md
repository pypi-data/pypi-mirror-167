# python-mssev

This library contains several utilities and scores commonly used in multiple
sclerosis studies.

## Installation

```shell
pip install mssev
```

## Usage

```python
import mssev as ms
```

### Calculating irreversible disability

If you want to calculate some irreversible disability measure (such as the
Expanded Disability Status Scale or EDSS), you can do so with the following code:

```python
followups["IEDSS"] = ms.irreversible_ds(followups, pid="pid", ds="edss", t="date")
```

### Calculating the MSSS

The Multiple Sclerosis Severity Score (MSSS) is obtained by normalising the
Expanded Disability Status Scale (EDSS) score for disease duration and has been
a valuable tool in cross-sectional studies. You can read the original article
[here](https://doi.org/10.1212/01.WNL.0000156155.19270.F8).

You can calculate the MSSS for every patient with the following:

```python
patients["MSSS"] = ms.MSSS(patients, ds="edss", duration="dd")
```

If you want to calculate the MSSS for each follow-up assessment, you can do so
like this:

```python
followups["MSSS"] = ms.MSSS(followups, ds="edss", duration="dd")
```

If you have a cohort of pediatric-onset MS (POMS) patients, you should use the
Ped-MSSS score (see the article [here](https://doi.org/10.1212/WNL.0000000000010414)).
For that, you can either pass `ref="santoro"` to the MSSS function or use the PedMSSS
alias:

```python
# both are equivalent
patients["PedMSSS"] = ms.MSSS(patients, ref="santoro", ds="edss", duration="dd")
patients["PedMSSS"] = ms.PedMSSS(patients, ds="edss", duration="dd")
```

### Calculating the ARMSS

The ARMSS (Age-Related Multiple Sclerosis Severity) score is the result of
standardizing the EDSS by age. Using age for the calculation instead of disease
duration offers several advantages, not least of which are its availability,
ease of measurement and absence of bias. If you want more information, you should
read the original [article](https://doi.org/10.1177%2F1352458517690618).

You can easily calculate the ARMSS for every patient like this:

```python
patients["ARMSS"] = ms.ARMSS(patients, ds="edss", age="ageatedss")
```

Or alternatively, you can calculate it for every follow-up assessment like this:

```python
followups["ARMSS"] = ms.ARMSS(followups, ds="edss", age="ageatedss")
```

### Calculating the P-MSSS

The patient-derived MS Severity Score (P-MSSS) enables patients to rank their
disability relative to others with similar disease duration. It does not require
clinician input which means it can be use in a remote setting or as a more cost-
effective alternative outcome measure for epidemiologic research. If you want
more information, you should check the original article
[here](https://doi.org/10.1212/WNL.0b013e3182872855).

In mssev, the P-MSSS score is implemented by the PMSSS function:

```python
patients["PMSSS"] = ms.PMSSS(patients, ds="pdds", duration="dd")
```