import matplotlib.pyplot as plt
import numpy as np

# Uncomment line below to override default theme
# plt.style.use('sparkle.mplstyle') 

# == Input (replace mock data)
x = np.linspace(1, 20, 500)
y = x**(-1/2)
dy = np.random.normal(0.1, 0.1, 500) / x

label = 'Cats'
xlabel = '$t$ ($h$)' # or None
ylabel = r'IQ ($\mu \Omega$)'
path = 'exports/shaded_error_plot.pdf'  # or None. Make sure the folder exists

# == Styling
FIGSIZE = (3, 2)  # inches
MARGINS = dict(
    left=0.7/FIGSIZE[0], 
    bottom=0.5/FIGSIZE[1],
    right=0.99, 
    top=0.99, 
    )
FILL = dict(
    color="#d7d7d7",
    alpha=1.0,   # opacity
)
LEGEND = dict(
    edgecolor='none',
    facecolor='none',
)

plt.figure(figsize=FIGSIZE)
plt.fill_between(x, y-dy, y+dy, **FILL)
plt.plot(x, y, label=label)
if xlabel: plt.xlabel(xlabel)
if ylabel: plt.ylabel(ylabel)
plt.legend(**LEGEND)
plt.subplots_adjust(**MARGINS)
if path: 
    plt.savefig(path, dpi=600)
    print('Saved figure')
else:
    print('Did not save the figure')

# plt.show()