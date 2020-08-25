#!/bin/python

import json

separator = '\t'
indirizzi = {}
geometrie = {}
siti = {}

def convert(path):
    with open(path) as json_file:
        data = json.load(json_file)
        for root in data['@graph']:
            if root['@type'] == 'clvapit:Address':
                tmpstr = ''
                if 'clvapit:fullAddress' in root:
                    tmpstr = root['clvapit:fullAddress']
                indirizzi[root['@id']] = tmpstr
            if root['@type'] == 'clvapit:Geometry':
                tmpstr = ''
                if 'clvapit:lat' in root:
                    tmpstr = root['clvapit:lat'] + ',' + root['clvapit:long']
                geometrie[root['@id']] = tmpstr
            if root['@type'] == 'cis:Site':
                tmpstr = ''
                if 'cis:siteAddress' in root:
                    tmpstr = indirizzi[root['cis:siteAddress']['@id']]
                tmpstr += separator
                if 'clvapit:hasGeometry' in root:
                    tmpstr += geometrie[root['clvapit:hasGeometry']['@id']]
                siti[root['@id']] = tmpstr
            if root['@type'] == 'cis:CulturalInstituteOrSite':
                tmpstr = ''
                if 'cis:hasSite' in root and root['cis:hasSite']['@id'] in siti:
                    tmpstr = siti[root['cis:hasSite']['@id']]
                if 'l0:identifier' in root:
                    print(root['l0:identifier'] + separator + root['cis:institutionalCISName']['@value'] + separator + tmpstr)


def main():
    convert('dataset-contenitoriGiuridiciCampania.json')
    convert('dataset-contenitoriGiuridiciLazio.json')
    convert('dataset-contenitoriGiuridiciLiguria.json')
    convert('dataset-contenitoriGiuridiciMarche.json')
    convert('dataset-contenitoriGiuridiciPiemonte.json')
    convert('dataset-contenitoriGiuridiciSardegna.json')
    convert('dataset-contenitoriGiuridiciToscana.json')
    convert('dataset-contenitoriGiuridiciUmbria.json')
    convert('dataset-contenitoriGiuridiciVeneto.json')

if __name__ == '__main__':
    main()

