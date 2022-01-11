all: meta
	
	
meta: figures \
	figures/defect_prone_f1_comparison.pdf \
		figures/defect_prone_rec20_comparison.pdf \
		figures/defect_prone_popt_comparison.pdf \
		figures/dp_oss6_f1_vs_nchanges.pdf \
		figures/dp_oss6_f1_vs_dratio.pdf \
		figures/dp_oss6_f1_vs_locchange.pdf \
		figures/dp_oss6_f1_vs_ndevavrg.pdf \
		figures/dp_f1_vs_defect_others.pdf 


figures:
	mkdir figures

figures/defect_prone_f1_comparison.pdf: ../metaanalysis/plotf1.py
	python plotf1.py figures/defect_prone_f1_comparison.pdf

figures/defect_prone_rec20_comparison.pdf: ../metaanalysis/plotrec20.py
	python plotrec20.py figures/defect_prone_rec20_comparison.pdf

figures/defect_prone_popt_comparison.pdf: ../metaanalysis/plotpopt.py
	python plotpopt.py figures/defect_prone_popt_comparison.pdf

figures/dp_oss6_f1_vs_nchanges.pdf: ../metaanalysis/plotoss6f1.py
	python plotoss6f1.py f1_vs_nchanges figures/dp_oss6_f1_vs_nchanges.pdf	

figures/dp_oss6_f1_vs_dratio.pdf: ../metaanalysis/plotoss6f1.py
	python plotoss6f1.py f1_vs_dratio figures/dp_oss6_f1_vs_dratio.pdf	

figures/dp_oss6_f1_vs_locchange.pdf: ../metaanalysis/plotoss6f1.py
	python plotoss6f1.py f1_vs_locchange figures/dp_oss6_f1_vs_locchange.pdf

figures/dp_oss6_f1_vs_ndevavrg.pdf: ../metaanalysis/plotoss6f1.py
	python plotoss6f1.py f1_vs_ndevavrg figures/dp_oss6_f1_vs_ndevavrg.pdf

figures/dp_f1_vs_defect_others.pdf: ../metaanalysis/plotf1vsdr.py
	python plotf1vsdr.py figures/dp_f1_vs_defect_others.pdf

clean:
	$(RM) figures/*.pdf
