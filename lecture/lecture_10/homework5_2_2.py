import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

methods = ['euler', 'rk2', 'rk4']
time_steps = [1e-3, 1e-2, 1e-1, 1e0]
path = 'lecture/lecture_10/data/'

errors = {method: [] for method in methods}

# Loop through each method and time step
for method in methods:
    for dt in time_steps:
        file_pattern = path + f'*_t={dt}_{method}.csv'
        files = glob.glob(file_pattern)
        
        df = pd.read_csv(files[0], comment='#', header=0)
        y_numerical = df['posy']
        y_analytical = df['anal_y']
        error = np.mean(np.abs(y_numerical - y_analytical))
        errors[method].append(error)

# Plot the error on a log-log plot
plt.figure(figsize=(10, 5))

for method in methods:
    plt.loglog(time_steps, errors[method], marker='o', label=method)

plt.xlabel(r'Time step ($ \ln dt $)')
plt.ylabel(r'$\ln \varepsilon$')
plt.title('Error vs Time step for different methods')
plt.legend(loc='best')
plt.grid(True)
plt.show()
print("Finish plotting!")