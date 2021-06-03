import pandas as pd
import re

oss6_proj_list = [
        'Bugzilla',
        'Columba',
        'JDT',
        'Mozilla',
        'Platform',
        'PostgreSQL'
        ]

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

# Duan et al.~\cite{duan2021impact}
def load_duan2021impact_f1():
    f1_list = []

    csv_fn_list = ['duan2021impact_perf_indup.csv',
        'duan2021impact_perf_undup.csv']
    for csv_fn in csv_fn_list:
        df = pd.read_csv(csv_fn, comment='#')
        for c in ['f1(OS)', 'f1(Smote)', 'f1(US)']:
            f1_list.append(df[c])

    return pd.concat(f1_list).to_list(),'Duan21'

def load_duan2021impact_f1_by_alg():
    alg_set = set()
    df_list = []
    csv_fn_list = ['duan2021impact_perf_indup.csv',
        'duan2021impact_perf_undup.csv']

    for csv_fn in csv_fn_list:
        df = pd.read_csv(csv_fn, comment='#')
        alg_set = alg_set.union(df['Classifier'].unique().tolist())
        df_list.append(df)

    f1_dict = dict()
    for alg in alg_set:
        f1_list = []
        for df in df_list:
            df_alg = df[df['Classifier'] == alg]
            for c in ['f1(OS)', 'f1(Smote)', 'f1(US)']:
                f1_list.append(df_alg[c])
        f1_dict[alg] = pd.concat(f1_list).to_list()

    return alg_set,f1_dict
    




# kang2020predicting (maritime)
def load_kang2020predicting_f1():
    f1_list = []

    df = pd.read_csv('kang2020predicting_perf_ab.csv', comment='#')
    for c in ['N0(F)', 'N1(F)', 'N2(F)', 'S5(F)']:
        f1_list.append(df[c])

    return pd.concat(f1_list).to_list(), 'Kang20(Maritime)'

# yan2020effort (alibaba study)
def load_yan2020effort_rec20():
    rec20_list = []

    df = pd.read_csv('yan2020effort_perf_sup_a.csv', comment='#')
    for c in ['R(OneWay)','R(EALR)','R(CBS+)']:
        rec20_list.append(df[c])

    return pd.concat(rec20_list).to_list(), 'Yan20(Alibaba)'

def load_yan2020effort_rec20_by_alg():
    alg_set = set()

    alg_list = ['OneWay','EALR','CBS+']
    alg_set = alg_set.union(alg_list)
    col_list = ['R(OneWay)','R(EALR)','R(CBS+)']
    rec20_dict = dict()
    rec20_list = []

    df = pd.read_csv('yan2020effort_perf_sup_a.csv', comment='#')
    for alg,col in zip(alg_list, col_list):
        rec20_dict[alg] = df[col].to_list()

    alg_list = ['LT','Churn','CBS+']
    alg_set = alg_set.union(alg_list)
    col_list = ['R(LT)','R(Churn)','R(CBS+)']

    df = pd.read_csv('yan2020effort_perf_unsup_a.csv', comment='#')
    for alg,col in zip(alg_list, col_list):
        if alg in rec20_dict:
            rec20_dict[alg].extend(df[col].to_list())
        else:
            rec20_dict[alg] = df[col].to_list()

    return alg_set,rec20_dict

# li2020effort - EATT
def load_li2020effort_f1():
    f1_list = []

    df = pd.read_csv('li2020effort_perf_f1.csv', comment='#')
    f1_list.append(df['EATT1'])
    f1_list.append(df['EATT2'])

    return pd.concat(f1_list).to_list(), 'Li20(EATT)'

def load_li2020effort_proj_f1():
    df = pd.read_csv('li2020effort_perf_f1.csv', comment='#')

    d = dict()
    for p in oss6_proj_list:
        d[p] = df[df['PROJECT'] == p[0:3].upper()][['EATT1', 'EATT2']].iloc[0].to_list()

    assert(len(d) == len(oss6_proj_list))
    return d

def load_li2020effort_acc20():
    acc20_list = []

    df = pd.read_csv('li2020effort_perf_acc20.csv', comment='#')
    acc20_list.append(df['EATT1'])
    acc20_list.append(df['EATT2'])

    return pd.concat(acc20_list).to_list(), 'Li20(EATT)'

