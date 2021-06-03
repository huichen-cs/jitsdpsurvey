import numpy as np
import sys
from loaddata import load_f1_data, load_lr_f1_data
from violinplot import plot_violin, sort_by_median

def add_baseline_data(data, labels, data_bl, labels_bl):
    data.extend(data_bl[1:])
    for i,e in enumerate(labels_bl):
        if e == 'Zhu20-BL':
            labels_bl[i] = '*Kamei12(DPLR):OS:Z-BL'
        elif e == 'Yang15-BL':
            labels_bl[i] = '*Kamei12(DPLR):OS:Y-BL'
    labels.extend(labels_bl[1:])
    return data,labels

def print_bl_stats(data, labels):
    for b,d in zip(labels,data):
        if b.endswith('-BL') or b.startswith('Kamei12'):
            print('baseline({}): mean={} std={}'
                    .format(b,np.mean(d), np.std(d)))

def main(argv):
    fig_fn='../doc/figures/defect_prone_f1_comparison.pdf'
    show=True
    if len(argv) == 2:
        fig_fn = argv[1]
        show=False
    data,labels = load_f1_data()
    data_bl,labels_bl = load_lr_f1_data()
    data,labels = add_baseline_data(data, labels, data_bl, labels_bl)
    if show:
        print_bl_stats(data, labels)
    highlighted = ['Kamei12(DPLR):OS'
        , 'Yang15(Deeper)'
        , 'Yang17(TLEL)'
        , 'Liu17(CCUM)'
        , 'Young18(DSL)'
        , 'Li20(EATT)'
        , 'Zhu20'
        , '*Kamei12(DPLR):OS:Z-BL'
        , '*Kamei12(DPLR):OS:Y-BL'
        ]
    data,labels = sort_by_median(data, labels, highlighted)
    plot_violin(data, 
            labels=labels, 
            figsize=(8, 3),
            yname='F1', 
            ylim=(0.0,1.0),
            xlabelrotation=45,
            highlighted=highlighted,
            fig_fn=fig_fn,
            show=show)

if __name__=='__main__':
    main(sys.argv)

