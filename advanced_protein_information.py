import requests

G = 'GGC' #glycine
E = 'GAA' #glutamic acid
D = 'GAU' #aspartic acid
V = 'GUG' #valine
A = 'GCG' #alanine
R = 'CGC' #arginine
S = 'AGC' #serine
K = 'AAA' #lysine
N = 'AAC' #asparagine
M = 'AUG' #methionine
I = 'AUU' #isoluecine
T = 'ACC' #threonine
W = 'UGG' #tryptophan
C = 'UGC' #cysteine
Y = 'UAU' #tyrosine
L = 'CUG' #leucine
F = 'UUU' #phenylalanine
Q = 'CAG' #glutamine
H = 'CAU' #histidine
P = 'CCG' #proline

base_url = 'http://www.uniprot.org'
kb_endpoint = '/uniprot/'

def info_name (name):
    return name;

def info_name_organism (name, organism):
    query = '?query=name%3A' + name + '+AND+reviewed%3Ayes+organism%3A' + organism + '&sort=score&columns=id,reviewed,protein%20names,organism,length&format=tab'
    response = requests.get(base_url + kb_endpoint + query)
    return response.text;

def amino_to_rna (amino_sequence):
    rna = ''
    for i in range(0, len(amino_sequence)):
        if amino_sequence[i] == 'G':
            rna += G
        elif amino_sequence[i] == 'E':
            rna += E
        elif amino_sequence[i] == 'D':
            rna += D
        elif amino_sequence[i] == 'V':
            rna += V
        elif amino_sequence[i] == 'A':
            rna += A
        elif amino_sequence[i] == 'R':
            rna += R
        elif amino_sequence[i] == 'S':
            rna += S
        elif amino_sequence[i] == 'K':
            rna += K
        elif amino_sequence[i] == 'N':
            rna += N
        elif amino_sequence[i] == 'M':
            rna += M
        elif amino_sequence[i] == 'I':
            rna += I
        elif amino_sequence[i] == 'T':
            rna += T
        elif amino_sequence[i] == 'W':
            rna += W
        elif amino_sequence[i] == 'C':
            rna += C
        elif amino_sequence[i] == 'Y':
            rna += Y
        elif amino_sequence[i] == 'L':
            rna += L
        elif amino_sequence[i] == 'F':
            rna += F
        elif amino_sequence[i] == 'Q':
            rna += Q
        elif amino_sequence[i] == 'H':
            rna += H
        else:
            rna += P
    return rna;

def rna_to_dna (rna_sequence):
    dna = rna_sequence.replace('U', 'T')
    return dna;

print(info_name_organism('lysozyme', 'human'))
print(amino_to_rna('GEDVARSKNMITWCYLFQH'))