def load_li2020effort_popt():
    popt_list = []

    df = pd.read_csv('li2020effort_perf_popt.csv', comment='#')
    popt_list.append(df['EATT1'])
    popt_list.append(df['EATT2'])

    return pd.concat(popt_list).to_list(), 'Li20(EATT)'
    

def load_zhu2020within_lr_f1():
    f1_list = []

    df = pd.read_csv('zhu2020within_perf_f1.csv', comment='#')
    for c in ['LR']:
        f1_list.append(df[c])

    return pd.concat(f1_list).to_list(),'Zhu20-BL'

def load_zhu2020within_f1():
    f1_list = []

    df = pd.read_csv('zhu2020within_perf_f1.csv', comment='#')
    for c in ['DAECNNJDP(0.25)', 'DAECNNJDP(0.5)', 'DAECNNJDP(0.75)', 'DAECNNJDP(1)']:
        f1_list.append(df[c])

    return pd.concat(f1_list).to_list(),'Zhu20'

# Fan et al.~\cite{fan2019impact}
def load_fan2019impact_f1():
    f1_list = []

    df = pd.read_csv('fan2019impact_perf_f1.csv', comment='#')
    for c in ['B', 'AG', 'MA', 'RA']:
        f1_list.append(df[c])

    return pd.concat(f1_list).to_list(),'Fan19'

def load_fan2019impact_f1_by_alg():
    df = pd.read_csv('fan2019impact_perf_f1.csv', comment='#')
    alg_set = set(df['Cls'].unique().tolist())

    f1_dict = dict()
    for alg in alg_set:
        df_alg = df[df['Cls'] == alg]
        f1_list = []
        for c in ['B', 'AG', 'MA', 'RA']:
            f1_list.append(df_alg[c])
        f1_dict[alg] = pd.concat(f1_list).to_list()

    return alg_set,f1_dict

def load_fan2019impact_rec20():
    df = pd.read_csv('fan2019impact_perf_rec20.csv', comment='#',
            converters={'rB':parse_percent,
                'rAG':parse_percent,
                'rMA':parse_percent})
    
    rec20_list = []
    for c in ['B', 'AG', 'MA', 'RA']:
        rec20_list.append(df[c])
    rec20 = pd.concat(rec20_list).to_list() 

    return rec20,'Fan19'

def load_fan2019impact_rec20_by_alg():
    df = pd.read_csv('fan2019impact_perf_rec20.csv', comment='#',
            converters={'rB':parse_percent,
                'rAG':parse_percent,
                'rMA':parse_percent})
    
    rec20_dict = dict()
    alg_set = set(df['Tech.'].unique().tolist())
    for alg in alg_set:
        df_alg = df[df['Tech.'] == alg]
        rec20_list = []
        for c in ['B', 'AG', 'MA', 'RA']:
            rec20_list.append(df_alg[c])
        rec20_dict[alg] = pd.concat(rec20_list).to_list() 

    return alg_set,rec20_dict



# pascarella2019fine
def load_pascarella2019fine_f1():
    f1_list = []

    df = pd.read_csv('pascarella2019fine_perf_a.csv', comment='#')
    f1_list.append(df['F-measure'])

    df = pd.read_csv('pascarella2019fine_perf_b.csv', comment='#')
    f1_list.append(df['F-measure'])

    df = pd.read_csv('pascarella2019fine_perf_c.csv', comment='#')
    f1_list.append(df['F-measure'])

    return pd.concat(f1_list).divide(100.).to_list(),'Pascarella19'

# huang2019revisiting
def load_huang2019revisiting_rec20():
    rec20_list = []

    df = pd.read_csv('huang2019revisiting_perf.csv', comment='#')
    rec20_list.append(df['R(CBS+)'])

    df = pd.read_csv('huang2019revisiting_perf_b.csv', comment='#')
    rec20_list.append(df['R(CBS+)'])

    df = pd.read_csv('huang2019revisiting_perf_c.csv', comment='#')
    rec20_list.append(df['R(CBS+)'])

    df = pd.read_csv('huang2019revisiting_perf_d.csv', comment='#')
    rec20_list.append(df['R(CBS+)'])

    return pd.concat(rec20_list).to_list(), 'Huang19(CBS+)'

