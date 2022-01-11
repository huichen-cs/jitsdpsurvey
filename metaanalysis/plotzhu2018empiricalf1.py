from matplotlib import pyplot as plt
import pandas as pd
import sys

def load_file_f1_list(data_fn, ctx_fn):
    df = pd.read_csv(data_fn, comment='#', index_col=False)
    df = df[df['Measure'] == 'fMeasure-1']
    ctx = pd.read_csv(ctx_fn, comment='#', index_col=False)

    alg_list=['Simple','ROS','RUS','Smote','Bag','ROSBag','RUSBag','SmoteBag','Boost','ROSBoost','RUSBoost','SmoteBoost']

    perf_list = []
    legend_list = alg_list
    for alg in alg_list:
        for i,alg in enumerate(alg_list):
            perf = df.reset_index(drop=True)

            f1 = pd.DataFrame()
            f1[['Project', 'f1']] = perf[['Project', alg]]
            f1['f1'] = f1['f1'].apply(float)/100.
            f1['dratio'] = 0
            for proj in ctx['Project']:
                ratio = ctx[ctx['Project'] == proj]['PercentBuggy'].tolist()[0]/100.
                f1.loc[f1['Project'] == proj, 'dratio'] = ratio
            # f1['dratio'] = ctx['PercentBuggy']/100.
            f1 = f1.sort_values('dratio')
            perf_list.append(f1)

    return perf_list,legend_list

def load_f1_list():
    data_csv_fn = 'zhu2018empricial_perf_all.csv'
    ctx_csv_fn = 'zhu2018empricial_proj_context.csv'
    p_list,n_list = \
            load_file_f1_list(data_csv_fn, ctx_csv_fn)

    return p_list,n_list

def plot_dratio_vs_f1(p_list, n_list):
    p_list,n_list= load_f1_list()
    for perf,n in zip(p_list,n_list):
        plt.plot(perf['dratio'].to_list(), perf['f1'].to_list(), 
             marker='x', linestyle='None', color='black') 
        plt.xlabel('Defect Ratio')
        plt.ylabel('F1')
        plt.legend(n)
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    fig_fn = None
    if len(sys.argv) == 2:
        fig_fn = sys.argv[1]

    p_list,n_list = load_f1_list()
    plot_dratio_vs_f1(p_list, n_list)
