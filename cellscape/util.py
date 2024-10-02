amino_acid_3letter = {'ALA':'A',
'ASX':'B',
'CYS':'C',
'ASP':'D',
'GLU':'E',
'PHE':'F',
'GLY':'G',
'HIS':'H',
'ILE':'I',
'LYS':'K',
'LEU':'L',
'MET':'M',
'MSE':'M',
'ASN':'N',
'PRO':'P',
'GLN':'Q',
'ARG':'R',
'SER':'S',
'THR':'T',
'VAL':'V',
'TRP':'W',
'XAA':'X',
'TYR':'Y',
'GLX':'Z'}

dna_3letter = {'A':'A',
"DA":"DA",
'U':'U',
'DU':'DU',
'G':'G',
"DG":"DG",
'T':'T',
"DT":"DT",
'C':'C',
'DC': 'DC'}

def group_by(l, key):
    """Take a list of dictionaries and group them according to a key."""
    d = dict()
    for i in l:
        k = key(i)
        if k in d:
            d[k].append(i)
        else:
            d[k] = [i]
    return d