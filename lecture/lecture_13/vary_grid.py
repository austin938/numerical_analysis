import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import os

method = 'LW'
N = [50, 126, 316, 793, 1991, 5000]

path = f"data_{method}//"

# manually choose the file at t=0.56
file = os.path.join(path+f'advection_{method}_07000.csv')

df = pd.read_csv(file, comment='#',  header=0)
diff = df['diff']
error = np.sum(diff) / N[5]

outdir = "exercise_1(3)/"+method

if not os.path.isdir(outdir):
    os.mkdir(outdir)

filename = os.path.join(outdir, f"{method}.csv")

f = open(filename, "a")
# f.write(f"N,error\n")
f.write(f"{N[5]:d},{error:e}\n")

f.close()