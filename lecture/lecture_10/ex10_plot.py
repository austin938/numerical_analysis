import pandas as pd
import matplotlib.pyplot as plt
import os
import glob

# Define the path to the CSV files
path = r"/home/austin/Documents/computer/numerical/lecture/lecture_10/data//" # Ubuntu path
# Define the directory and filename for the plot
directory = "lecture/lecture_10/plot"
filename = 'Projectile_motion.png'
# Pattern to match all CSV files
file_pattern = path + '*.csv' 

# Get a list of all CSV files in the directory
csv_files = glob.glob(file_pattern)

# Initialize a figure for plotting
plt.figure(figsize=(10, 5))

# Loop through the list of CSV files
for file in csv_files:
    # Read the CSV file
    # header must be 0, otherwise it connot read posx, posy, etc...
    df = pd.read_csv(file, comment='#',  header=0)
    # Extract the required columns
    posx = df['posx']
    posy = df['posy']
    
    # Plot the data
    # file = /home/austin/Documents/computer/numerical/lecture/lecture_10/data/euler_t=0.1.csv, etc..., use split to get the method name
    plt.plot(posx, posy, label=file.split('/')[-1].split('_')[1], marker='o')
    # use t=0.1 as the reference to plot the analytical solution
    if file.split('/')[-1].split('_')[1] == 't=0.1':
        anal_y = df['anal_y']
        plt.plot(posx, anal_y, label='analytical', marker='o')

# set the y axis positive
plt.ylim(0, 50)
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.title('Projectile motion by euler method')
plt.legend(loc='best')
plt.grid('True')

# Ensure the directory exists, otherwise auto create it
os.makedirs(directory, exist_ok=True)

# Save the plot to the specified directory with the specified filename
plt.savefig(os.path.join(directory, filename))

plt.show()
print("Finish plotting!")