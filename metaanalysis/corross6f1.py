import numpy as np

from scipy.stats import spearmanr

from matplotlib import pyplot as plt

from loaddata import load_proj_f1_data, load_kamei2012large_oss6_context

def get_context(ctx, ctx_factor):
    data = ctx[ctx_factor].to_list()
    return data


def cmp_corr_f1_vs_nchanges(**kwargs):
    ctx = load_kamei2012large_oss6_context()
    ctx = ctx.sort_values('Changes', axis='index')
    ctx_data = get_context(ctx, 'Changes')
    print(ctx_data)


    labels = ctx['Project'].to_list()
    ddict = load_proj_f1_data()
    data = [ddict[k] for k in labels]
    print(data)
    avrg_f1 = np.mean(data, axis=1)
    print(avrg_f1)

    corr,pv = spearmanr(ctx_data, avrg_f1)
    print('F1 vs. Changes', corr, pv)

    return 'F1 vs. Number of Changes', corr, pv





def cmp_corr_f1_vs_defect_ratio(**kwargs):
    ctx = load_kamei2012large_oss6_context()
    ctx = ctx.sort_values('DefectRatio', axis='index')
    ctx_data = get_context(ctx, 'DefectRatio')
    print(ctx_data)


    labels = ctx['Project'].to_list()
    ddict = load_proj_f1_data()
    # print(ctx['DefectRatio'])
    data = [ddict[k] for k in labels]
    print(data)

    avrg_f1 = np.mean(data, axis=1)
    print(avrg_f1)

    corr,pv = spearmanr(ctx_data, avrg_f1)
    print('F1 vs. Defect Ratio', corr, pv)

    return 'F1 vs. Ratio of Defective Changes', corr, pv


def cmp_corr_f1_vs_loc_file():
    ctx = load_kamei2012large_oss6_context()
    ctx = ctx.sort_values('LOCFile', axis='index')
    labels = ctx['Project'].to_list()
    ddict = load_proj_f1_data()
    # print(ctx['LOCFile'])
    data = [ddict[k] for k in labels]

def cmp_corr_f1_vs_loc_change(**kwargs):
    ctx = load_kamei2012large_oss6_context()
    ctx = ctx.sort_values('LOCChange', axis='index')
    ctx_data = get_context(ctx, 'LOCChange')
    print(ctx_data)
    

    labels = ctx['Project'].to_list()
    ddict = load_proj_f1_data()
    # print(ctx['LOCChange'])
    data = [ddict[k] for k in labels]
    print(data)

    avrg_f1 = np.mean(data, axis=1)
    print(avrg_f1)

    corr,pv = spearmanr(ctx_data, avrg_f1)
    print('F1 vs. LOC of Change', corr, pv)

    return 'F1 vs. Change Size', corr, pv


def cmp_corr_f1_vs_ndevs_per_file_avrg(**kwargs):
    ctx = load_kamei2012large_oss6_context()
    ctx = ctx.sort_values('NDevPerFileAvrg', axis='index')
    ctx_data = get_context(ctx, 'NDevPerFileAvrg')
    print(ctx_data)


    labels = ctx['Project'].to_list()
    ddict = load_proj_f1_data()
    data = [ddict[k] for k in labels]
    print(data)

    avrg_f1 = np.mean(data, axis=1)
    print(avrg_f1)

    corr,pv = spearmanr(ctx_data, avrg_f1)
    print('F1 vs. NDevPerFileAvrg', corr, pv)

    return 'F1 vs. Number of Developers Per File', corr, pv


def cmp_corr_f1_vs_ndevs_per_file_max():
    ctx = load_kamei2012large_oss6_context()
    ctx = ctx.sort_values('NDevPerFileMax', axis='index')
    labels = ctx['Project'].to_list()
    ddict = load_proj_f1_data()
    # print(ctx['NDevPerFileMax'])
    data = [ddict[k] for k in labels]

def print_table(names, corrs, pvs):
    for i,n in enumerate(names):
        if i == 0: 
            print(n, end='')
        else:
            print(' & ' + n, end='')
    print(r'\\')

    for i,(c,p) in enumerate(zip(corrs,pvs)):
        if i == 0:
            print('{:.3f} & {:.3f} '.format(c, p), end='')
        else:
            print(' & {:.3f} & {:.3f} '.format(c,p), end='')
    print(r'\\')



def main():
    names, corrs, pvs = [],[],[]

    name,corr,pv = cmp_corr_f1_vs_nchanges()
    names.append(name)
    corrs.append(corr)
    pvs.append(pv)

    name,corr,pv = cmp_corr_f1_vs_defect_ratio()
    names.append(name)
    corrs.append(corr)
    pvs.append(pv)

    name,corr,pv = cmp_corr_f1_vs_loc_change()
    names.append(name)
    corrs.append(corr)
    pvs.append(pv)

    name,corr,pv = cmp_corr_f1_vs_ndevs_per_file_avrg()
    names.append(name)
    corrs.append(corr)
    pvs.append(pv)

    print_table(names, corrs, pvs)

if __name__=='__main__':
    main()

