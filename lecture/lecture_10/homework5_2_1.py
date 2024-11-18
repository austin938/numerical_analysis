import glob
import pandas as pd
import matplotlib.pyplot as plt

method=['euler','rk2','rk4']
dt = 0.1
path = 'lecture/lecture_10/data//'
files = []
for m in method:
    file_pattern = path + f'*_t={dt}_{m}.csv'
    files.extend(glob.glob(file_pattern))

plt.figure(figsize=(10, 5))

# Define the property cyclers for color, marker, and linestyle
color_cycler = plt.gca()._get_lines.prop_cycler
marker_cycler = iter(plt.Line2D.filled_markers)
linestyle_cycler = iter(['-', '--', '-.', ':'])

# Loop through the list of CSV files
for file in files:
    df = pd.read_csv(file, comment='#',  header=0)
    # Extract the required columns
    posx = df['posx']
    posy = df['posy']
    N = len(posx)

    # Generate a unique color marker andd linestyle for each file
    color = next(color_cycler)['color']
    marker = next(marker_cycler)
    linestyle = next(linestyle_cycler)
    label = file.split('/')[-1].split('_')[-1].split('.')[0]

    # Plot the data
    # file = /home/austin/Documents/computer/numerical/lecture/lecture_10/data/euler_t=0.1.csv, etc..., use split to get the method name
    plt.plot(posx, posy, label=label, color=color,  linestyle=linestyle)
    if label == 'rk4':
        anal_y = df['anal_y']
        plt.plot(posx, anal_y, label='analytical', color='b', linestyle=linestyle)

plt.ylim(0, 50)
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.title(f'Projectile motion with dt={dt}s')
plt.legend(loc='best')
plt.grid('True')
plt.show()
print("Finish plotting!")