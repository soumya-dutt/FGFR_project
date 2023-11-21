import matplotlib.pyplot as plt
import glob

# Define a pattern to match the files you want to include
file_pattern = 'namdenergy_residue_*112.dat'

# Initialize empty lists for x and y values
x_values = []
y_values = []
labels = []

# Define the range for y values
y_range = (-50, 50)

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

# Create a larger figure
plt.figure(figsize=(15, 10))

# Create a line plot for each dataset
for i in range(len(x_values)):
    plt.plot(x_values[i], y_values[i], label=f'File {labels[i]}')

# Add labels and a title using the extracted column names
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(f'Line Plot of {x_label} vs. {y_label}')

# Move the legend outside the plot to the upper right corner
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1.0))
plt.savefig('residue_112_interaction_plot.png')
# Show the plot
plt.show()


