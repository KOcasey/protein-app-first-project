import requests
import json

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

def protein_list_name (name):
    query = '?query=name%3A' + name + '+AND+reviewed%3Ayes&sort=score&columns=id,reviewed,protein%20names,organism,length&format=tab'
    response = requests.get(base_url + kb_endpoint + query)
    return response.text;

def protein_list_name_organism (name, organism):
    query = '?query=name%3A' + name + '+AND+reviewed%3Ayes+organism%3A' + organism + '&sort=score&columns=id,reviewed,protein%20names,organism,length&format=tab'
    response = requests.get(base_url + kb_endpoint + query)
    return response.text;

def protein_amino_sequence (id_number):
    response = (requests.get(base_url + kb_endpoint + id_number + '.fasta')).text
    response = response[response.find('SV=') + 2:len(response)]
    return response;

def get_protein_function (id_number):
    response = requests.get(base_url + kb_endpoint + id_number + '.txt').text
    func_index = response.find('FUNCTION')
    prot_func = response[func_index:response.find('-!-', func_index)]
    prot_func = prot_func.replace('CC', '')
    prot_func = " ".join(prot_func.split())
    return prot_func;

def get_protein_subunit (id_number):
    response = requests.get(base_url + kb_endpoint + id_number + '.txt').text
    sunit_index = response.find('SUBUNIT')
    prot_sunit = response[sunit_index:response.find('-!-', sunit_index)]
    prot_sunit = prot_sunit.replace('CC', '')
    prot_sunit = " ".join(prot_sunit.split())
    return prot_sunit;

def get_protein_subcell_location (id_number):
    response = requests.get(base_url + kb_endpoint + id_number + '.txt').text
    sloc_index = response.find('SUBCELLULAR LOCATION')
    prot_sloc = response[sloc_index:response.find('-!-', sloc_index)]
    prot_sloc = prot_sloc.replace('CC', '')
    prot_sloc = " ".join(prot_sloc.split())
    return prot_sloc;

def get_protein_miscellaneous_info (id_number):
    response = requests.get(base_url + kb_endpoint + id_number + '.txt').text
    misc_index = response.find('MISCELLANEOUS')
    prot_misc = response[misc_index:response.find('-!-', misc_index)]
    prot_misc = prot_misc.replace('CC', '')
    prot_misc = " ".join(prot_misc.split())
    return prot_misc;

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

print(protein_list_name_organism('lysozyme', 'human'))
print(protein_list_name('lysozyme'))
print(amino_to_rna(protein_amino_sequence('P61626')))
print(get_protein_miscellaneous_info('P61626'))






