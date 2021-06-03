from matplotlib import pyplot as plt
import pandas as pd
import re
import sys

def parse_num(s):
    matches = re.match(r'[\d\.]+([KM]+)', s)
    if matches is None:
        return float(s)
    elif len(matches.group(1)) == 1 and matches.group(1) == 'K':
        return float(s[0:len(s)-1])*1000
    elif len(matches.group(1)) ==1 and matches.group(1) == 'M':
        return float(s[0:len(s)-1])*1000000
    else:
        print(len(matches.group(1)))
        print(matches.group(1))
        raise NotImplementedError('Cannot parse ' + s)

def parse_percent(s):
    matches = re.match(r'[\d\.]+(%)', s)
    if matches is None:
        return float(s)
    elif len(matches.group(1)) == 1 and matches.group(1) == '%':
        return float(s[0:len(s)-1])/100.
    else:
        print(len(matches.group(1)))
        print(matches.group(1))
        raise NotImplementedError('Cannot parse ' + s)
        

def load_perf_list():
    converters={'LOC': parse_num
            , 'NumofChanges': parse_num
            , 'PercentofBuggyChanges': parse_percent}
    ctx = pd.read_csv('jiang2013personalized_proj_context.csv', comment='#',
            converters=converters)
    df = pd.read_csv('jiang2013personalized_perf.csv', comment='#')

    legend_list = df['Method'].unique().tolist()

    perf_list = []
    for m in df['Method'].unique():
        perf = df[df['Method'] == m]
        perf = perf.reset_index(drop=True)
        perf['dratio'] = ctx['PercentofBuggyChanges']

        perf = perf.sort_values('dratio')
        perf_list.append(perf)

    return perf_list,legend_list

def main(argv):
    fig_fn = None
    if len(argv) == 2:
        fig_fn = argv[1]

    perf_list,legend_list = load_perf_list()

    marker_list = ['x', '^', 'v', 'o']
    line_styles = ['dotted', 'dashed', 'dashdot', (0, (3, 1, 1, 1))]
    fig = plt.figure( figsize=(4, 2.5))
    for i,perf in enumerate(perf_list):
        plt.plot(perf['dratio'].to_numpy(), perf['F1'].to_numpy(),
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

