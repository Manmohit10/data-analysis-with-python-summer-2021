#!/usr/bin/env python3

import pandas as pd

def cities():
    ind=['Helsinki', 'Espoo','Tampere','Vantaa','Oulu']
    df=pd.DataFrame({'Population': [643272, 279044, 231853,223027,201810],
                    "Total area":[715.48,528.03,689.59,240.35,3817.52]},index=ind)
    return df
    

def main():
    print(cities())
    
if __name__ == "__main__":
    main()
