# Metrics and Features for JIT-SDP

## Software Change Metrics  

| Category                        | Metric  | Description                                                                                             |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------- | 
| Diffusion                       | NS      | Number of modified subsystems                                                                           |
|                                 | ND      | Number of modified directories                                                                          |
|                                 | NF      | Number of modified files                                                                                |
|                                 | Entropy | Distribution of modified code across each file                                                          |
| Size                            | LA      | Lines of code added                                                                                     |
|                                 | LD      | Lines of code deleted                                                                                   |
|                                 | LT      | Lines of code in a file before the change                                                               |
| Purpose                         | FIX     | Whether or not the change is a defect fix                                                               |
| History                         | NDEV    | The number of developers that changed the modified files                                                |
|                                 | AGE     | The average time interval between the last and current change                                           |
|                                 | NUC     | The number of unique changes to the modified files                                                      |
| Experience                      | EXP     | Developer experience                                                                                    |
|                                 | REXP    | Recent developer experience                                                                             |
|                                 | SEXP    | Developer experience on a sub-system                                                                    |
| Size                            | Churn   | Size of the change, i.e., LA + LD                                                                       |
|                                 | RChurn  | Relative Churn, i.e., (LA + LD)/LT                                                                      |
|                                 | RLA     | Relative LA, i.e., LA / LT                                                                              |
|                                 | RLD     | Relative LD, i.e., LD / LT                                                                              |
|                                 | RLT     | Relative LT, i.e., LT / NF                                                                              |
| Change Complexity (Indentation) | AS      | Number of white spaces on all the “+” (added) lines in a commit                                         |
|                                 | AB      | Sum of the difference of left-braces and right-braces on all the “+” lines in each function in a commit |
| Change Context                  | NCW     | Number of words in context                                                                              |
|                                 | NCKW    | Number of programming language keywords                                                                 |
|                                 | NCCW    | number of words in the context and the changed lines                                                    |
|                                 | NCCKW   | Number of programming language keywords in the context and the changed lines                            |


## Software File Change Metrics

| Category       | Metric| Description                                                                                                |
| -------------- | ----- | ---------------------------------------------------------------------------------------------------------- | 
| Change Process | COMM  | Number of changes to the file up to the considered commit                                                  |
|                | ADEV  | Number developers who modified the file up to the considered commit                                        |
|                | DDEV  | Cumulative number of distinct developers contributed to the file up to the considered commit               |
|                | ADD   | Number of lines added to the file in the considered commit                                                 |
|                | DEL   | Number of lines removed from the file in the considered commit                                             |
|                | OWN   | Whether the commit is done by the owner of the file                                                        |
|                | MINOR | Number of contributors who contributed less than 5% of the file up to the considered commits               |
|                | SCTR  | Number of packages modified by the committer in the commit                                                 |
|                | NADEV | Number of developers who changed the files in the commits where the file has been modified                 |
|                | NDDEV | Cumulative number of distinct developers who changed the files in commits where the file has been modified |
|                | NCOMM | Number of commits made to files in commits where the file has been modified                                |
|                | NSCTR | Number of different packages touched by the developer in commits where the file has been modified          |
|                | OEXP  | Percentage of lines authored in the project                                                                |
|                | AEXP  | Mean of the experiences of all the developers who touched the file                                         |




## Issue Report and Code Review Metrics  

| Category       | Metric   | Description               |
| -------------- | -------- | ------------------------- | 
| Thread Focus   | COMMEXP  | Commenter experience      |
|                | RPTEXP   | Reporter experience       |
|                | RVWEXP   | Reviewer experience       |
|                | PATCHNUM | Number of patch revisions |
|                | NINLCMMT | Number of inline comments |
| Thread Length  | NUMCMMT  | Number of comments        |
|                | LENCMMT  | Length of comments        |
| Thread Time    | RVWTIME  | Review time               |
|                | FIXTIME  | Fix time                  |
|                | DISCLAG  | Average discussion lag    |
| Sentiment      | CMMTSENT | Comment sentiment         |





## Static Program Analysis Metrics 

| Category         | Metric | Description                                                              |
| ---------------- | ------ | ------------------------------------------------------------------------ | 
| Program Analysis | SysWD  | Warning density of the project                                           |
|                  | FSysWD | Cumulative difference between warning density of the file and the project|
|                  | AuDWD  | Cumulative sum of the changes in warning density by the author           |
























































