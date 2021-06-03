from matplotlib import pyplot as plt
import pandas as pd
import sys

from loaddata import load_fan2019impact_rec20_by_alg \
        , load_yan2020effort_rec20_by_alg
from violinplot import plot_violin

def plot_violin_by_alg(data, labels, fig_fn, xlabel):
    plot_violin(data, 
            labels=labels, 
            figsize=(4, 2.5),
            xname=xlabel,
            yname='Recall@20%', 
            ylim=(0.0,1.0),
            xlabelrotation=90,
            fig_fn=fig_fn,
            show=True)

def load_rec20_data():
    rec20_list = []
    label_list = []

    rec20,label = load_kamei2012large_pub_rec20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_kamei2012large_rec20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_jiang2013personalized_pofb20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_yang2015deep_pofb20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_yang2016effort_rec20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_yang2017tlel_pofb20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_huang2017supervised_rec20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_liu2017code_rec20() 
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_chen2018multi_acc20() 
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_huang2019revisiting_rec20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_li2020effort_acc20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_yan2020effort_rec20()
    rec20_list.append(rec20)
    label_list.append(label)

    return rec20_list,label_list


def main(argv):
    alg_set,data_dict = load_fan2019impact_rec20_by_alg()
    labels = [k+':Fan19' for k in data_dict.keys()]
    data = [data_dict[k] for k in data_dict]

    alg_set,data_dict = load_yan2020effort_rec20_by_alg()
    labels.extend([k+':Yan20' for k in data_dict.keys()])
    data.extend([data_dict[k] for k in data_dict])

    fig_fn = None
    if len(argv) == 2:
        fig_fn = argv[1]
    plot_violin_by_alg(data, labels, fig_fn, 'Effort-Aware Models')

if __name__=='__main__':
    main(sys.argv)



