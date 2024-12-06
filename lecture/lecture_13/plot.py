import matplotlib.pyplot as plt
import pandas as pd
import glob
import os

method = 'LF'
exercise = '1'
directory = f"plot_exercise{exercise}"
filename = f'{method}_exercise{exercise}.png'
path = f"data_{method}//"
file_pattern = path + f'*.csv'
color_cycler = plt.gca()._get_lines.prop_cycler
csv_files = glob.glob(file_pattern)

numbers = ['00000', '00200', '00400', '00600', '00800']
plt.figure(figsize=(10, 5))

for file in csv_files:
    for j in numbers:
        if file.split('/')[-1].split('_')[2].split('.')[0] == j:
            df = pd.read_csv(file, comment='#',  header=0)
            x = df['x']
            u = df['u(x)']
            ua = df['ua(x)']
            plt.plot(x, u, label=j, color=color_cycler.__next__()['color'])
            plt.plot(x, ua, color=color_cycler.__next__()['color'], linestyle='dashed')


plt.xlabel('x')
plt.ylabel('u')
plt.title(f'data_{method}')
plt.legend(loc='best')
plt.grid('True')

# Create directory for plot if it does not exist
os.makedirs(directory, exist_ok=True)

# Save the plot to the specified directory with the specified filename
plt.savefig(os.path.join(directory, filename))

plt.show()