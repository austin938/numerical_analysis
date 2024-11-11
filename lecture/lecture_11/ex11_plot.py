import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

dt = 0.0001

# some path
path = f"lecture/lecture_11/data//"
directory = "lecture/lecture_11/plot"
filename = f'binary_{dt}.png'

# Pattern to match all CSV files
file_pattern = path + f'*.csv' 

# Get a list of all CSV files in the directory
csv_files = glob.glob(file_pattern)

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
    x = df['x']
    y = df['y']

    # Generate a unique color marker andd linestyle for each file
    color = next(color_cycler)['color']
    marker = next(marker_cycler)
    linestyle = next(linestyle_cycler)

    # Plot the data
    # file = /home/austin/Documents/computer/numerical/lecture/lecture_11/data/binary_001.csv, etc..., use split to get the method name
    plt.plot(x, y, label=file.split('/')[-1].split('_')[1].split('.')[0], color=color,  linestyle=linestyle)
    # use t=0.1 as the reference to plot the analytical solution
    

# set the y axis positive
plt.xlabel('x(cm)')
plt.ylabel('y(cm)')
plt.title(f'orbits of binary systems with dt={dt}')
plt.legend(loc='best')
plt.grid('True')

# Create directory for plot if it does not exist
os.makedirs(directory, exist_ok=True)

# Save the plot to the specified directory with the specified filename
plt.savefig(os.path.join(directory, filename))

plt.show()
print("Finish plotting!")