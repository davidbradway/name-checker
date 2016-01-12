# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 20:52:29 2016

pip install web.py

@author: David
"""
import web
import re
from string import ascii_uppercase
import names

bad = names.badNames()

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

def getNames (x):
    #print "Input : " + x

    # Force to uppercase
    x =  x.upper()

    # Remove leading whitespace
    p = re.compile('^[^a-zA-Z]*')
    xNoLeadingWhitespace = p.sub('', x)
        
    # Replace hyphens with spaces
    p2 = re.compile('[-]+')
    xNoHyphen = p2.sub(' ', xNoLeadingWhitespace)
    
    # Remove non alphabetic characters
    p3 = re.compile('[^a-zA-Z ]*')
    xAlphabetic = p3.sub('', xNoHyphen)
    #print "Output: " + xAlphabetic

    p4 = re.compile(r'(?P<firstName>\b\w+\b)\s+(?P<secondName>\b\w+\b)\s+(?P<thirdName>\b\w*\b)')
    m = p4.search(xAlphabetic)
    if m == None:
        #print "matched None, try with no middle name"
        p4 = re.compile(r'(?P<firstName>\b\w+\b)\s+(?P<thirdName>\b\w+\b)')
        m = p4.search(xAlphabetic)
        # set second name
        xSecondName = None
    else:
        # Get second name
        xSecondName = m.group('secondName')    
    # Get first name
    xFirstName =  m.group('firstName')
    # Get third name
    xThirdName = m.group('thirdName')

    return xFirstName, xSecondName, xThirdName

def getInitials (xFirstName, xSecondName, xThirdName):
    # Get first initial
    xFirstInitial = getInitialFromName(xFirstName)
    # Get second initial
    xSecondInitial = getInitialFromName(xSecondName)
    # Get third initial
    xThirdInitial = getInitialFromName(xThirdName)

    # Combine initlals
    initials = xFirstInitial + xSecondInitial + xThirdInitial    
    return initials

def getMonogram (initials):
    # Need three initials for a monogram to make sense
    if len(initials) == 3:
        return initials[0]+initials[2]+initials[1]
    else:
        return None
        
def getListOfConventionalMarriageNames (initials):
    nameList = []
    # Go through all the letters of the alphabet
    for c in ascii_uppercase:
        # Replace old last name initial  with the new married name initial 
        nameList.append(initials[:-1] + c)
    return nameList
    
def getListOfHyphenatedMarriageNames (initials):
    nameList = []
    # Go through all the letters of the alphabet
    for c in ascii_uppercase:
        # Append new married name initial to existing initials
        nameList.append(initials + c)
    return nameList
    
def getListOfRemovedMiddleShiftedMarriageNames (initials):
    nameList = []
    # this function only works with three names
    if len(initials) == 3:
        # Go through all the letters of the alphabet
        for c in ascii_uppercase:
            # Append new married name initial and remove old middle name
            nameList.append(initials[0:1] + initials[-1:] + c)
        return nameList
    else:
        return None
        
def getInitialFromName (name):
    # Get initial
    if name == None:
        initial = ''
    else:
        p = re.compile('^[a-zA-Z]')
        initialTemp = p.match(name)
        initial = initialTemp.group()
    return initial

def getEmailPattern1 (firstName, secondName, thirdName, initials):
    return initials[0:1].lower()+thirdName.lower()+"@company.com"

def getEmailPattern2 (firstName, secondName, thirdName, initials):
    return thirdName.lower()+initials[0:1].lower()+"@company.com"

def getEmailPattern3 (firstName, secondName, thirdName, initials):
    if secondName:
        return initials[0:2].lower()+thirdName.lower()+"@company.com"
    else:
        return ''

def getEmailPattern4 (firstName, secondName, thirdName, initials):
    if secondName:
        return thirdName.lower()+initials[0:2].lower()+"@company.com"
    else:
        return ''

class Index(object):
    def GET(self):
        return render.index(namevalue = '', dict ='')

    def POST(self):
        form = web.input(name="Nobody")

        dict1 = {}

        nameString = "%s" % (form.name)

        # Parse the input string and return the two or three names (Second name could be 'None;)
        xFirstName, xSecondName, xThirdName = getNames(nameString)
        
        initials = getInitials(xFirstName, xSecondName, xThirdName)
        
        initials_married1 = getListOfRemovedMiddleShiftedMarriageNames(initials)
        initials_hyphen = getListOfHyphenatedMarriageNames(initials)
        initials_married = getListOfConventionalMarriageNames(initials)

        if initials_married1 != None:
            for initial in initials_married1:
                if initial in bad:
                    dict1[initial]=[bad[initial],'If he/she marries, drops middle name, and adds married name.']

        for initial in initials_hyphen:
            if initial in bad:
                dict1[initial]=[bad[initial],'If he/she marries and hyphenates married name.']
        
        for initial in initials_married:
            if initial in bad:
                dict1[initial]=[bad[initial],'If he/she marries and takes new surname.']

        # Always show the given initials        
        if initials in bad:
            dict1[initials]=[bad[initials],'These are the given initials.']
        else:
            dict1[initials]=['','These are the given initials.']

        # Show the given monogram if a valid one is returned (need three initials)
        temp = getMonogram(initials)
        if temp != None:
            if temp in bad:
                dict1[temp]=[bad[temp],'This is the monogram for the given name.']
            else:
                dict1[temp]=['','This is the monogram for the given name']

        # Always show 2 to 4 possible email addresses
        dict1[getEmailPattern1(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.']
        
        dict1[getEmailPattern2(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.']
        
        temp = getEmailPattern3(xFirstName, xSecondName, xThirdName, initials)
        if temp != "":
            dict1[temp]=['','This could be a default email address.']
        
        temp = getEmailPattern4(xFirstName, xSecondName, xThirdName, initials)
        if temp != "":
            dict1[temp]=['','This could be a default email address.']
        
        return render.index(namevalue = nameString, dict = dict1)

if __name__ == "__main__":
    app.run()
