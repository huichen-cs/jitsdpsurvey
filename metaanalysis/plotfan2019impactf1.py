from matplotlib import pyplot as plt
import pandas as pd
import sys

def read_data():
    ctx1 = pd.read_csv('fan2019impact_oss10_project_context.csv', comment='#')
    ctx2 = pd.read_csv('fan2019impact_oss10_project_context_b.csv', comment='#')
    df = pd.read_csv('fan2019impact_perf_f1.csv', comment='#')
    return ctx1,ctx2,df

def load_f1_list():
    ctx1,ctx2,df = read_data()

    szz_list = ['RA', 'MA', 'AG', 'B']
    szz_ratio_list = [ szz+'-SZZ-Ratio' for szz in szz_list ]
    cls_list = ['RF', 'NB', 'LR'] 

    perf_list = []
    legend_list = []
    for szz,szz_ratio in zip(szz_list, szz_ratio_list):
        legend_list.extend([c+szz for c in cls_list])
        for i,cls in enumerate(cls_list):
            perf = pd.DataFrame()
            perf[['Project', 'NChanges']] = ctx1[['Project', 'NChanges']]
            assert(all(ctx1['Project'] == ctx2['Project']))

            perf['dratio'] = ctx2['B-SZZ-Ratio'].div(100) 
            f1 = df[df['Cls'] == cls][['Project', szz]]
            f1 = f1.reset_index(drop=True)
            assert(all(perf['Project'] == f1['Project']))
            perf['f1'] = f1[szz]

            perf = perf.sort_values('dratio')
            perf_list.append(perf)
    return perf_list,legend_list



def plot_f1_each_szz(ctx1, ctx2, df):
    szz_list = ['RA', 'MA', 'AG', 'B']
    szz_ratio_list = [ szz+'-SZZ-Ratio' for szz in szz_list ]
    cls_list = ['RF', 'NB', 'LR'] 

    for szz,szz_ratio in zip(szz_list, szz_ratio_list):
        marker_list = ['x', '^', 's', 'o']
        line_styles = ['dotted', 'dashed', 'dashdot', (0, (3, 1, 1, 1))]
        fig = plt.figure( figsize=(4*1/2, 2.5*1/2))
        legend_list = cls_list
        for i,cls in enumerate(cls_list):
            perf = pd.DataFrame()
            perf[['Project', 'NChanges']] = ctx1[['Project', 'NChanges']]
            assert(all(ctx1['Project'] == ctx2['Project']))

            # perf['dratio'] = ctx2['RA-SZZ-Ratio'].div(100) 
            perf['dratio'] = ctx2['B-SZZ-Ratio'].div(100) 
            # f1 = df[df['Cls'] == cls][['Project', 'RA']]
            f1 = df[df['Cls'] == cls][['Project', szz]]
            f1 = f1.reset_index(drop=True)
            assert(all(perf['Project'] == f1['Project']))
            perf['f1'] = f1[szz]

            perf = perf.sort_values('dratio')
            print(perf)
            plt.plot(perf['dratio'].to_list(), perf['f1'].to_list(),
                    marker=marker_list[i], fillstyle='none',
                    linestyle=line_styles[i], color='black')
        plt.legend(legend_list)
        plt.xlabel('Defect Ratio (' + szz + '-SZZ)')
        plt.ylabel('F1')
        plt.show()

def plot_f1_szz(ctx1, ctx2, df, szz, fig_fn):
    szz_ratio = szz+'-SZZ-Ratio'
    cls_list = ['RF', 'NB', 'LR'] 

    marker_list = ['x', '^', 's', 'o']
    line_styles = ['dotted', 'dashed', 'dashdot', (0, (3, 1, 1, 1))]
    fig = plt.figure( figsize=(4, 2.5))
    legend_list = cls_list
    for i,cls in enumerate(cls_list):
        perf = pd.DataFrame()
        perf[['Project', 'NChanges']] = ctx1[['Project', 'NChanges']]
        assert(all(ctx1['Project'] == ctx2['Project']))

        # perf['dratio'] = ctx2['RA-SZZ-Ratio'].div(100) 
        perf['dratio'] = ctx2['B-SZZ-Ratio'].div(100) 
        # f1 = df[df['Cls'] == cls][['Project', 'RA']]
        f1 = df[df['Cls'] == cls][['Project', szz]]
        f1 = f1.reset_index(drop=True)
        assert(all(perf['Project'] == f1['Project']))
        perf['f1'] = f1[szz]

        perf = perf.sort_values('dratio')
        print(perf)
        plt.plot(perf['dratio'].to_list(), perf['f1'].to_list(),
                marker=marker_list[i], fillstyle='none',
                linestyle=line_styles[i], color='black')
    plt.legend(legend_list)
    plt.xlabel('Defect Ratio (' + szz + '-SZZ)')
    plt.ylabel('F1')
    plt.tight_layout()
    if not fig_fn is None:
        plt.savefig(fig_fn)
    else:
        plt.show()

def main(argv):
    fig_fn = None
    if len(argv) == 2:
        fig_fn = argv[1]
    ctx1,ctx2,df = read_data()
    # plot_f1_each_szz(ctx1, ctx2, df)
    plot_f1_szz(ctx1, ctx2, df, 'RA', fig_fn)

if __name__=='__main__':
    main(sys.argv)

