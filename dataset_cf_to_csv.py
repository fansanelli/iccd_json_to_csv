#!/bin/python

import json

separator = '\t'
indirizzi = {}
geometrie = {}

def convert(path):
    with open(path) as json_file:
        data = json.load(json_file)
        for root in data['@graph']:
            if root['@type'] == 'clvapit:Address':
                tmpstr = ''
                if 'rdfs:label' in root:
                    if isinstance(root['rdfs:label'], str):
                        tmpstr = root['rdfs:label']
                    else:
                        tmpstr = root['rdfs:label'][0]                    
                indirizzi[root['@id']] = tmpstr
        for root in data['@graph']:
            if root['@type'] == 'clvapit:Geometry':
                tmpstr = ''
                if 'clvapit:serialization' in root:
                    tmpstr = root['clvapit:serialization']['@value']
                if 'clvapit:isGeometryFor' in root:
                    geometrie[root['clvapit:isGeometryFor']['@id']] = tmpstr
        for root in data['@graph']:
            if root['@type'] == 'cis:Site' and isinstance(root['l0:name'], str):
                tmpstr = ''
                if 'cis:siteAddress' in root:
                    tmpstr = indirizzi[root['cis:siteAddress']['@id']]
                tmpstr += separator 
                if root['@id'] in geometrie:      
                    tmpstr += geometrie[root['@id']]
                print(root['@id'] + separator + root['l0:name'] + separator + tmpstr)


def main():
    convert('dataset-contenitoriFisici.json')

if __name__ == '__main__':
    main()

