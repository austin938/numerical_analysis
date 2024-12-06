import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Paths to the CSV files
path_lf = "exercise_1(3)/LF/LF.csv"
path_lw = "exercise_1(3)/LW/LW.csv"

# Read the CSV files into DataFrames
df_lf = pd.read_csv(path_lf, comment='#', header=0)
df_lw = pd.read_csv(path_lw, comment='#', header=0)

# Extract the columns for N and error
N_lf = df_lf['N']
error_lf = df_lf['error']
N_lw = df_lw['N']
error_lw = df_lw['error']

# Create a log-log plot
plt.figure(figsize=(10, 5))
plt.loglog(N_lf, error_lf, 'o-', label='Lax-Friedrichs (LF)')
plt.loglog(N_lw, error_lw, 's-', label='Lax-Wendroff (LW)')
plt.xlabel('Number of Grid Cells (N)')
plt.ylabel('Error (E)')
plt.grid(True, which="both", ls="--")
plt.legend(loc='best')
plt.title('Log-Log Plot of Error vs. Number of Grid Cells')
plt.savefig('exercise_1(3)/compare.png')
plt.show()