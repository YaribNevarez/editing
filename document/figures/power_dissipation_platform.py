import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
###########################################################################
# SbS from conference
labels = 'Clocks', 'Signals', 'Logic', 'BRAM', 'DSP', 'CPU', 'PL static'
sizes =  [  0.324,     0.245,   0.236,  0.059, 0.037, 1.445, 0.173]
explode = (     0,         0,       0,      0,      0,    0,     0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Reference architecture with homogeneous AUs using standard floating-point arithmetic (IEEE 754)')
plt.show()

###########################################################################
# Float 32
labels = 'Clocks', 'Signals', 'Logic', 'BRAM', 'DSP', 'CPU', 'PL static'
sizes =  [  0.228,     0.199,   0.174,  0.090, 0.049, 1.412, 0.171]
explode = (     0,         0,       0,      0,      0,    0,     0)


fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Reference architecture with specialized heterogeneous PUs using standard floating-point arithmetic (IEEE 754)')
plt.show()

###########################################################################
# Float 5
labels = 'Clocks', 'Signals', 'Logic', 'BRAM', 'DSP', 'CPU', 'PL static'
sizes =  [  0.232,     0.239,   0.211,  0.094, 0.050, 1.412, 0.174]
explode = (     0,         0,       0,      0,      0,    0,     0)


fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Proposed architecture with specialized heterogeneous PUs using synaptic weight with number representation composed of 4-bit exponent and 1-bit mantissa')
plt.show()

###########################################################################
# Float 4
labels = 'Clocks', 'Signals', 'Logic', 'BRAM', 'DSP', 'CPU', 'PL static'
sizes =  [  0.231,     0.215,   0.194,  0.086, 0.050, 1.412, 0.171]
explode = (     0,         0,       0,      0,      0,    0,     0)


fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Proposed architecture with specialized heterogeneous PUs using synaptic weight with number representation composed of 4-bit exponent')
plt.show()
