import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
"""
This script reads CSV files containing projectile motion data, plots the data using matplotlib, 
and saves the plot as a PNG file. It supports different numerical methods: Euler, RK2, and RK4.
Only input needed is the method name.
"""

# Define the path to the CSV files
method = 'rk2' # select solver ('euler', 'rk2', or 'rk4')
path = f"lecture/lecture_10/data//" # Ubuntu path
# Define the directory and filename for the plot
directory = "lecture/lecture_10/plot"
filename = f'Projectile_motion_{method}.png'
# Pattern to match all CSV files
file_pattern = path + f'*{method}.csv' 

# Get a list of all CSV files in the directory
csv_files = glob.glob(file_pattern)

# Initialize a figure for plotting
plt.figure(figsize=(10, 5))

# Define the property cyclers for color, marker, and linestyle
color_cycler = plt.gca()._get_lines.prop_cycler
marker_cycler = iter(plt.Line2D.filled_markers)
linestyle_cycler = iter(['-', '--', '-.', ':'])

# Loop through the list of CSV files
for file in csv_files:
    # Read the CSV file
    # header must be 0, otherwise it connot read posx, posy, etc...
    df = pd.read_csv(file, comment='#',  header=0)
    # Extract the required columns
    posx = df['posx']
    posy = df['posy']

    # Generate a unique color marker andd linestyle for each file
    color = next(color_cycler)['color']
    marker = next(marker_cycler)
    linestyle = next(linestyle_cycler)

    # Plot the data
    # file = /home/austin/Documents/computer/numerical/lecture/lecture_10/data/euler_t=0.1.csv, etc..., use split to get the method name
    plt.plot(posx, posy, label=file.split('/')[-1].split('_')[1], color=color,  linestyle=linestyle)
    # use t=0.1 as the reference to plot the analytical solution
    if file.split('/')[-1].split('_')[1] == 't=0.1':
        anal_y = df['anal_y']
        plt.plot(posx, anal_y, label='analytical', color='b', linestyle=linestyle)

# set the y axis positive
plt.ylim(0, 50)
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.title(f'Projectile motion by {method} method')
plt.legend(loc='best')
plt.grid('True')

# Create directory for plot if it does not exist
os.makedirs(directory, exist_ok=True)

# Save the plot to the specified directory with the specified filename
plt.savefig(os.path.join(directory, filename))

plt.show()
print("Finish plotting!")