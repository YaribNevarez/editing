import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1)

fig.suptitle('Performance')

begin   = np.array([0.000, 0.003, 11.496, 106.300, 130.469, 189.311, 557.976, 564.029, 566.319, 568.596, 1265.665, 1267.183, 1267.310, 1267.917])
latency = np.array([1267.926, 11.490, 94.801, 24.167, 58.840, 368.663, 6.052, 2.287, 2.274, 697.066, 1.516, 0.125, 0.605, 0.007])
event   = ["Interpreter", "DEPTHWISE_CONV_2D", "CONV_2D", "MAX_POOL_2D", "DEPTHWISE_CONV_2D", "CONV_2D", "MAX_POOL_2D", "MUL", "ADD", "CONV_2D", "MAX_POOL_2D", "RESHAPE", "FULLY_CONNECTED", "SOFTMAX"]
colors = ["#1864ab", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9"]


ax1.barh(range(len(begin)),  latency, left=begin, color=colors)
ax1.grid(linestyle = ':')


plt.sca(ax1)
plt.yticks(range(len(begin)), event)
ax1.tick_params(axis='both', which='major', labelsize=5)
ax1.tick_params(axis='both', which='minor', labelsize=1)

plt.xlabel("Schedule (ms)")
plt.ylabel("Task")

data = [[ 0.003, 11.496, 106.300, 130.469, 189.311, 557.976, 564.029, 566.319, 568.596, 1265.665, 1267.183, 1267.310, 1267.917],
        [ 11.490, 94.801, 24.167, 58.840, 368.663, 6.052, 2.287, 2.274, 697.066, 1.516, 0.125, 0.605, 0.007],
        [ 1.366, 20.209, 0.000, 6.255, 12.268, 0.000, 0.000, 0.000, 16.887, 0.000, 0.000, 0.000, 0.000]]

columns = ("DEPTHWISE_CONV_2D", "CONV_2D", "MAX_POOL_2D", "DEPTHWISE_CONV_2D", "CONV_2D", "MAX_POOL_2D", "MUL", "ADD", "CONV_2D", "MAX_POOL_2D", "RESHAPE", "FULLY_CONNECTED", "SOFTMAX")
rows = ["Hardware", "Software", "II OFFSET"]

# Get some pastel shades for the colors
colors = plt.cm.Blues(np.linspace(0.4, 0.8, len(rows)))
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(columns))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    ax2.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(data[row])
# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]
cell_text.reverse()

plt.sca(ax2)
# Add a table at the bottom of the axes
the_table = ax2.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom',
                      fontsize='xx-small')

the_table.auto_set_font_size(False)
the_table.set_fontsize(7)


# Adjust layout to make room for the table:

plt.subplots_adjust(left=0.2, bottom=0.2)

plt.ylabel("Latency (ms)")

plt.xticks([])
ax2.grid(linestyle = ':')


plt.show()