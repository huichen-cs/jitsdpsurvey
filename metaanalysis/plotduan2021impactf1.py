from matplotlib import pyplot as plt
import pandas as pd
import sys

def load_file_f1_list(fn, ctx):
    df = pd.read_csv(fn, comment='#')

    alg_list = ['RF', 'LR', 'NB']
    bal_list = ['OS', 'Smote', 'US']

    perf_list = []
    legend_list = []
    for bal in bal_list:
        legend_list.extend([bal+alg for alg in alg_list])

        for i,alg in enumerate(alg_list):
            perf = df[df['Classifier'] == alg].reset_index(drop=True)
            f1_column = 'f1(' + bal + ')'
            assert(all(ctx['Project'] == perf['Project']))

            f1 = pd.DataFrame()
            f1[['Project', 'f1']] = perf[['Project', f1_column]]
            f1['dratio'] = ctx['BugIntroducingChanges'].div(ctx['NumChanges'])
            f1 = f1.sort_values('dratio')
            perf_list.append(f1)

    return perf_list,legend_list

def load_f1_list():
    ctx = pd.read_csv('duan2021impact_proj_context.csv', comment='#')
    p1_list,n1_list = \
            load_file_f1_list('duan2021impact_perf_undup.csv', ctx)
    p2_list,n2_list = \
            load_file_f1_list('duan2021impact_perf_indup.csv', ctx)

    assert(n1_list == n2_list)

    return p1_list+p2_list,n1_list


if __name__ == '__main__':
    fig_fn = None
    if len(sys.argv) == 2:
        fig_fn = sys.argv[1]

    ctx = pd.read_csv('duan2021impact_proj_context.csv', comment='#')
# df = pd.read_csv('duan2021impact_perf_indup.csv', comment='#')
    df = pd.read_csv('duan2021impact_perf_undup.csv', comment='#')

    alg_list = ['RF', 'LR', 'NB']
# bal_list = ['OS', 'Smote', 'US']
    bal_list = ['Smote']
# for alg in alg_list:
#     fig = plt.figure( figsize=(4*1/2, 2.5*1/2))
# 
#     perf = df[df['Classifier'] == alg].reset_index(drop=True)
#     for bal in bal_list:
#         f1_column = 'f1(' + bal + ')'
#         assert(all(ctx['Project'] == perf['Project']))
# 
#         f1 = pd.DataFrame()
#         f1[['Project', f1_column]] = perf[['Project', f1_column]]
#         f1['dratio'] = ctx['BugIntroducingChanges'].div(ctx['NumChanges'])
#         f1 = f1.sort_values('dratio')
#         plt.plot(f1['dratio'], f1[f1_column])
#     plt.show()

    for bal in bal_list:
        fig = plt.figure( figsize=(4, 2.5))
        marker_list = ['x', '^', 's', 'o']
        line_styles = ['dotted', 'dashed', 'dashdot', (0, (3, 1, 1, 1))]
        legend_list = alg_list

        for i,alg in enumerate(alg_list):
            perf = df[df['Classifier'] == alg].reset_index(drop=True)
            f1_column = 'f1(' + bal + ')'
            assert(all(ctx['Project'] == perf['Project']))

            f1 = pd.DataFrame()
            f1[['Project', f1_column]] = perf[['Project', f1_column]]
            f1['dratio'] = ctx['BugIntroducingChanges'].div(ctx['NumChanges'])
            f1 = f1.sort_values('dratio')
            plt.plot(f1['dratio'].to_list(), f1[f1_column].to_list(),
                    marker=marker_list[i], fillstyle='none',
                    linestyle=line_styles[i], color='black')
        plt.legend(legend_list)
        plt.xlabel('Defect Ratio (SMOTE+Unsup)')
        plt.ylabel('F1')
        plt.tight_layout()

        if not fig_fn is None:
            plt.savefig(fig_fn)
        else:
            plt.show()
