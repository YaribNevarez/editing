import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1)

fig.suptitle('Performance')

#Python:
begin   = np.array([0.000, 0.003, 0.009, 0.027, 0.035, 0.049, 0.058, 0.072, 8.324, 8.327, 8.420, 8.465, 8.558, 8.599, 8.692, 31.581, 43.659, 43.662, 43.845, 43.877, 44.059, 44.085, 44.267, 55.095, 55.097, 55.455, 55.481, 55.839, 55.862, 56.220, 74.523, 80.600, 80.603, 81.314, 81.333, 82.045, 82.059, 82.770, 88.200, 88.203, 89.619, 89.634, 91.051, 91.063, 92.479, 102.171, 105.199, 105.449, 120.744, 120.828, ])
latency = np.array([120.837, 8.319, 0.025, 8.252, 0.022, 7.996, 0.021, 7.924, 23.214, 0.137, 23.116, 0.133, 22.458, 0.133, 22.398, 12.075, 11.410, 0.214, 11.222, 0.208, 10.531, 0.211, 10.493, 19.404, 0.383, 19.042, 0.380, 17.823, 0.379, 17.826, 6.074, 7.587, 0.730, 6.625, 0.724, 5.422, 0.725, 5.415, 13.957, 1.430, 11.941, 1.428, 9.678, 1.427, 9.677, 3.025, 0.249, 15.291, 0.082, 0.008, ])
event   = ["MODEL", "CONV_2D", "DELEGATE", "HARDWARE", "DELEGATE", "HARDWARE", "DELEGATE", "HARDWARE", "CONV_2D", "DELEGATE", "HARDWARE", "DELEGATE", "HARDWARE", "DELEGATE", "HARDWARE", "MAX_POOL_2D", "CONV_2D", "DELEGATE", "HARDWARE", "DELEGATE", "HARDWARE", "DELEGATE", "HARDWARE", "CONV_2D", "DELEGATE", "HARDWARE", "DELEGATE", "HARDWARE", "DELEGATE", "HARDWARE", "MAX_POOL_2D", "CONV_2D", "DELEGATE", "HARDWARE", "DELEGATE", "HARDWARE", "DELEGATE", "HARDWARE", "CONV_2D", "DELEGATE", "HARDWARE", "DELEGATE", "HARDWARE", "DELEGATE", "HARDWARE", "MAX_POOL_2D", "RESHAPE", "FULLY_CONNECTED", "FULLY_CONNECTED", "SOFTMAX", ]
colors  = ["#1864ab", "#4a98c9", "#6faed4", "#94c4df", "#6faed4", "#94c4df", "#6faed4", "#94c4df", "#4a98c9", "#6faed4", "#94c4df", "#6faed4", "#94c4df", "#6faed4", "#94c4df", "#4a98c9", "#4a98c9", "#6faed4", "#94c4df", "#6faed4", "#94c4df", "#6faed4", "#94c4df", "#4a98c9", "#6faed4", "#94c4df", "#6faed4", "#94c4df", "#6faed4", "#94c4df", "#4a98c9", "#4a98c9", "#6faed4", "#94c4df", "#6faed4", "#94c4df", "#6faed4", "#94c4df", "#4a98c9", "#6faed4", "#94c4df", "#6faed4", "#94c4df", "#6faed4", "#94c4df", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", "#4a98c9", ]

data = [[0.003, 335.346, 3507.252, 3519.275, 5049.681, 8096.818, 8102.862, 9497.286, 12278.258, 12281.268, 12281.520, 12296.819, 12296.903, ],
        [ 335.338, 3171.903, 12.020, 1530.403, 3047.134, 6.042, 1394.421, 2780.968, 3.008, 0.249, 15.296, 0.082, 0.008, ],
        [ 8.252, 23.116, 0.000, 11.222, 19.042, 0.000, 6.625, 11.941, 0.000, 0.000, 0.000, 0.000, 0.000, ]]
columns = ("CONV_2D", "CONV_2D", "MAX_POOL_2D", "CONV_2D", "CONV_2D", "MAX_POOL_2D", "CONV_2D", "CONV_2D", "MAX_POOL_2D", "RESHAPE", "FULLY_CONNECTED", "FULLY_CONNECTED", "SOFTMAX", )




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