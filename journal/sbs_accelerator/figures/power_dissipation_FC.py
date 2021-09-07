import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
###########################################################################
# Float 32
labels = 'Clocks', 'Logic', 'DSP', 'Data', 'BRAM', 'I/O'
sizes =  [     16,      24,     6,     14,      6,  0.1]
explode = (     0,       0,     0,      0,      0,  0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

###########################################################################
# Float 5
labels = 'Clocks', 'Logic', 'DSP', 'Data', 'BRAM', 'I/O'
sizes =  [     19,      29,     6,      8,      4,  0.1]
explode = (     0,       0,     0,      0,      0,  0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

###########################################################################
# Log 4
labels = 'Clocks', 'Logic', 'DSP', 'Data', 'BRAM', 'I/O'
sizes =  [     19,      28,     6,      8,      4,  0.1]
explode = (     0,       0,     0,      0,      0,  0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
