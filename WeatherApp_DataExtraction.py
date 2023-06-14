# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 19:21:18 2023

@author: jan.osredkar
"""

# you PIP INSTALLed LXML

from bs4 import BeautifulSoup
import requests

# class HTMLfetcher intended to fetch a response from RS agromet web page.
class HTMLfetcher:
    def __init__(self, inURL:str):
        self.__URL = inURL

    def createResponse(self):
        self.__response = requests.get(self.__URL)
        if self.__response.status_code == 200:
            return self.__response
        else:
            print("Error: Failed to fetch the webpage")
                  
    @property #getter for URL(encapsulation)
    def URL(self):
        return self.__URL
    
    @property  #getter for response(encapsulation)
    def response(self):
        return self.__response

# class HTMLparser intended to get data from RS agromet web page. Input is a response generated from HTMLfetcher
class HTMLparser:
    def __init__(self, inResponse):
        self.__soupFeed = inResponse
        
    #Get all .xml (full)links (with main part of the URL: "http://agromet.mkgp.gov.si" + "/APP2/AgrometContent/xml/55.xml")
    def getXMLfiles(self):
        def findMainURL(self):
            return self.__soupFeed.url[self.__soupFeed.url.find('http'):self.__soupFeed.url.find('.si')+3]
       
        self.soup = BeautifulSoup(self.__soupFeed.content, features="html.parser")
        # print("Tole je URL: ", self.__soupFeed.url)
        self.xml = []
        for a in self.soup.findAll('td'):
            if(a.find('a')):
                if(a.find('a')['href'].find('.xml')>0):
                    # print(a.find('a')['href'])
                    self.xml.append(findMainURL(self) + a.find('a')['href'])
        return self.xml
                    
    def getData_fromXML(self):
        #extract text content from a txt within a tags 
        def getTXT(self, inTxt):
            self.outTxt = []
            for param in inTxt:
                self.outTxt.append(param.get_text())
            return self.outTxt
                
        self.XMLsoup = BeautifulSoup(self.__soupFeed.content, features='lxml')
        
        self.domainTitle = getTXT(self.XMLsoup, self.XMLsoup.findAll('domain_title'))
        self.TimeDate = getTXT(self.XMLsoup, self.XMLsoup.findAll('valid'))[2:]
        self.avTemperature = getTXT(self.XMLsoup, self.XMLsoup.findAll('tavg'))
        self.avRelativeHumidity = getTXT(self.XMLsoup, self.XMLsoup.findAll('rhavg'))
        self.avWindSpeed = getTXT(self.XMLsoup, self.XMLsoup.findAll('ffavg'))
        return [self.domainTitle, self.TimeDate, self.avTemperature, self.avRelativeHumidity, self.avWindSpeed]
            
    @property  #getter for response(encapsulation)
    def soupFeed(self):
        return self.__soupFeed