def load_young2018replication_f1():
    df = pd.read_csv('young2018replication_perf_f1.csv', comment='#')
    return df['DSL'].to_list(), 'Young18(DSL)'

# young2018replication
def load_young2018replication_proj_f1():
    df = pd.read_csv('young2018replication_perf_f1.csv', comment='#')

    d = dict()
    for p in oss6_proj_list:
        d[p] = df[df['Project'].str.lower() == p.lower()]['DSL'].to_list()

    return d


# chen2018multi
def load_chen2018multi_popt():
    df = pd.read_csv('chen2018multi_perf_popt.csv', comment='#')
    return df['MULTI-M'].to_list(), 'Chen18(MULTI)'

def load_chen2018multi_acc20():
    df = pd.read_csv('chen2018multi_perf_acc20.csv', comment='#')
    return df['MULTI-M'].to_list(), 'Chen18(MULTI)'

# liu2017code
def load_liu2017code_popt():
    popt_list = []

    df = pd.read_csv('liu2017code_perf_popt.csv', comment='#')
    popt_list.append(df['CCUM'])

    df = pd.read_csv('liu2017code_perf_poptb.csv', comment='#')
    popt_list.append(df['CCUM'])

    return pd.concat(popt_list).to_list(), 'Liu17(CCUM)'

def load_liu2017code_rec20():
    rec20_list = []

    df = pd.read_csv('liu2017code_perf_acc20.csv', comment='#')
    rec20_list.append(df['CCUM'])

    df = pd.read_csv('liu2017code_perf_acc20b.csv', comment='#')
    rec20_list.append(df['CCUM'])

    df = pd.read_csv('liu2017code_perf_pprf1.csv', comment='#')
    rec20_list.append(df['CCUM(PofB20)'].divide(100.))

    return pd.concat(rec20_list).to_list(), 'Liu17(CCUM)'

def load_liu2017code_f1():
    df = pd.read_csv('liu2017code_perf_pprf1.csv', comment='#')
    return df['CCUM(F1)'].to_list(), 'Liu17(CCUM)'

# huang2017supervised
def load_huang2017supervised_rec20():
    df = pd.read_csv('huang2017supervised_perf.csv', comment='#')
    return df['R(CBS)'].to_list(), 'Huang17(CBS)'

# tourani2016impact
def load_tourani2016impact_f1():
    df = pd.read_csv('tourani2016impact_perf.csv', comment='#')
    return df['f1'].to_list(), 'Tourani16'

# yang2017tlel (xinli yang)
def load_yang2017tlel_pofb20():
    df = pd.read_csv('yang2017tlel_perf_pofb20.csv', comment='#')
    return df['PofB20(TLEL)'].divide(100.).to_list(), 'Yang17(TLEL)'

def load_yang2017tlel_f1():
    df = pd.read_csv('yang2017tlel_perf_f1.csv', comment='#')
    return df['f1(TLEL)'].to_list(), 'Yang17(TLEL)'

def load_yang2017tlel_proj_f1():
    df = pd.read_csv('yang2017tlel_perf_f1.csv', comment='#')

    d = dict()
    for p in oss6_proj_list:
        d[p] = df[df['Project'] == p]['f1(TLEL)'].to_list()
    assert(len(d) == len(oss6_proj_list))

    return d

# yang2016effort (xinli yang)
def load_yang2016effort_rec20():
    rec20_list = []

    df = pd.read_csv('yang2016effort_perf_rec20.csv', comment='#')
    for c in ['NF','Entropy','LT','AGE']:
        rec20_list.append(df[c])

    return pd.concat(rec20_list).to_list(), 'Yang16(LT,AGE)'

def load_yang2016effort_popt():
    popt_list = []

    df = pd.read_csv('yang2016effort_perf_popt.csv', comment='#')
    for c in ['NF','NUC','LT','AGE']:
        popt_list.append(df[c])

    return pd.concat(popt_list).to_list(), 'Yang16(LT,AGE)'

# kamei2016studying
def load_kamei2016studying_oss6_proj_f1():
    df = pd.read_csv('kamei2016studying_f1.csv', comment='#')

    d = dict()
    for p in df.columns[1:]:
        d[p.lower()] = df[['Project', p]][df['Project'] == p][p].to_list()

    f1 = dict()
    for p in oss6_proj_list:
        f1[p] = d[p.lower()[0:3]]

    assert(len(f1) == len(oss6_proj_list))
    return f1 

