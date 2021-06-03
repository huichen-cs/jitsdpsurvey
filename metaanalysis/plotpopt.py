import sys
from loaddata import load_popt_data
from violinplot import plot_violin, sort_by_median

def main(argv):
    fig_fn='../doc/figures/defect_prone_popt_comparison.pdf'
    show = True
    if len(argv) == 2:
        fig_fn = argv[1]
        show = False
    data,labels = load_popt_data()
    highlighted = ['Kamei12(EALR):OS'
        , 'Yang16(LT,AGE)'
        , 'Liu17(CCUM)'
        , 'Chen18(MULTI)'
        , 'Li20(EATT)']
    data,labels = sort_by_median(data,labels,highlighted)
    plot_violin(data, 
            labels=labels, 
            figsize=(7*6/12, 4),
            yname='$P_{opt}$',
            ylim=(0.,1.0),
            xlabelrotation=45,
            highlighted=highlighted,
            fig_fn=fig_fn,
            show=show)

if __name__=='__main__':
    main(sys.argv)

