import sys
from loaddata import load_rec20_data
from violinplot import plot_violin, sort_by_median

def main(argv):
    fig_fn='../doc/figures/defect_prone_rec20_comparison.pdf'
    show = True
    if len(argv) == 2:
        fig_fn = argv[1]
        show = False
    data,labels = load_rec20_data()
    highlighted = ['Kamei12(EALR):OS'
        , 'Yang15(Deeper)'
        , 'Yang16(LT,AGE)'
        , 'Yang17(TLEL)'
        , 'Huang17(CBS)'
        , 'Liu17(CCUM)'
        , 'Chen18(MULTI)'
        , 'Huang19(CBS+)'
        , 'Qiao19(FCNN)'
        , 'Li20(EATT)'
        , 'Yang20(DEJIT)'
        ]
    data,labels = sort_by_median(data,labels,highlighted)
    plot_violin(data, 
            labels=labels, 
            figsize=(7, 4),
            yname='Recall@20%', 
            xlabelrotation=45,
            highlighted=highlighted,
            fig_fn=fig_fn,
            show=show)

if __name__=='__main__':
    main(sys.argv)

