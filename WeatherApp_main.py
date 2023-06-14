# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 20:51:05 2023

@author: jan.osredkar
"""

from DataExtraction_newsite_classes import HTMLfetcher, HTMLparser

def main():

    url = "http://agromet.mkgp.gov.si/APP2/sl/Home/Index?id=2&archive=0&graphs=1#esri_map_iframe"
    
    ## create response from main page
    fetchURL = HTMLfetcher(url)
    createdResponse = fetchURL.createResponse()
    
    ## get all xml files on the main webpage
    ParseWebpage = HTMLparser(createdResponse)
    xmls = ParseWebpage.getXMLfiles()
    
    data_in_city = []
    for i in range(len(xmls)):
    #% create response from xml files/website
        fetchURL_xml = HTMLfetcher(xmls[i])
        createdResponse_xml = fetchURL_xml.createResponse()
    
        ## parse xml files
        ParseWebpage_xml = HTMLparser(createdResponse_xml)
        data_in_city.append(ParseWebpage_xml.getData_fromXML())
    
    return data_in_city
    
if __name__ == '__main__':
    WeatherData = main()
    
    