# baseline for yang2015deep -- this isn't really Kamei et al.'s proposal
def load_yang2015deep_lr_f1():
    df = pd.read_csv('yang2015deep_perf_f1.csv', comment='#')
    return df['Kamei_et_al.’s'].to_list(), 'Yang15-BL'


def load_yang2015deep_f1():
    df = pd.read_csv('yang2015deep_perf_f1.csv', comment='#')
    return df['Deeper'].to_list(), 'Yang15(Deeper)'

def load_yang2015deep_proj_f1():
    df = pd.read_csv('yang2015deep_perf_f1.csv', comment='#')
    f1 = df[['Project', 'Deeper']]

    f1_dict = dict()
    for p in oss6_proj_list:
        f1_dict[p] = []

    for p in oss6_proj_list:
        f1_dict[p].extend(f1[f1['Project'].str.lower() == p.lower()]['Deeper'].to_list())
    return f1_dict


def load_yang2015deep_pofb20():
    df = pd.read_csv('yang2015deep_perf_pofb20.csv', comment='#')
    return df['Deeper(%)'].divide(100.).to_list(), 'Yang15(Deeper)'

def load_jiang2013personalized_f1():
    df = pd.read_csv('jiang2013personalized_perf.csv', comment='#')
    return df['F1'].to_list(), 'Jiang13(PCC+)'

def load_jiang2013personalized_pofb20():
    df = pd.read_csv('jiang2013personalized_perf.csv', comment='#')
    return df['PofB20'].to_list(), 'Jiang13(PCC+)'

# kamei et al.~\cite{kamei2012large}
def load_kamei2012large_oss6_context():
    df = pd.read_csv('../metaanalysis/kamei2012large_oss6_proj_context.csv', comment='#')
    df['DefectRatio'] = df['DefectRatio'].divide(100)
    return df


def load_kamei2012large_f1():
    df = pd.read_csv('kamei2012large_perf.csv', comment='#')
    return df['F1'].divide(100.).to_list(), 'Kamei12(DPLR)'

def load_kamei2012large_oss_f1():
    df = pd.read_csv('kamei2012large_perf.csv', comment='#')
    return df.iloc[0:6]['F1'].divide(100.).to_list(), 'Kamei12(DPLR):OS'

def load_kamei2012large_oss_proj_f1():
    df = pd.read_csv('kamei2012large_perf.csv', comment='#')
    f1 = df[['Proj', 'F1']].iloc[0:6]
    f1['F1'] = f1['F1'].divide(100)

    f1_dict = dict()
    for p in oss6_proj_list:
        f1_dict[p] = []

    for p in oss6_proj_list:
        f1_dict[p].extend(f1[f1['Proj'].str.lower() == p.lower()]['F1'].to_list())
    return f1_dict

def load_kamei2012large_rec20():
    df = pd.read_csv('kamei2012large_perf.csv', comment='#')
    return df['Acc20'].to_list(), 'Kamei12(EALR)'

def load_kamei2012large_pub_rec20():
    df = pd.read_csv('kamei2012large_perf.csv', comment='#')
    return df.iloc[0:6]['Acc20'].to_list(), 'Kamei12(EALR):OS'

def load_kamei2012large_popt():
    df = pd.read_csv('kamei2012large_perf.csv', comment='#')
    return df['Popt'].to_list(), 'Kamei12(EALR)'

def load_kamei2012large_pub_popt():
    df = pd.read_csv('kamei2012large_perf.csv', comment='#')
    return df.iloc[0:6]['Popt'].to_list(), 'Kamei12(EALR):OS'

def load_lr_f1_data():
    f1_list = []
    label_list = []

    f1,label = load_kamei2012large_oss_f1()
    f1_list.append(f1)
    label_list.append(label)

    f1,label = load_yang2015deep_lr_f1()
    f1_list.append(f1)
    label_list.append(label)

    f1,label = load_zhu2020within_lr_f1()
    f1_list.append(f1)
    label_list.append(label)

    return f1_list,label_list

