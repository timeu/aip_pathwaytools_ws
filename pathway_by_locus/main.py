import json
import requests
import xmltodict
import re
from xml.etree import ElementTree

# Invoke PLANTCYC  web services given a locus and filter parameters
#
# Example URI:
#
# Response:

def search(arg):

# arg contains a dict with several key:values
#
# locus is AGI identifier and is mandatory
#
#
#
    if not (('locus' in arg)):
        return

    locus = arg['locus']
    locus = locus.upper()
    p = re.compile('AT[1-5MC]G[0-9]{5,5}', re.IGNORECASE)
    if not p.search(locus):
        return

    svc_url = 'http://pmn.plantcyc.org/apixml?fn=pathways-of-gene&id=ARA:'+locus+'&details=full'


    r = requests.get(svc_url)

    # Interpret the result string, turn it into AIP JSON records
    tree = xmltodict.parse(r.content)
    if (tree):
        print json.dumps(tree, indent=3)
        print '---'



def list(arg):
	pass
