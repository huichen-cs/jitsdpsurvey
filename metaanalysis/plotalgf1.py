from matplotlib import pyplot as plt
import pandas as pd
import sys

from loaddata import load_duan2021impact_f1_by_alg \
        , load_fan2019impact_f1_by_alg
from violinplot import plot_violin

alg_sl_map = {'NB': 'Naive Bayes',
        'RF': 'Random Forest',
        'LR': 'Logistic Regression'}

def plot_violin_by_alg(f1_data, labels, fig_fn):
    plot_violin(f1_data, 
            labels=labels, 
            figsize=(4, 2.5),
            xname='Defect Proneness Models',
            yname='F1', 
            ylim=(0.0,1.0),
            xlabelrotation=90,
            fig_fn=fig_fn,
            show=True)

def main(argv):
    alg_set,f1_dict = load_duan2021impact_f1_by_alg()
    labels = [k+':Duan21' for k in f1_dict.keys()]
    f1_data = [f1_dict[k] for k in f1_dict]

    alg_set,f1_dict = load_fan2019impact_f1_by_alg()
    labels.extend([k+':Fan19' for k in f1_dict.keys()])
    f1_data.extend([f1_dict[k] for k in f1_dict])

    fig_fn = None
    if len(argv) == 2:
        fig_fn = argv[1]
    plot_violin_by_alg(f1_data, labels, fig_fn)

if __name__=='__main__':
    main(sys.argv)



