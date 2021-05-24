import matplotlib.pyplot as plt
import numpy as np

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Chocolate', 'Vanilla', 'Strawberry'
total_invoice = [267.1, 388.6, 159.69]
explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

def func(pct, allvals):
    absolute = int(round(pct/100.* np.sum(allvals)))
    return "{:.1f}%\n({:d} $)".format(pct, absolute)

fig1, ax1 = plt.subplots()
ax1.pie(total_invoice, explode=explode, labels=labels, autopct=lambda pct: func(pct, total_invoice),
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


plt.show()