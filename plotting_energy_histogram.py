import matplotlib.pyplot as plt
import glob

# Define a pattern to match the files you want to include
file_pattern = '*namdenergy.dat'

# Initialize empty lists for x and y values
x_values = []
y_values = []
labels = []

# Define the range for y values
y_range = (-5000, 5000)

# Iterate through matching files
for data_file in glob.glob(file_pattern):
    # Initialize empty lists for x and y values for each file
    x = []
    y = []
    
    # Extract the label from the file name
    label = data_file.split('_')[-1].split('.')[0]
    
    with open(data_file, 'r') as file:
        for line_number, line in enumerate(file):
            columns = line.strip().split()
            if line_number == 0:
                x_label = columns[0]
                y_label = columns[-1]
            else:
                x_val = float(columns[0])
                y_val = float(columns[-1])
                
                # Check if the x value is within the specified range
                if y_range[0] <= y_val <= y_range[1]:
                    x.append(x_val)
                    y.append(y_val)
    
    # Append x and y values and label to the respective lists
    x_values.append(x)
    y_values.append(y)
    labels.append(label)

    # Plot the histogram of y values
plt.figure(figsize=(20, 16))

for i in range(len(y_values)):
    plt.hist(y_values[i], bins=200,color='r', edgecolor='black', label=labels[i])

# Set labels and title with specified fontsize
plt.xlabel('Non-bonded energy (kcal/mole)', fontsize=30)
plt.ylabel('Frequency', fontsize=30)
#plt.title('Histogram of Y Values', fontsize=30)

# Set tick label size
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)

# Add legend with specified fontsize
#plt.legend(fontsize=24)
plt.savefig('namd_energy_histogram.png', dpi=200)
# Show the plot
plt.show()

