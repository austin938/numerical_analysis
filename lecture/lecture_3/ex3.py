import numpy as np

run_number = 127
over = 1.0
under = 1.0


for i in range(run_number):
    over *= 2.0
    under /= 2.0
print(f"N = {run_number}, under = {under}, over = {over}")