import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1)

fig.suptitle('Performance')

#Python:
begin   = np.array([0.000, 0.002, 0.728, 700.957, 13367.875, 13391.949, 19472.967, 19485.017, 19494.000, 19511.842, 25055.615, 25061.653, 25061.781, 25095.694, 25095.791, 25096.067, ])
latency = np.array([25096.074, 0.723, 700.226, 12666.916, 24.071, 6081.015, 12.048, 8.981, 17.839, 5543.770, 6.036, 0.126, 33.910, 0.096, 0.273, 0.005, ])
event   = ["Interpreter", "QUANTIZE", "CONV_2D", "CONV_2D", "MAX_POOL_2D", "CONV_2D", "MAX_POOL_2D", "MUL", "ADD", "CONV_2D", "MAX_POOL_2D", "RESHAPE", "FULLY_CONNECTED", "FULLY_CONNECTED", "SOFTMAX", "DEQUANTIZE", ]
colors  = ["#1864ab", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", ]

data = [[0.002, 0.728, 700.957, 13367.875, 13391.949, 19472.967, 19485.017, 19494.000, 19511.842, 25055.615, 25061.653, 25061.781, 25095.694, 25095.791, 25096.067, ],
        [ 0.723, 700.226, 12666.916, 24.071, 6081.015, 12.048, 8.981, 17.839, 5543.770, 6.036, 0.126, 33.910, 0.096, 0.273, 0.005, ],
        [ 0.000, 55.171, 296.910, 0.000, 142.658, 0.000, 0.000, 0.000, 121.278, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, ]]
columns = ("QUANTIZE", "CONV_2D", "CONV_2D", "MAX_POOL_2D", "CONV_2D", "MAX_POOL_2D", "MUL", "ADD", "CONV_2D", "MAX_POOL_2D", "RESHAPE", "FULLY_CONNECTED", "FULLY_CONNECTED", "SOFTMAX", "DEQUANTIZE", )


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