import pandas as pd
import io

def read_info(df):
    print("The number of rows is: %d"%df.shape[0])
    print("The number of columns is: %d"%df.shape[1])
    buf = io.StringIO()
    df.info(buf=buf)
    info = buf.getvalue()
    info = buf.getvalue().split('\n')[-2]
    print(info)
