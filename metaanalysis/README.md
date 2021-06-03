# Synthesis and Meta-Analysis  
To generate figures for the analysis, run  
```shell
$ make
```



We adopt the approaches reported in in Hall et al.[1] and Hosseini et al.[2] and conduct a meta-analysis of the reported performance evaluation results in the studies ( https://github.com/huichen-cs/jitsdpsurvey/tree/main/papers).  
First, we examine the studies and determine that the predictive performance reported are somewhat comparable. Second, we assemble the predictive performance data and visualize the data in violin plots. As indicated by Hosseini et al.[2] , a violin plot is like a box plot that reports summary statistics such as minima, maxima, and median, but is also more informative than a box plot since the violin plot also show the distribution of the data.  

## Defect Proneness Prediction  
We compare the defect proneness prediction without considering QA effort. We select the studies(https://github.com/huichen-cs/jitsdpsurvey/tree/main/papers) that are of a batch learning setting and evaluate the models with a k-fold cross-validation where k is 10 for most of the studies as shown in table1. For these studies do not often include the decision threshold free evaluation criteria like AUC, we settle on collecting and reporting on the decision threshold dependent evaluation criteria. Since F1 score is a harmonic mean of precision and recall and is more difficult to manipulate than either precision or recall, we use the F1 score as an indicator of the predictive performance.  
Figure 3 is the violin plots of the reported F1 scores in the JIT-SDP studies. Among these violin plots, several are the studies that use the dataset of six open source projects shared by Kamei et al.[paper No.39] . We highlight these violin plots by filling the plots with gray color.  

Table 1: Summary of Evaluation Strategies in JIT-SDP Researches (paper citing number matches the number in the table of papers that we studied in our survey: https://github.com/huichen-cs/jitsdpsurvey/tree/main/papers)  

| Validation Strategy        | Remark                                                       | Research  | 
| -------------------------- | ------------------------------------------------------------ | --------- | 
| Cross validation           | 10-fold                                                      | Kim et al. [40], Kamei et al. [39],Fukushima et al. [36], Yang et al. [35], Tan et al. [34], Kamei et al. [29], Yang et al. [32], Tourani and Adams [30], Liu et al. [26], Yang et al. [28], Chen et al. [23], Zhang et al. [20],Huang et al. [18] Kang et al. [4], Khanan et al. [11], Li et al. [12], Zhu et al. [9]     | 
|                            | 5-fold                                                       | Hoang et al. [3], Hoang et al. [16]      | 
|                            | 2- to 10-fold                                                | Young et al. [22] ,Guo et al. [21]     | 
|                            | multi-fold                                                   | Zhao et al. [2]  |
|                            | leave-one-out                                                | Catolino et al. [13]       |
| Bootstrap validation       | out-of-sample                                                | Duan et al. [1], Fan et al. [15]       |
| Time-wise cross-validation | 10-fold                                                      | Yang et al. [32], Liu et al. [26], Chen et al. [23], Zhang et al. [20], Huang et al. [18] Li et al. [12] Fu and Menzies [24], Huang et al. [25]       |
|                            | time-aware validation, 11 groups, (same as Yang et al. [103] | 11 groups in Yan et al. [10]      |
|                            | time-sensitive analysis                                      | Pascarella et al. [17], Tan et al. [34], Trautsch et al. [7], Kondo et al. [14]     |
| Cross-project prediction   | 10-fold                                                      | Yang et al. [32], Liu et al. [26], Chen et al. [23] Huang et al. [18]      |
| SDLC                       | short-term/period                                            |       |
|                            | long-term/period                                             |       |




## Effort-Aware Defect Prediction  
Similar as before, we identify the studies that compute the effort-aware evaluation criteria in a comparable fashion. As the result, the studies we selected include k-fold cross validations. The evaluation criteria are 𝑃𝑜𝑝𝑡 and 𝑅𝑒𝑐𝑎𝑙𝑙@20%. Figure 4 are the violin plots of 𝑅𝑒𝑐𝑎𝑙𝑙@20% and 𝑃𝑜𝑝𝑡 of the selected studies. 


[1] Tracy Hall, Sarah Beecham, David Bowes, David Gray, and Steve Counsell. 2011. A systematic literature review on fault prediction performance in software engineering. IEEE Transactions on Software Engineering 38, 6 (2011), 1276–1304.   
[2] Seyedrebvar Hosseini, Burak Turhan, and Dimuthu Gunarathna. 2017. A systematic literature review and metaanalysis on cross project defect prediction. IEEE Transactions on Software Engineering 45, 2 (2017), 111–147.  






