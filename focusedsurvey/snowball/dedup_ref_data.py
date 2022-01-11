import hashlib
import re
import sys

from extract_ref_data import is_comment, is_blank



lineno = 0

refstartpatterns = [r'^\s*\D+\(\d{4}[a-z]*\)', 
        r'^\s*[^\d\(\)]+\d{4}', 
        r'^\s*\[\d+\]', 
        r'^\s*\d+\s+', 
        r'^\s*\d+\.\s+']


reftitlepatterns = [
        [r'^\s*\D+\(\d{4}[a-z]*\)\s*([^\.]+)\.\s+[A-Z]',
            r'^\s*[^\d\(\)]+\(\d{4}[a-z]*\)\s*(\D+)\?', 
            r'^\s*[^\d\(\)]+\(\d{4}[a-z]*\)\s*(\D+)\.\s*In:',
            r'^\s*[^\d\(\)]+\(\d{4}[a-z]*\)\s*(\D+)\s*IEEE',
            r'^\s*[^\d\(\)]+\(\d{4}[a-z]*\)\s*([A-Z][a-z\s]+)',
            r'^\s*[^\d\(\)]+\(\d{4}[a-z]*\)\s*([a-z]+:\s[A-Z][a-z\s]+)',
            r'^\s*[^\d\(\)]+\(\d{4}[a-z]*\)\s*(.*)\s*Morgan Kaufmann'
            ],
        [None],
        [r'^\s*\[\d+\].*“([^“”]+),”',
            r'^\s*\[\d+\].*,\s+“(.*),”',
            r'^\s*\[\d+\].*“([^“”]+)”', 
            r'^\s*\[\d+\]\D+\d{4}\.\s+([^\.]+)\.', 
            r'^\s*\[\d+\].*,\s\w\.\s\w+\.\s(.*)\.\sFSE',
            r'^\s*\[\d+\].*,\s\w\.\s\w+\.\s(.*)\.\sICSE',
            r'^\s*\[\d+\].*,\s\w\.\s\w+\.\s(.*)\.\sESEM',
            r'^\s*\[\d+\].*and\s+\w\.\s+\w+\.\s+(.*)\.\s+In Proc',
            r'^\s*\[\d+\].*and\s+\w\.\s+\w+\.\s+\d+\.\s+(.*)\.\s+In Proc',
            r'^\s*\[\d+\].*\.\s+(.*)\.\s+In Proc',
            r'^\s*\[\d+\].*\.\s+(.*)\?\s+In Proc',
            r'^\s*\[\d+\].*\.\s+(.*)\.\s+IEEE Trans.',
            r'^\s*\[\d+\].*\.\s+(.*)\.\s+Software Quality Journal',
            r'^\s*\[\d+\].*\.\s+(.*)\.\s+Empirical Software Engineering',
            r'^\s*\[\d+\].*\.\s+(.*)\?\s+IEEE Trans.',
            ('^\[\d+\]\s(\w\.\s+\w+,\s+)*\w\.\s+\w+\.\s+(.*)\.\sMSR', 1),
            ('^\[\d+\]\s(\w\.(\w\.)*\s\w+,\s)*\w\.(\w\.)*\s\w+\.\s+(.*)\.\s+ESEM', 3),
            ('^\[\d+\]\s(\w\.(\w\.)*\s\w+,\s)*\w\.(\w\.)*\s\w+\.\s+(.*)\.\s+cta', 3),
            ('^\[\d+\]\s(\w\.(\w\.)*\s\w+,\s)*\w\.(\w\.)*\s\w+\.\s+(.*)\.\s+HASE', 3),
            ('^\[\d+\]\s(\w\.(\w\.)*\s\w+,\s)*\w\.(\w\.)*\s\w+\.\s+(.*)\.\s+ACM', 3),
            ('^\[\d+\]\s(\w\.(\w\.)*\s*\w+,\s)*\w\.(\w\.)*\s\w+\.\s+(.*)\.\s+Automated', 3),
            ('^\[\d+\]\s(\w\.(\w\.)*\s*\w+,\s)*\w\.(\w\.)*\s\w+\.\s+(.*)\.\s+QRS', 3),
            ('^\[\d+\]\s(\w\.(\w\.)*\s*\w+,\s)*\w\.(\w\.)*\s\w+\.\s+(.*)\.\s+ICSE', 3),
            ('^\[\d+\]\s(\w\.(\w\.)*\s*\w+,\s)*\w\.(\w\.)*\s\w+\.\s+(.*)\.\s+arXiv:', 3),
            ('^\[\d+\]\s(\w\.(\w\.)*\s*\w+,\s)*\w\.(\w\.)*\s\w+\.\s+(.*)\.\s+SAIR', 3),
            ('^\[\d+\]\s(\w\.(\w\.)*\s*\w+,\s)*\w\.(\w\.)*\s\w+\.\s+(.*)\.\s+ICSM', 3),
            ('^\[\d+\]\s(\w\.(\w\.)*\s*\w+,\s)*\w\.(\w\.)*\s\w+\.\s+(.*)\.\s+Information\sand\sSoftware', 3),
            ('^\[\d+\]\s(\w+,\s\w\.(\w\.)*\sand\s)\w+,\s\w\.(\w\.)*\s+(.*)\.', 3),
            (r'^\[\d+\]\s(\w\w*\.\s\w+,\s+)*\w\w*\.\s\w+\.\s+(.*)\.\s+Journal', 1),
            r'^\s*\[\d+\].*,\s+([^\.]+)\..+',
            r'^\s*\[\d+\].*\.\s+([^\.0-9]+)\.',
            r'^\s*\[\d+\].*,\s+([^\.]+),\s*\d+',
            (r'^\s*\[\d+\]\s+\w+-\w+\s+et\s+al\.,\s+(.*)\.', 0)
            ],
        [(r'^\s*\d+\s+\w+(\s\w)+(,\s\w+(\s\w)+)*(,\set\sal)*\.\s+(.*)\.\s', 4)],
        [r'^\s*\d+\.\s+[^:]+:\s*([^\.]+)\.',
            r'^\s*\d+\.\s+\D+,\s+"([^""]+),\s*"', 
            r'^\s*\d+\.\s+[\w\.\s]+,([^\,]+),\s',
            r'^\s*\d+\.\s+.*\.\s+([\w\s]+)\.',
            r'^\s*\d+\.\s+[^\d\(\)]+\(\d{4}\)\s+([^\.]+)\.',
            r'^\s*\d+\.\s+[^\d\(\)]+\(\d{4}\)\s+([:A-Za-z\s]+)',
            r'^\s*\d+\.\s+[A-Za-z\s]+:\s+([^\(]+)\('
            ] 

    ]


