import requests

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
    return rna;

def rna_to_dna (rna_sequence):
    dna = rna_sequence.replace('U', 'T')
    return dna;

print(info_name_organism('lysozyme', 'human'))



