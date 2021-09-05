#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    ind=['United Kingdom','Finland','USA','Sweden','Germany','Russia']
    df=pd.DataFrame({"Year of independence": [np.nan,1917,1776,1523,np.nan,1992],'President': [np.nan,'Niinistö','Trump',np.nan,'Steinmeier','Putin']},index=ind)
    return df
               
def main():
    a=missing_value_types()
    print(a)

if __name__ == "__main__":
    main()
