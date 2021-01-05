import numpy as np
import os
import pandas as pd

currentPath = os.path.dirname(__file__)  # Get the directory the current file is in.
parentPath = os.path.dirname(currentPath)
dataDir = os.path.join(parentPath, 'Data')

# Load and Dump data from and to files, using Pandas.
fname = 'SampleData'
floc = os.path.join(dataDir, fname)

# ----- CSV -----
df_csv = pd.read_csv(floc + '.csv', parse_dates=['Time'])  # Dates are not parsed automatically
df_csv.to_csv(floc + '.csv', index=False)

# ---- Excel ----
df_xlsx = pd.read_excel(floc + '.xlsx')
df_xlsx.to_excel(floc + '.xlsx', index=False)

# --- Pickle ----
df_pickled = pd.read_pickle(floc + '.pkl')
df_pickled.to_pickle(floc + '.pkl')

# -- Raw Text ---
with open(floc + '.csv', 'r') as raw_csv:
    text = raw_csv.read()
with open(floc + '.csv', 'r') as raw_csv:
    text_as_lines = raw_csv.readlines()
lines = text.split('\n')[:-1]  # Either split manually, but take care not to take the empty last element of the split
lines = [line.replace('\n', '').split(',') for line in text_as_lines]  # Or use the readlines method and remove the newline characters
headers = lines.pop(0)
df_txt = pd.DataFrame(data=lines, columns=headers)
df_txt.FloatNumbers = pd.to_numeric(df_txt.FloatNumbers)  # Alternatively, .to_numpy(dtype='float64')
df_txt.Time = pd.to_datetime(df_txt.Time)

# Sanity Checks
assert df_csv.SomeStrings.equals(df_txt.SomeStrings) and df_csv.Time.equals(df_txt.Time)
assert np.isclose(df_csv.FloatNumbers, df_txt.FloatNumbers).all()  # Excel float precision is lesser
assert df_csv.SomeStrings.equals(df_xlsx.SomeStrings) and df_csv.Time.equals(df_xlsx.Time)
assert np.isclose(df_csv.FloatNumbers, df_xlsx.FloatNumbers).all()  # Excel float precision is lesser
assert df_csv.SomeStrings.equals(df_pickled.SomeStrings) and df_csv.Time.equals(df_pickled.Time)
assert np.isclose(df_csv.FloatNumbers, df_pickled.FloatNumbers).all()  # Also float precision smh

print("Success!")
