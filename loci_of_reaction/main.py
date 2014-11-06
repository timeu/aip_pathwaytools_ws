import json
import requests
import re
import xmltodict
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

    if not (('reaction' in arg)):
        return

    reaction = arg['reaction']
    reaction = reaction.upper()


    svc_url = 'http://pmn.plantcyc.org/apixml?fn=genes-of-reaction&id=ARA:'+reaction+'&details=full'


    r = requests.get(svc_url)

    # Interpret the result string, turn it into AIP JSON records
    tree = xmltodict.parse(r.content)
    if (tree):
        print json.dumps(tree, indent=3)
        print '---'



def list(arg):
	pass
