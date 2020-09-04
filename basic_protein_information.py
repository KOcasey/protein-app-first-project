import requests
import re

base_url = 'https://kids.kiddle.co/'

def get_protein_facts (name):
    response = requests.get(base_url + name).text
    stripped = re.sub('<[^<]+?>', '', response)
    start_ind = stripped.find("Kids Encyclopedia Facts")
    loop_ind = stripped.find("Kids Encyclopedia Facts")
    img_count = stripped.count("Images for kids")
    for i in range(1, img_count):
        img_ind = stripped.find("Images for kids", loop_ind)
        if i != img_count:
            loop_ind = img_ind + 15
    facts = stripped[start_ind:stripped.find("Images for kids", loop_ind)]
    facts = facts[0:facts.find("Related pages", 0)]
    return facts;

print(get_protein_facts('myosin'))

#need to loop through count of images and set index to after the second to last image