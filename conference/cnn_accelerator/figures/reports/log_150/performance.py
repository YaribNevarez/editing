import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1)

fig.suptitle('Performance')

#Python:
begin   = np.array([0.000, 0.011, 1.580, 22.069, 46.287, 54.695, 94.969, 101.031, 103.319, 105.992, 178.976, 180.498, 180.624, 181.228, ])
latency = np.array([181.236, 1.557, 20.487, 24.202, 8.355, 40.271, 6.060, 2.286, 2.273, 72.981, 1.521, 0.124, 0.602, 0.006, ])
event   = ["Interpreter", "CONV_HW", "CONV_HW", "MAX_POOL_2D", "CONV_HW", "CONV_HW", "MAX_POOL_2D", "MUL", "ADD", "CONV_HW", "MAX_POOL_2D", "RESHAPE", "FULLY_CONNECTED", "SOFTMAX", ]
colors  = ["#1864ab", "#94c4df", "#94c4df", "#4a98c9", "#94c4df", "#94c4df", "#4a98c9", "#4a98c9", "#4a98c9", "#94c4df", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", ]

data = [[0.002, 1.570, 22.069, 46.273, 54.644, 94.969, 101.031, 103.319, 105.594, 178.976, 180.498, 180.624, 181.228, ],
        [ 1.566, 20.497, 24.202, 8.370, 40.323, 6.060, 2.286, 2.273, 73.380, 1.521, 0.124, 0.602, 0.006, ],
        [ 1.557, 20.487, 0.000, 8.355, 40.271, 0.000, 0.000, 0.000, 72.981, 0.000, 0.000, 0.000, 0.000, ]]
columns = ("DEPTHWISE_CONV_2D", "CONV_2D", "MAX_POOL_2D", "DEPTHWISE_CONV_2D", "CONV_2D", "MAX_POOL_2D", "MUL", "ADD", "CONV_2D", "MAX_POOL_2D", "RESHAPE", "FULLY_CONNECTED", "SOFTMAX", )


ax1.barh(range(len(begin)),  latency, left=begin, color=colors)
ax1.grid(linestyle = ':')


plt.sca(ax1)
plt.yticks(range(len(begin)), event)
ax1.tick_params(axis='both', which='major', labelsize=5)
ax1.tick_params(axis='both', which='minor', labelsize=1)

plt.xlabel("Schedule (ms)")
plt.ylabel("Task")

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