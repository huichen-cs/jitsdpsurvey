import sys
from matplotlib import pyplot as plt

from loaddata import load_proj_f1_data, load_kamei2012large_oss6_context
from violinplot import plot_violin_ax

def plot_context(ax, ctx, ctx_factor, factor):
    ax2 = ax.twinx() 
    ax2.set_ylabel(factor, color='black')
    ax2.plot(range(1,7), ctx[ctx_factor].to_list(), 
            marker='x', markeredgecolor='black', markerfacecolor='black',
            linestyle='dashed', color='gray')
    ax2.tick_params(axis='y', labelcolor='black')
    ax2.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    ax2.legend([factor])


def plot_f1_vs_nchanges(**kwargs):
    show = True
    fig_fn = '../doc/figures/defect_prone_proj_f1_vs_nchanges_comparison.pdf'
    if 'fig_fn' in kwargs:
        fig_fn = kwargs['fig_fn']
        show = False
    ctx = load_kamei2012large_oss6_context()
    ctx = ctx.sort_values('Changes', axis='index')
    labels = ctx['Project'].to_list()
    ddict = load_proj_f1_data()
    # print(ctx['Changes'])
    data = [ddict[k] for k in labels]
    ax = plot_violin_ax(data, 
            labels=labels, 
            figsize=(4*5/4, 2.5*5/4),
            yname='F1', 
            ylim=(0.0,1.0),
            xlabelrotation=45,
            highlighted='all',
            show=show)

    plot_context(ax, ctx, 'Changes', '# of Changes')
    plt.tight_layout()
    plt.savefig(fig_fn)
    if show:
        plt.show()


def plot_f1_vs_defect_ratio(**kwargs):
    show = True
    fig_fn = '../doc/figures/defect_prone_proj_f1_vs_dratio_comparison.pdf',
    if 'fig_fn' in kwargs:
        fig_fn = kwargs['fig_fn']
        show = False
    ctx = load_kamei2012large_oss6_context()
    ctx = ctx.sort_values('DefectRatio', axis='index')
    labels = ctx['Project'].to_list()
    ddict = load_proj_f1_data()
    # print(ctx['DefectRatio'])
    data = [ddict[k] for k in labels]
    ax = plot_violin_ax(data, 
            labels=labels, 
            figsize=(4*5/4, 2.5*5/4),
            yname='F1', 
            ylim=(0.0,1.0),
            xlabelrotation=45,
            highlighted='all',
            show=show)

    plot_context(ax, ctx, 'DefectRatio', 'Defect Ratio')
    plt.tight_layout()
    plt.savefig(fig_fn)
    if show:
        plt.show()

def plot_f1_vs_loc_file():
    ctx = load_kamei2012large_oss6_context()
    ctx = ctx.sort_values('LOCFile', axis='index')
    labels = ctx['Project'].to_list()
    ddict = load_proj_f1_data()
    # print(ctx['LOCFile'])
    data = [ddict[k] for k in labels]
    plot_violin(data, 
            labels=labels, 
            figsize=(4*5/4, 2.5*5/4),
            yname='F1', 
            ylim=(0.0,1.0),
            xlabelrotation=45,
            highlighted='all',
            fig_fn='../doc/figures/defect_prone_proj_f1_vs_locfile_comparison.pdf',
            show=True)

def plot_f1_vs_loc_change(**kwargs):
    show = True
    fig_fn = '../doc/figures/defect_prone_proj_f1_vs_locchange_comparison.pdf',
    if 'fig_fn' in kwargs:
        fig_fn = kwargs['fig_fn']
        show = False
    ctx = load_kamei2012large_oss6_context()
    ctx = ctx.sort_values('LOCChange', axis='index')
    labels = ctx['Project'].to_list()
    ddict = load_proj_f1_data()
    # print(ctx['LOCChange'])
    data = [ddict[k] for k in labels]
    ax = plot_violin_ax(data, 
            labels=labels, 
            figsize=(4*5/4, 2.5*5/4),
            yname='F1', 
            ylim=(0.0,1.0),
            xlabelrotation=45,
            highlighted='all',
            show=show)

    plot_context(ax, ctx, 'LOCChange', 'Change Size')
    plt.tight_layout()
    plt.savefig(fig_fn)
    if show:
        plt.show()


def plot_f1_vs_ndevs_per_file_avrg(**kwargs):
    show = True
    fig_fn='../doc/figures/defect_prone_proj_f1_vs_ndevavrg_comparison.pdf',
    if 'fig_fn' in kwargs:
        fig_fn = kwargs['fig_fn']
        show = False
    ctx = load_kamei2012large_oss6_context()
    ctx = ctx.sort_values('NDevPerFileAvrg', axis='index')
    labels = ctx['Project'].to_list()
    ddict = load_proj_f1_data()
    # print(ctx['NDevPerFileAvrg'])
    data = [ddict[k] for k in labels]
    ax = plot_violin_ax(data, 
            labels=labels, 
            figsize=(4*5/4, 2.5*5/4),
            yname='F1', 
            ylim=(0.0,1.0),
            xlabelrotation=45,
            highlighted='all',
            show=show)

    plot_context(ax, ctx, 'NDevPerFileAvrg', '# of Developers/File')
    plt.tight_layout()
    plt.savefig(fig_fn)
    if show:
        plt.show()

def plot_f1_vs_ndevs_per_file_max():
    ctx = load_kamei2012large_oss6_context()
    ctx = ctx.sort_values('NDevPerFileMax', axis='index')
    labels = ctx['Project'].to_list()
    ddict = load_proj_f1_data()
    # print(ctx['NDevPerFileMax'])
    data = [ddict[k] for k in labels]
    plot_violin(data, 
            labels=labels, 
            figsize=(4*5/4, 2.5*5/4),
            yname='F1', 
            ylim=(0.0,1.0),
            xlabelrotation=45,
            highlighted='all',
            fig_fn='../doc/figures/defect_prone_proj_f1_vs_ndevmax_comparison.pdf',
            show=True)

def main(argv):
    # print(len(argv))
    # print(argv)
    if len(argv) == 1: 
        plot_f1_vs_nchanges()
        plot_f1_vs_defect_ratio()
        plot_f1_vs_loc_file()
        plot_f1_vs_loc_change()
        plot_f1_vs_ndevs_per_file_avrg()
        plot_f1_vs_ndevs_per_file_max()
    elif len(argv) == 3:
        if argv[1] == 'f1_vs_nchanges':
            fig_fn = argv[2]
            plot_f1_vs_nchanges(fig_fn=fig_fn)
        elif argv[1] == 'f1_vs_dratio':
            fig_fn = argv[2]
            plot_f1_vs_defect_ratio(fig_fn=fig_fn)
        elif argv[1] == 'f1_vs_locchange':
            fig_fn = argv[2]
            plot_f1_vs_loc_change(fig_fn=fig_fn)
        elif argv[1] == 'f1_vs_ndevavrg':
            fig_fn = argv[2]
            plot_f1_vs_ndevs_per_file_avrg(fig_fn=fig_fn)
        else:
            raise NotImplemented('Figure type ' + argv[1] + ' not implemented')
    else:
        print('Usage: ' + argv[0] + ' figure_type figure_filename') 
        sys.exit(1)
#    plot_f1_vs_ndevs_per_file_avrg()
#    plot_f1_vs_ndevs_per_file_max()

if __name__=='__main__':
    main(sys.argv)

