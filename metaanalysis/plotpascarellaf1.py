from matplotlib import pyplot as plt
import pandas as pd
import sys

def read_ctx():
    ctx = pd.read_csv('pascarella2019fine_oss10_proj_context.csv', comment='#')
    dratio = ctx['DefectiveCommits'].divide(ctx['Commits'])
    return ctx,dratio

def read_perf_abc(csv_fn_list):
    df_list = []
    for csv_fn in csv_fn_list:
        perf = pd.read_csv(csv_fn, comment='#')
        df_list.append(perf)
    perf = None
    for p in df_list:
        if perf is None:
            perf = p.copy()
        else:
            assert(all(perf['Systems'] == p['Systems']))
            perf['F-measure'] = perf['F-measure'] + p['F-measure']
    perf['F-measure'] = perf['F-measure'].divide(300)
    return perf,df_list

def load_avrg_perf():
    csv_fn_list = ['pascarella2019fine_perf_a.csv',
            'pascarella2019fine_perf_b.csv',
            'pascarella2019fine_perf_c.csv']
    perf_avrg,_ = read_perf_abc(csv_fn_list)
    ctx,dratio = read_ctx()
    assert(all(ctx['Project'] == perf_avrg['Systems']))
    perf_avrg['dratio'] = dratio

    perf_avrg = perf_avrg.sort_values('dratio')
    return perf_avrg

def plot_f1(ctx, dratio, perf, fig_fn):
    print(ctx)
    print(perf)
    assert(all(ctx['Project'] == perf['Systems']))
    perf['dratio'] = dratio
    perf = perf.sort_values('dratio')
    plt.plot(perf['dratio'].to_list(), perf['F-measure'].to_list(), 
             marker='x', linestyle='dotted', color='black') 
    plt.xlabel('Defect Ratio')
    plt.ylabel('F1')
    plt.tight_layout()
    if not fig_fn is None:
        plt.savefig(fig_fn)
    plt.show()

def plot_3_f1(ctx, dratio, perf_list, fig_fn):
    fig = plt.figure( figsize=(4, 2.5))
    marker_list = ['x', '^', 'o']
    line_styles = ['dotted', 'dashed', 'dashdot']
    legend_list = ['all commits', 'partial defective', 'complete defective']

    print(ctx)
    for i,perf in enumerate(perf_list):
        print(perf)
        assert(all(ctx['Project'] == perf['Systems']))
        perf['dratio'] = dratio
        perf = perf.sort_values('dratio')
        plt.plot(perf['dratio'].to_list(), perf['F-measure'].divide(100).to_list(), 
                marker=marker_list[i], fillstyle='none',
                linestyle=line_styles[i], color='black')
    plt.xlabel('Defect Ratio')
    plt.ylabel('F1')
    plt.legend(legend_list)
    plt.tight_layout()
    if not fig_fn is None:
        plt.savefig(fig_fn)
    plt.show()

def plot_abc_f1(fig_fn):
    ctx,ratio = read_ctx()
    csv_fn_list = ['pascarella2019fine_perf_a.csv',
            'pascarella2019fine_perf_b.csv',
            'pascarella2019fine_perf_c.csv']
    perf,_ = read_perf_abc(csv_fn_list)
    plot_f1(ctx, ratio, perf, fig_fn)

def plot_abc_3lines_f1(fig_fn):
    ctx,ratio = read_ctx()
    csv_fn_list = ['pascarella2019fine_perf_a.csv',
            'pascarella2019fine_perf_b.csv',
            'pascarella2019fine_perf_c.csv']
    _,df_list = read_perf_abc(csv_fn_list)
    plot_3_f1(ctx, ratio, df_list, fig_fn)


def plot_dratio_vs_f1(csv_fn):
    ctx,dratio = read_ctx()
    perf = pd.read_csv(csv_fn, comment='#')
    perf['F-measure'] = perf['F-measure'].divide(100)
    print(perf)
    assert(all(ctx['Project'] == perf['Systems']))

    perf['dratio'] = dratio
    perf = perf.sort_values('dratio')
    plt.plot(perf['dratio'].to_list(), perf['F-measure'].to_list(), 
             marker='x', linestyle='dotted', color='black') 
    plt.xlabel('Defect Ratio')
    plt.ylabel('F1')
    plt.tight_layout()
    plt.show()

def main(argv):
    fig_fn = None
    if len(argv) == 2:
        fig_fn = argv[1]
    # plot_dratio_vs_f1('pascarella2019fine_perf_a.csv')
    # plot_dratio_vs_f1('pascarella2019fine_perf_b.csv')
    # plot_dratio_vs_f1('pascarella2019fine_perf_c.csv')
    # plot_abc_f1(fig_fn)
    plot_abc_3lines_f1(fig_fn)

if __name__=='__main__':
    main(sys.argv)


