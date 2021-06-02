# Metrics and Features for JIT-SDP

## Software Change Metrics  

| Category                        | Metric  | Description                                                                                             |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------- | 
| Diffusion                       | NS      | Number of modified subsystems                                                                           |
                                  | ND      | Number of modified directories                                                                          |
                                  | NF      | Number of modified files                                                                                |
                                  | Entropy | Distribution of modified code across each file                                                          |
| Size                            | LA      | Lines of code added                                                                                     |
                                  | LD      | Lines of code deleted                                                                                   |
                                  | LT      | Lines of code in a file before the change                                                               |
| Purpose                         | FIX     | Whether or not the change is a defect fix                                                               |
| History                         | NDEV    | The number of developers that changed the modified files                                                |
                                  | AGE     | The average time interval between the last and current change                                           |
                                  | NUC     | The number of unique changes to the modified files                                                      |
| Experience                      | EXP     | Developer experience                                                                                    |
                                  | REXP    | Recent developer experience                                                                             |
                                  | SEXP    | Developer experience on a sub-system                                                                    |
| Size                            | Churn   | Size of the change, i.e., LA + LD                                                                       |
                                  | RChurn  | Relative Churn, i.e., (LA + LD)/LT                                                                      |
                                  | RLA     | Relative LA, i.e., LA / LT                                                                              |
                                  | RLD     | Relative LD, i.e., LD / LT                                                                              |
                                  | RLT     | Relative LT, i.e., LT / NF                                                                              |
| Change Complexity (Indentation) | AS      | Number of white spaces on all the “+” (added) lines in a commit                                         |
                                  | AB      | Sum of the difference of left-braces and right-braces on all the “+” lines in each function in a commit |
| Change Context                  | NCW     | Number of words in context                                                                              |
                                  | NCKW    | Number of programming language keywords                                                                 |
                                  | NCCW    | number of words in the context and the changed lines                                                    |
                                  | NCCKW   | Number of programming language keywords in the context and the changed lines                            |




