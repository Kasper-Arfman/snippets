import matplotlib.pyplot as plt
import numpy as np

# Uncomment line below to override default theme
# plt.style.use('sparkle.mplstyle') 

# == Input (replace mock data)
names = ['root', 'leaf', 'flower']

exp_name = r'$\Delta$something'
experim = [10, 11.0, 9.0]
err_exp = [0.4, 0.3, 0.3]  # or None

ctl_name = 'WT'
control = [ 8, 10.3, 8.8]
err_ctl = [0.2, 0.4, 0.3]  # or None

p_value = [0.0001, 0.013, 0.8] # or None

xlabel = 'Tissue type' # or None
ylabel = r'Conductivity $R$ ($\mu \Omega$)'

path = 'exports/example.pdf'  # or None. Make sure the folder exists

# == Styling parameters
FIGSIZE = (6, 4)  # inches
MARGINS = dict(
    left=0.6/FIGSIZE[0], 
    bottom=0.5/FIGSIZE[1],
    right=0.99, 
    top=0.99, 
    )
BAR_PLOT = dict(
    edgecolor='k', 
    capsize=3,
    width=0.8,  # 0.0 - 1.0
    )
CTL_BAR = {**BAR_PLOT, **dict(
    facecolor="#d7d7d7",  # Your favourite colors here
)}
EXP_BAR = {**BAR_PLOT, **dict(
    # facecolor="#4742e0",  # Your favourite colors here
    )}
LEGEND = dict(
    edgecolor='none',
    facecolor='none',
)

TEXT_OFFSET_Y = 0.02  # > 0
SPACE_ABOVE_BARS = 1.2  # > 1

def p_symbol(p, s='✶'):
    if p <= 0.001: return s*3
    if p <= 0.01:  return s*2
    if p <= 0.05:  return s*1
    return '$ns$'

# Compute axis dimensions
if True:
    # Y dimensions
    num_bars = len(experim)
    heights = [max(e+de, c+dc) for e, c, de, dc in zip(experim, control, err_exp or [0]*num_bars, err_ctl or [0]*num_bars)]
    max_height = max(heights)
    text_offset = TEXT_OFFSET_Y * max_height
    ylim = [0, max_height*SPACE_ABOVE_BARS + text_offset]

    # X dimensions
    xlim = [BAR_PLOT.get('width', 1), 2 + 2*num_bars - BAR_PLOT.get('width', 1)]
    x_vals = 2 * np.arange(1, num_bars+1)
    dx = BAR_PLOT.get('width', 1)/2

# Plotting
if True:
    plt.figure(figsize=FIGSIZE)
    plt.bar(x_vals+dx, experim, yerr=err_exp, label=exp_name, **EXP_BAR)
    plt.bar(x_vals-dx, control, yerr=err_ctl, label=ctl_name, **CTL_BAR)
    if p_value is not None:
        for px, py, pval in zip(x_vals, heights, p_value):
            plt.text(px, py+text_offset, p_symbol(pval), ha='center', va='center')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xticks(x_vals, names)
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)
    plt.legend(**LEGEND)
    plt.subplots_adjust(**MARGINS)
    if path: 
        plt.savefig(path, dpi=600)
        print('Saved figure')
    else:
        print('Did not save the figure')
    plt.show()

print('\nFinished successfully')