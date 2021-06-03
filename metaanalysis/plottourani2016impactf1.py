from matplotlib import pyplot as plt
import pandas as pd
import sys

def load_f1_list():
    ctx = pd.read_csv('tourani2016impact_proj_context.csv', comment='#')
    perf = pd.read_csv('tourani2016impact_perf.csv', comment='#')
    num_projs = ctx.shape[0]
    assert(perf.shape[0] % num_projs == 0)
    perf_list = []
    for i in range(perf.shape[0]//num_projs):
        perf_list.append(perf.iloc[(i*num_projs):((i+1)*num_projs)])

    f1_list = []
    for i,perf in enumerate(perf_list):
        f1 = perf[['Project', 'f1']].reset_index(drop=True)
        # assert(all(f1['Project'].to_list() == dratio['Project'].to_list()))
        assert(all(f1['Project'] == ctx['Project']))
        f1['dratio'] = ctx['TotalNumOfCommits(%defective)'].div(100)
        f1_sorted = f1.sort_values('dratio')
        f1_list.append(f1_sorted)

    legend_list = ['issue metrics', 'review metrics', 'issue+review metrics']
    return f1_list,legend_list

def main(argv):
    fig_fn = None
    if len(argv) == 2:
        fig_fn = argv[1]

    f1_list,legend_list = load_f1_list()

    marker_list = ['x', '^', 'o']
    line_styles = ['dotted', 'dashed', 'dashdot']
    fig = plt.figure( figsize=(4, 2.5))
    for i,f1 in enumerate(f1_list):
        plt.plot(f1['dratio'].to_list(), f1['f1'],
                marker=marker_list[i], fillstyle='none',
                linestyle=line_styles[i], color='black')

    plt.legend(legend_list)
    plt.xlabel('Defect Ratio')
    plt.ylabel('F1')
    plt.tight_layout()
    if not fig_fn is None:
        plt.savefig(fig_fn)
    else:
        plt.show()


if __name__ == '__main__':
    main(sys.argv)

