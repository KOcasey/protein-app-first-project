import requests
import re

base_url = 'https://kids.kiddle.co/'

def get_protein_facts (name):
    response = requests.get(base_url + name).text
    stripped = re.sub('<[^<]+?>', '', response)
    start_ind = stripped.find("Kids Encyclopedia Facts")
    facts = stripped[start_ind:stripped.find("Related pages", start_ind)]
    return facts;

print(get_protein_facts('lysozyme'))