def load_f1_data():
    f1_list = []
    label_list = []

    f1,label = load_kamei2012large_oss_f1()
    f1_list.append(f1)
    label_list.append(label)


    f1,label = load_kamei2012large_f1()
    f1_list.append(f1)
    label_list.append(label)

    f1,label = load_jiang2013personalized_f1()
    f1_list.append(f1)
    label_list.append(label)

    f1,label = load_yang2015deep_f1()
    f1_list.append(f1)
    label_list.append(label)

    f1,label = load_tourani2016impact_f1()
    f1_list.append(f1)
    label_list.append(label)

    f1,label = load_yang2017tlel_f1()
    f1_list.append(f1)
    label_list.append(label)

    f1,label = load_liu2017code_f1()
    f1_list.append(f1)
    label_list.append(label)

    f1,label = load_young2018replication_f1()
    f1_list.append(f1)
    label_list.append(label)

    # time-sensitive analysis
    f1,label = load_pascarella2019fine_f1()
    f1_list.append(f1)
    label_list.append(label)

    # out-of-sample bootstrap
    f1,label = load_fan2019impact_f1()
    f1_list.append(f1)
    label_list.append(label)

    f1,label = load_li2020effort_f1()
    f1_list.append(f1)
    label_list.append(label)

    f1,label = load_zhu2020within_f1()
    f1_list.append(f1)
    label_list.append(label)

    # project context factors
    f1,label = load_kang2020predicting_f1()
    f1_list.append(f1)
    label_list.append(label)

    # out-of-sample bootstrap
    f1,label = load_duan2021impact_f1()
    f1_list.append(f1)
    label_list.append(label)


    return f1_list,label_list

def load_rec20_data():
    rec20_list = []
    label_list = []

    rec20,label = load_kamei2012large_pub_rec20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_kamei2012large_rec20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_jiang2013personalized_pofb20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_yang2015deep_pofb20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_yang2016effort_rec20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_yang2017tlel_pofb20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_huang2017supervised_rec20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_liu2017code_rec20() 
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_chen2018multi_acc20() 
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_fan2019impact_rec20()
    rec20_list.append(rec20)
    label_list.append(label)


    rec20,label = load_huang2019revisiting_rec20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_li2020effort_acc20()
    rec20_list.append(rec20)
    label_list.append(label)

    rec20,label = load_yan2020effort_rec20()
    rec20_list.append(rec20)
    label_list.append(label)

    return rec20_list,label_list

def load_popt_data():
    popt_list = []
    label_list = []

    popt,label = load_kamei2012large_pub_popt()
    popt_list.append(popt)
    label_list.append(label)

    popt,label = load_kamei2012large_popt()
    popt_list.append(popt)
    label_list.append(label)

    popt,label = load_yang2016effort_popt()
    popt_list.append(popt)
    label_list.append(label)

    popt,label = load_liu2017code_popt()
    popt_list.append(popt)
    label_list.append(label)

    popt,label = load_chen2018multi_popt()
    popt_list.append(popt)
    label_list.append(label)

    popt,label = load_li2020effort_popt()
    popt_list.append(popt)
    label_list.append(label)

    return popt_list,label_list

def load_proj_f1_data():
    # 1. 
    f1_dict = load_kamei2012large_oss_proj_f1()

    # 2. 
    tmp_dict = load_yang2015deep_proj_f1()
    for k in f1_dict.keys():
        f1_dict[k].extend(tmp_dict[k])

    # 3. 
    tmp_dict = load_kamei2016studying_oss6_proj_f1()
    for k in f1_dict.keys():
        f1_dict[k].extend(tmp_dict[k])

    # 4. 
    tmp_dict = load_yang2017tlel_proj_f1()
    for k in f1_dict.keys():
        f1_dict[k].extend(tmp_dict[k])

    # 5. 
    tmp_dict = load_young2018replication_proj_f1()
    for k in f1_dict.keys():
        f1_dict[k].extend(tmp_dict[k])
    
    # 6.
    tmp_dict = load_li2020effort_proj_f1()
    for k in f1_dict.keys():
        f1_dict[k].extend(tmp_dict[k])

#    f1,label = load_zhu2020within_f1()
#    f1_list.append(f1)
#    label_list.append(label)
#
    return f1_dict
