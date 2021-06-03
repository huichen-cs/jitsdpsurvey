from matplotlib import pyplot as plt
import numpy as np
from loaddata import load_lr_f1_data
from plotf1 import plot_violin


def main():
    data,labels = load_lr_f1_data()
    plot_violin(data, labels=labels, \
        yname='F1', \
        figsize=(8*3/11,5),
        xlabelrotation=90,
        highlighted='all',
        fig_fn='../doc/figures/defect_prone_lr_f1_comparison.pdf', \
        show=True)

if __name__=='__main__':
    main()

