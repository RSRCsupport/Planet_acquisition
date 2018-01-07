#! usr/bin/env python
"""a complementary script to download planet data: get the coordinates from geojson file drawn in geojson.io 
and insert them in the redding.json file 
defined by Planet in https://www.planet.com/docs/api-quickstart-examples/step-3-download/

Author: Rodney Borrego Acevedo (Rodney.Borrego@dnrm.qld.gov.au).  No licence, though please attribute me and publish any derivatives open source. """

import json
import argparse
import sys
import os

def jsonToDict(infile):
    "convert json to dictionary"
    with open (infile) as f:
        outdict=json.load(f)
    return outdict

def reEnc(fileToEncode, dictionary_target):
    "function to re-encode (make it json again from dict) and rewrite the file"
    with open(fileToEncode, 'w') as file:
        json.dump(dictionary_target, file)
        
   
   

def mainRoutine():
    cmdargs=getCmdArgs()
    dict_source=jsonToDict(cmdargs.coordinate_source)
    dict_target=jsonToDict(cmdargs.coordinate_target)
    
    for item in dict_source['features']: ## get the coordinates from the source
        source_coord=item['geometry']['coordinates']
        #get rid of 0.0 as a third coordinate in list source_coord
    for c in source_coord:
        for n in c:
            if len(n)>2:
                del n[2] # here I am looping inside the nested list to remove 0.0 as the last coordinate that appears sometimes when creating the redding.json/
            # #to check this just print n[2]


    try:
        for feat in dict_target['config']:
            if feat['config']['coordinates']:
                feat['config']['coordinates']=source_coord
                #
    except KeyError:
        pass
        

    reEnc(cmdargs.coordinate_target, dict_target)
    print "Finish your bloody thing"


def getCmdArgs():
    parser=argparse.ArgumentParser(description='a script to insert coordinates to redding.json (Planet query jsonfile) from geojson file drawn from geojeson.io')
    parser.add_argument('-s_json', '--coordinate_source', help='geojson file from geojson.io')
    parser.add_argument('-t_json', '--coordinate_target', help='json file from  https://www.planet.com/docs/api-quickstart-examples/step-3-download/')
    cmdargs=parser.parse_args()
    if cmdargs.coordinate_source and cmdargs.coordinate_target is None:
        parser.print_help()
        sys.exist()
    return cmdargs
    
if __name__=='__main__':
    mainRoutine()