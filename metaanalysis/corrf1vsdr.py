import numpy as np
from scipy.stats import spearmanr

from plotf1vsdr import get_avrg_jian2013personalized_f1, \
    get_avrg_tourani2016impact_f1, \
    get_avrg_zhu2018empirical_f1, \
    get_avrg_pascarella_f1,\
    get_avrg_fan2019impact_f1,\
    get_avrg_duan2021impact_f1\

def scale_dratio(dratios):
    small = min(dratios)
    big = max(dratios)
    diff = big - small
    return [(r-small)/diff for r in dratios]

def sort_data(f1s, dratios):
    # for r,f in zip(dratios,f1s):
    #     print(r,f)
    fds = sorted(zip(f1s, dratios), key=lambda t: t[1])
    f1s = [f1 for f1,_ in fds]
    dratios = [r for _,r in fds]
    # for r,f in zip(dratios,f1s):
    #    print(r,f)
    return f1s, dratios

def collapse_data(f1s, dratios):
    # for r,f in zip(dratios,f1s):
    #    print(r,f)

    d = dict()
    for f,r in zip(f1s,dratios):
        # print('....', f,r)
        if not str(r) in d.keys():
            d[str(r)] = f
        elif isinstance(d[str(r)], list):
            d[str(r)].append(f)
        else:
            d[str(r)] = [d[str(r)], f]

    f1s = [np.mean(d[k]) for k in d.keys()]
    dratios = [float(k) for k in d.keys()]

    # print('--------------')
    # for r,f in zip(dratios,f1s):
    #     print(r,f)

    return f1s, dratios

def resample_data(f1s, dratios, rsamples=np.linspace(0,1,num=11, endpoint=True)):
    f1s, dratios = sort_data(f1s, dratios)
    f1s, dratios = collapse_data(f1s, dratios)
    f1samples = np.interp(rsamples, dratios, f1s)

    # for r,f in zip(rsamples,f1samples):
    #    print(r,f)
    # print('------------')

    return f1samples, rsamples

def corr_f1_vs_ctx():
    f1_jian13,dr_jian13 = get_avrg_jian2013personalized_f1()
    f1_tourani16,dr_tourani16 = get_avrg_tourani2016impact_f1()
    f1_zhu2018,dr_zhu2018 = get_avrg_zhu2018empirical_f1()
    f1_pascarella,dr_pascarella = get_avrg_pascarella_f1()
    f1_fan2019,dr_fan2019 = get_avrg_fan2019impact_f1()
    f1_duan2021,dr_duan2021 = get_avrg_duan2021impact_f1()

    yx_list = [(f1_jian13,dr_jian13,'Jian13(PCC+)'), \
            (f1_tourani16,dr_tourani16,'Tourani16'),\
            (f1_zhu2018,dr_zhu2018,'Zhu18'),\
            (f1_pascarella,dr_pascarella, 'Pascarella119'),\
            (f1_fan2019,dr_fan2019, 'Fan19'), \
            (f1_duan2021,dr_duan2021, 'Duan21')]
    for (y, x, n) in yx_list:
        corr,pv = spearmanr(y, x)
        print('{} & {:5.2f} & {:5.3f} \\\\'.format(n, corr, pv))
    
   
def corr_f1_vs_f1():
    f1_jian13,dr_jian13 = resample_data(*get_avrg_jian2013personalized_f1())
    f1_tourani16,dr_tourani16 = resample_data(*get_avrg_tourani2016impact_f1())
    f1_zhu2018,dr_zhu2018 = resample_data(*get_avrg_zhu2018empirical_f1())
    f1_pascarella,dr_pascarella = resample_data(*get_avrg_pascarella_f1())
    f1_fan2019,dr_fan2019 = resample_data(*get_avrg_fan2019impact_f1())
    f1_duan2021,dr_duan2021 = resample_data(*get_avrg_duan2021impact_f1())


    yx_list = [(f1_jian13,dr_jian13,'Jian13(PCC+)'), \
            (f1_tourani16,dr_tourani16,'Tourani16'),\
            (f1_zhu2018,dr_zhu2018,'Zhu18'),\
            (f1_pascarella,dr_pascarella, 'Pascarella119'),\
            (f1_fan2019,dr_fan2019, 'Fan19'), \
            (f1_duan2021,dr_duan2021, 'Duan21')]


    mtx = [] 
    for (y1,x1,_) in yx_list:
        row = []
        for (y2,x2,_) in yx_list: 
            assert(all(x1 == x2))
            corr,pv = spearmanr(y1, y2)
            row.append((corr,pv))
        mtx.append(row)

    for row in mtx:
        for (c,p) in row:
            print('({:5.2f} {:4.2f})'.format(c,p), end=' ')
        print()

if __name__ == '__main__':
    corr_f1_vs_f1()
    corr_f1_vs_ctx()

