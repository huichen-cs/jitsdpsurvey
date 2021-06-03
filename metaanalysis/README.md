# Synthesis and Meta-Analysis  
We adopt the approaches reported in in Hall et al. and Hosseini et al. and conduct a meta-analysis of the reported performance evaluation results in the studies ( https://github.com/huichen-cs/jitsdpsurvey/tree/main/papers).  
First, we examine the studies and determine that the predictive performance reported are somewhat comparable. Second, we assemble the predictive performance data and visualize the
data in violin plots. As indicated by Hosseini et al. , a violin plot is like a box plot that reports summary statistics such as minima, maxima, and median, but is also more informative than a box plot since the violin plot also show the distribution of the data.  

## Defect Proneness Prediction  
We compare the defect proneness prediction without considering QA effort. We select the studies(https://github.com/huichen-cs/jitsdpsurvey/tree/main/papers) that are of a batch learning setting and evaluate the models with a k-fold cross-validation where k is 10 for most of the studies as shown in following table. For these studies do not often include the decision threshold free evaluation criteria like AUC, we settle on collecting and reporting on the decision threshold dependent evaluation criteria. Since F1 score is a harmonic mean of precision and recall and is more difficult to manipulate than either precision or recall, we use the F1 score as an indicator of the predictive performance.  
Figure 3 is the violin plots of the reported F1 scores in the JIT-SDP studies. Among these violin plots, several are the studies that use the dataset of six open source projects shared by Kamei et al. . We highlight these violin plots by filling the plots with gray color.  

| Validation Strategy        | Remark                                                       | Research  | 
| -------------------------- | ------------------------------------------------------------ | --------- | 
| Cross validation           | 10-fold                                                      | Kim et al. [46], Kamei et al. [43],Fukushima et al. [23], Yang et al. [102], Tan et al. [91], Kamei et al. [41], Yang et al. [103], Tourani and Adams [94], Liu et al. [58], Yang et al. [101], Chen et al. [13], Zhang et al. [108],Huang et al. [38] Kang et al. [44], Khanan et al. [45], Li et al. [54], Zhu et al. [111]     | 
|                            | 5-fold                                                       | Hoang et al. [35], Hoang et al. [34]      | 
|                            | 2- to 10-fold                                                | Young et al. [104] ,Guo et al. [27]     | 
|                            | multi-fold                                                   | Zhao et al. [109]  |
|                            | leave-one-out                                                | Catolino et al. [10]       |
| Bootstrap validation       | out-of-sample                                                | Duan et al. [18], Fan et al. [19]       |
| Time-wise cross-validation | 10-fold                                                      | Yang et al. [103], Liu et al. [58], Chen et al. [13], Zhang et al. [108], Huang et al. [38] Li et al. [54] Fu and Menzies [22], Huang et al. [37]       |
|                            | time-aware validation, 11 groups, (same as Yang et al. [103] | 11 groups in Yan et al. [100]      |
|                            | time-sensitive analysis                                      | Pascarella et al. [72], Tan et al. [91], Trautsch et al. [95], Kondo et al. [50]     |
| Cross-project prediction   | 10-fold                                                      | Yang et al. [103], Liu et al. [58], Chen et al. [13] Huang et al. [38]      |
| SDLC                       | short-term/period                                            |       |
|                            | long-term/period                                             |       |


## Effort-Aware Defect Prediction  
Similar as before, we identify the studies that compute the effort-aware evaluation criteria in a comparable fashion. As the result, the studies we selected include k-fold cross validations. The evaluation criteria are 𝑃𝑜𝑝𝑡 and 𝑅𝑒𝑐𝑎𝑙𝑙@20%. Figure 4 are the violin plots of 𝑅𝑒𝑐𝑎𝑙𝑙@20% and 𝑃𝑜𝑝𝑡 of the selected studies. 



To generate figures for the analysis, run  
```shell
$ make
```