def check_on_ref_start(entry, logfd):
    global lineno
    selected_tps = []
    for rsp,tp in zip(refstartpatterns, reftitlepatterns):
        m = re.match(rsp, entry)
        if m is None:
            continue
        if not tp is None:
            selected_tps.extend(tp)
            log_state(logfd, lineno, entry, ['matched pattern', rsp, 'selected pattern', tp])
    if len(selected_tps) == 0:
        log_state(logfd, lineno, entry, 'error on check_on_ref_start - no selected title pattern')
        raise RuntimeError('Cannot determine ref type at lineno {} line {}'.format(lineno, entry))

    for p in selected_tps: 
        if p is None: 
            print(selected_tps)
            log_state(logfd, lineno, entry, 'error on check_on_ref_start - no selected title pattern')
            raise RuntimeError('Cannot determine ref type at lineno {} line {}'.format(lineno, entry))

    return selected_tps

def extract_title(pattern_list, entry, logfd):
    global lineno 
    title_list = []
    for pattern in pattern_list:
        if isinstance(pattern, tuple): 
            m = re.match(pattern[0], entry)
        else:
            m = re.match(pattern, entry)
        if m is None:
            log_state(logfd, lineno, entry, ['cannot match title', pattern])
        if not m is None and len(m.groups()) > 0:
            if isinstance(pattern, tuple):
                title_list.append(m.groups()[pattern[1]])
            else:
                title_list.append(m.groups()[0])
    if len(title_list) == 0:
        log_state(logfd, lineno, entry, ['cannot match title', pattern_list])
        raise RuntimeError('Cannot match title at lineno {} line {} pattern {}'.format(lineno, entry, pattern_list))
    elif len(title_list) > 1:
        log_state(logfd, lineno, entry, ['match too many titles', pattern_list])
    return title_list[0]


def log_state(logfd, lineno, line, *argv):
    if argv:
        print('processing lineno {} line {} status {}'.format(lineno, line, argv), file=logfd)
    else:
        print('processing lineno {} line {}'.format(lineno, line), file=logfd)

def hash_title(title):
    titlealpha = ''.join([c.lower() for c in title if c.isalpha()])
    digest = hashlib.md5(titlealpha.encode()).hexdigest()
    return digest

def add_ref_to_dict(refdict, title, refentry):
    digest = hash_title(title)
    if digest in refdict.keys():
        reflist = refdict[digest]
        if len(title) > 10:
            if len(reflist[0]) < len(refentry):
                reflist[0] = refentry
        else:
            reflist.append(refentry)
        refdict[digest] = reflist
    else:
        refdict[digest] = [refentry]

def dedup_ref_entries_by_title(infd, outfd, logfd):
    global lineno
    refdict = dict()
    f = open('title.txt', mode='wt', encoding='utf-8')
    for line in infd.readlines():
        lineno = lineno + 1
        line = line.strip()
        if is_comment(line) or is_blank(line):
            continue
        
        log_state(logfd, lineno, line)
        titlepattern = check_on_ref_start(line, logfd)
        title = extract_title(titlepattern, line, logfd)
        print(title, file=f)
        add_ref_to_dict(refdict, title, line) 
    f.close()

    for digest in refdict.keys():
        for entry in refdict[digest]:
            print(digest, ';', entry, file=outfd)


def main(argv):
    if len(argv) < 4:
        infile = 'jitsdp_cited_entries.txt'
        outfile = 'jitsdp_cited_entries_dedup.txt'
        logfile = 'dedup_ref_data.log'
    else:
        [infile, outfile, logfile] = argv[1:4]

    with open(infile, mode='rt', encoding='utf-8') as infd, \
            open(outfile, mode='wt', encoding='utf-8') as outfd, \
            open(logfile, mode='wt', encoding='utf-8') as logfd:
        dedup_ref_entries_by_title(infd, outfd, logfd)


if __name__ == '__main__':
    main(sys.argv)
