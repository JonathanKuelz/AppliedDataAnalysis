import datetime
import numpy as np
import pandas as pd
import string
import random


def main():
    columns = ['FloatNumbers', 'Integers', 'SomeStrings', 'Time']
    nr_rows = 10000
    df = pd.DataFrame(columns=columns)
    df.FloatNumbers = np.random.rand(nr_rows) * np.random.randint(0, 1e6, nr_rows)
    df.Integers = np.random.randint(0, 1e6, nr_rows)
    strings = [''.join([random.choice(string.ascii_letters) for _ in range(10)]) for row in range(nr_rows)]
    df.SomeStrings = strings
    start_date = datetime.datetime(1994, 10, 25)
    df.Time = [start_date + datetime.timedelta(days=random.randint(0, 9565)) for i in range(nr_rows)]
    df.to_csv('SampleData.csv', index=False)
    df.to_excel('SampleData.xlsx', index=False)
    df.to_pickle('SampleData.pkl')


if __name__ == '__main__':
    main()
    print("Data Samples creation done.")
