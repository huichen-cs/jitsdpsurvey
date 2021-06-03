import numpy as np
import sys

from matplotlib import pyplot as plt

from plotjiang2013personalizedf1 import \
        load_perf_list as load_jiang2013personalized_perf_list
from plottourani2016impactf1 import \
        load_f1_list as load_tourani2016impact_f1_list
from plotpascarellaf1 import \
        load_avrg_perf as load_avrg_pascarella_perf
from plotfan2019impactf1 import \
        load_f1_list as load_fan2019impact_f1_list
from plotduan2021impactf1 import \
        load_f1_list as load_duan2021impact_f1_list

def get_avrg_jian2013personalized_f1():
    perf_list,name_list = load_jiang2013personalized_perf_list()
    f1_list = [p['F1'].to_numpy() for p in perf_list]
    f1_avrg = np.average(f1_list, axis=0)

    dratios = perf_list[0]['dratio'].to_numpy()
    for perf in perf_list[1:]:
        assert(all(dratios == perf['dratio'].to_numpy()))

    return f1_avrg,dratios

def get_avrg_tourani2016impact_f1():
    perf_list,name_list = load_tourani2016impact_f1_list()
    f1_list = [p['f1'].to_numpy() for p in perf_list]
    f1_avrg = np.average(f1_list, axis=0)

    dratios = perf_list[0]['dratio'].to_numpy()
    for perf in perf_list[1:]:
        assert(all(dratios == perf['dratio'].to_numpy()))

    return f1_avrg,dratios


def get_avrg_pascarella_f1():
    f1_pascarella = load_avrg_pascarella_perf()
    return f1_pascarella['F-measure'].to_numpy(),f1_pascarella['dratio'].to_numpy()

def get_avrg_fan2019impact_f1():
    perf_list,name_list = load_fan2019impact_f1_list()
    f1_list = [p['f1'].to_numpy() for p in perf_list ]
    # f1_list = [p['f1'].to_numpy() for p,n in zip(perf_list,name_list) if n.endswith('RA') ]
    # print(name_list)
    # print(len(f1_list))
    f1_avrg = np.average(f1_list, axis=0)

    dratios = perf_list[0]['dratio'].to_numpy()
    for perf in perf_list[1:]:
        assert(all(dratios == perf['dratio'].to_numpy()))

    return f1_avrg,dratios

def get_avrg_duan2021impact_f1():
    perf_list,name_list = load_duan2021impact_f1_list()
    # print(type(perf_list[0]))
    # print(perf_list[0].columns)
    f1_list = [p['f1'].to_numpy() for p in perf_list ]
    f1_avrg = np.average(f1_list, axis=0)

    dratios = perf_list[0]['dratio'].to_numpy()
    for perf in perf_list[1:]:
        assert(all(dratios == perf['dratio'].to_numpy()))

    return f1_avrg,dratios

if __name__ == '__main__':
    fig_fn = None
    if len(sys.argv) == 2:
        fig_fn = sys.argv[1]

    f1_jian13,dr_jian13 = get_avrg_jian2013personalized_f1()
    f1_tourani16,dr_tourani16 = get_avrg_tourani2016impact_f1()
    f1_pascarella,dr_pascarella = get_avrg_pascarella_f1()
    f1_fan2019,dr_fan2019 = get_avrg_fan2019impact_f1()
    f1_duan2021,dr_duan2021 = get_avrg_duan2021impact_f1()

    figsize=(4*5/4, 2.5*5/4)
    marker_list = ['x', '^', 's', 'o', 'v']
    line_styles = ['dotted', 'dashed', 'dashdot', (0, (3, 1, 1, 1)), (0, (3, 5, 1, 5, 1, 5))]
    fig = plt.figure(figsize=figsize)
    for i,(x,y) in enumerate(zip([dr_jian13\
            , dr_tourani16\
            , dr_pascarella\
            , dr_fan2019\
            , dr_duan2021],[f1_jian13\
            , f1_tourani16\
            , f1_pascarella\
            , f1_fan2019\
            , f1_duan2021])):
        plt.plot(x, y, marker=marker_list[i], fillstyle='none'\
                , linestyle=line_styles[i], color='black')
    plt.legend(['Jiang13(PCC+)', 'Tourani16', 'Pascarella119', 'Fan19', 'Duan21'])
    plt.xlabel('Defect Ratio')
    plt.ylabel('F1')
    plt.tight_layout()

    if not fig_fn is None:
        plt.savefig(fig_fn)
    else:
        plt.show()
    
