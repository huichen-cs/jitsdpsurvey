from matplotlib import pyplot as plt
import numpy as np

def sort_by_median(data, labels, highlighted):
    data_unhled = []
    label_unhled = []
    data_hled = []
    label_hled = []
    for a,b in zip(data,labels):
        if b in highlighted:
            data_hled.append(a)
            label_hled.append(b)
        else:
            data_unhled.append(a)
            label_unhled.append(b)
    
    medians = np.array([np.median(d) for d in data_hled])
    sorted_keys = np.argsort(medians)
    data_hled_new = [data_hled[i] for i in sorted_keys]
    label_hled_new = [label_hled[i] for i in sorted_keys]

    data = data_hled_new + data_unhled
    labels = label_hled_new + label_unhled

    return data,labels

def adjacent_values(vals, q1, q3):
    upper_adjacent_value = q3 + (q3 - q1) * 1.5
    upper_adjacent_value = np.clip(upper_adjacent_value, q3, vals[-1])

    lower_adjacent_value = q1 - (q3 - q1) * 1.5
    lower_adjacent_value = np.clip(lower_adjacent_value, vals[0], q1)
    return lower_adjacent_value, upper_adjacent_value

def set_axis_style(ax, labels, **kwargs):
    ax.xaxis.set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(np.arange(1, len(labels) + 1))
    if 'xlabelrotation' in kwargs:
        ha='center'
        if kwargs['xlabelrotation'] != 90:
            ha = 'right'
        ax.set_xticklabels(labels, rotation=kwargs['xlabelrotation'], ha=ha)
    else:
        ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_xlim(0.25, len(labels) + 0.75)
    if 'ylim' in kwargs:
        ax.set_ylim(kwargs['ylim'][0], kwargs['ylim'][1])
    else:
        ax.set_ylim(0.00, 0.90)

    if 'xname' in kwargs:
        xlabel = kwargs['xname']
    else:
        xlabel = 'Studies'
    ax.set_xlabel(xlabel)


def plot_violin_ax(data, labels, **kwargs):
    figsize=(8,4)
    if 'figsize' in kwargs:
        figsize = kwargs['figsize']
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize, sharey=True)

    if 'yname' in kwargs:
        ax.set_ylabel(kwargs['yname'])
    parts = ax.violinplot(data, showmeans=True, showmedians=False, showextrema=True)

    
    for pc,label in zip(parts['bodies'], labels):
        if 'highlighted' in kwargs \
            and isinstance(kwargs['highlighted'], str) \
            and kwargs['highlighted'] == 'all':
            pc.set_facecolor('gray')
        elif 'highlighted' in kwargs  \
            and label in kwargs['highlighted']:
            pc.set_facecolor('gray')
        else:
            pc.set_facecolor('white')
        pc.set_edgecolor('black')
        pc.set_alpha(1)

    parts['cmeans'].set_color('black')
    parts['cbars'].set_color('black')
    parts['cmins'].set_color('black')
    parts['cmaxes'].set_color('black')
    


    quartile1, medians, quartile3 = \
        np.zeros(len(data)),np.zeros(len(data)),np.zeros(len(data))
    
    for i in range(len(data)):
        quartile1[i], medians[i], quartile3[i] = np.percentile(data[i], [25, 50, 75])
    whiskers = np.array([
        adjacent_values(sorted_array, q1, q3)
        for sorted_array, q1, q3 in zip(data, quartile1, quartile3)])
    whiskers_min, whiskers_max = whiskers[:, 0], whiskers[:, 1]

    inds = np.arange(1, len(medians) + 1)
    ax.scatter(inds, medians, marker='o', color='white', s=30, zorder=3, edgecolor='black')
    ax.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
    ax.vlines(inds, whiskers_min, whiskers_max, color='k', linestyle='-', lw=1)

    if not kwargs is None:
        set_axis_style(ax, labels, **kwargs)
    else:
        set_axis_style(ax, labels)

    return ax


def plot_violin(data, labels, **kwargs):
    plot_violin_ax(data, labels, **kwargs)
#    figsize=(8,4)
#    if 'figsize' in kwargs:
#        figsize = kwargs['figsize']
#    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize, sharey=True)
#
#    if 'yname' in kwargs:
#        ax.set_ylabel(kwargs['yname'])
#    parts = ax.violinplot(data, showmeans=True, showmedians=False, showextrema=True)
#
#    
#    for pc,label in zip(parts['bodies'], labels):
#        if 'highlighted' in kwargs \
#            and isinstance(kwargs['highlighted'], str) \
#            and kwargs['highlighted'] == 'all':
#            pc.set_facecolor('gray')
#        elif 'highlighted' in kwargs  \
#            and label in kwargs['highlighted']:
#            pc.set_facecolor('gray')
#        else:
#            pc.set_facecolor('white')
#        pc.set_edgecolor('black')
#        pc.set_alpha(1)
#
#    parts['cmeans'].set_color('black')
#    parts['cbars'].set_color('black')
#    parts['cmins'].set_color('black')
#    parts['cmaxes'].set_color('black')
#    
#
#
#    quartile1, medians, quartile3 = \
#        np.zeros(len(data)),np.zeros(len(data)),np.zeros(len(data))
#    
#    for i in range(len(data)):
#        quartile1[i], medians[i], quartile3[i] = np.percentile(data[i], [25, 50, 75])
#    whiskers = np.array([
#        adjacent_values(sorted_array, q1, q3)
#        for sorted_array, q1, q3 in zip(data, quartile1, quartile3)])
#    whiskers_min, whiskers_max = whiskers[:, 0], whiskers[:, 1]
#
#    inds = np.arange(1, len(medians) + 1)
#    ax.scatter(inds, medians, marker='o', color='white', s=30, zorder=3, edgecolor='black')
#    ax.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
#    ax.vlines(inds, whiskers_min, whiskers_max, color='k', linestyle='-', lw=1)
#
#    if not kwargs is None:
#        set_axis_style(ax, labels, **kwargs)
#    else:
#        set_axis_style(ax, labels)


    plt.tight_layout()
    if 'fig_fn' in kwargs:
        fig_fn = kwargs['fig_fn']
        if not fig_fn is None:
            plt.savefig(fig_fn)
        if 'show' in kwargs and bool(kwargs['show']):
            plt.show()
    else:
        if not 'show' in kwargs or bool(kwargs['show']):
            plt.show()
