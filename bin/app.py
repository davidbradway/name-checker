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

const_GIVEN = 0
const_EMAIL = 1
const_MARRIED = 2

bad = names.badNames()

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

def getNames (x):
    #print "Input : " + x

    # Remove leading whitespace
    p = re.compile('^[^a-zA-Z]*')
    # Replace leading non-letters with nothing 
    xNoLeadingWhitespace = p.sub('', x)
        
    # Replace hyphens with spaces
    p2 = re.compile('[-]+')
    xNoHyphen = p2.sub(' ', xNoLeadingWhitespace)
    
    # Remove non alphabetic characters
    p3 = re.compile('[^a-zA-Z ]*')
    # Replace non-(letters or spaces) with nothing
    xAlphabetic = p3.sub('', xNoHyphen)
    #print "Output: " + xAlphabetic

    # Create Regular Expression to look for a three-name pattern
    p4 = re.compile(r'(?P<firstName>\b\w+\b)\s+(?P<secondName>\b\w+\b)\s+(?P<thirdName>\b\w*\b)')
    m = p4.search(xAlphabetic)
    # If a three-name pattern is not matched:
    if m == None:
        #print "matched None, try with no middle name"
        # Create Regular Expression to look for a two-name pattern
        p4 = re.compile(r'(?P<firstName>\b\w+\b)\s+(?P<thirdName>\b\w+\b)')
        m = p4.search(xAlphabetic)
        # set second name to None
        xSecondName = None
    else:
        # Get second name
        xSecondName = m.group('secondName')    
    # Get first name - i.e. Joe
    xFirstName =  m.group('firstName')
    # Get third (last/surname/family) name - i.e. Smith
    xThirdName = m.group('thirdName')

    return xFirstName, xSecondName, xThirdName

def getInitials (xFirstName, xSecondName, xThirdName):
    # Get first initial
    xFirstInitial = getInitialFromName(xFirstName)
    # Get second initial, returns empty string if None
    xSecondInitial = getInitialFromName(xSecondName)
    # Get third initial, returns empty string if None
    xThirdInitial = getInitialFromName(xThirdName)

    # Combine initlals
    initials = xFirstInitial + xSecondInitial + xThirdInitial    
    return initials

def getInitials2 (initials):
    # If a three-name pattern was used, also show just First and Last initials
    if len(initials) == 3:
        return initials[0] + initials[2]
    else:
        return None

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
    # If a three-name pattern was used, also show just First initial plus married initial
    if len(initials) == 3:
        for c in ascii_uppercase:
            # Replace old last name initial  with the new married name initial 
            nameList.append(initials[0] + c)
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
    # If a three-name pattern was used, show First initial plus maiden initial, plus new married initial
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
        initialTemp = p.match(name.upper())
        initial = initialTemp.group()
    return initial

def getNamePattern1 (firstName, thirdName):
    # Show Last name, First name
    return thirdName+", "+firstName

def getNamePattern2 (firstName, initials):
    # Show First name Last initial
    return firstName+" "+initials[-1:]+"."

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

def getEmailPattern5 (firstName, secondName, thirdName, initials):
    return firstName[0:2].lower() + thirdName[0:3].lower()+"@company.com"

def getEmailPattern6 (firstName, secondName, thirdName, initials):
    return firstName[0:2].lower() + thirdName.lower()+"@company.com"

def getEmailPattern7 (firstName, secondName, thirdName, initials):
    return thirdName.lower()+firstName[0:2].lower()+"@company.com"

def getEmailPattern8 (firstName, secondName, thirdName, initials):
    return firstName[0].lower()+thirdName[0:3].lower()+"@company.com"

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
                    dict1[initial]=[bad[initial],'If he/she marries, drops middle name, and adds married name.',const_MARRIED]

        for initial in initials_hyphen:
            if initial in bad:
                dict1[initial]=[bad[initial],'If he/she marries and hyphenates married name.',const_MARRIED]
        
        for initial in initials_married:
            if initial in bad:
                dict1[initial]=[bad[initial],'If he/she marries and takes new surname.',const_MARRIED]

        # Always show the given initials        
        if initials in bad:
            dict1[initials]=[bad[initials],'These are the given initials.',const_GIVEN]

        else:
            dict1[initials]=['','These are the given initials.',const_GIVEN]

        # Show the given first and last initials if three names were given
        temp = getInitials2(initials)
        if temp != None:
            if temp in bad:
                dict1[temp]=[bad[temp],'These are the given initials.',const_GIVEN]
            else:
                dict1[temp]=['','These are the given initials.',const_GIVEN]

        # Show the given monogram if a valid one is returned (need three initials)
        temp = getMonogram(initials)
        if temp != None:
            if temp in bad:
                dict1[temp]=[bad[temp],'This is the monogram for the given name.',const_GIVEN]
            else:
                dict1[temp]=['','This is the monogram for the given name',const_GIVEN]

        dict1[getNamePattern1(xFirstName, xThirdName)]=['','Given last name, first name.',const_GIVEN]

        dict1[getNamePattern2(xFirstName, initials)]=['','Given first name and last initial.',const_GIVEN]

        # Always show 2 to 4 possible email addresses
        dict1[getEmailPattern1(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.',const_EMAIL]
        
        dict1[getEmailPattern2(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.',const_EMAIL]
        
        temp = getEmailPattern3(xFirstName, xSecondName, xThirdName, initials)
        if temp != "":
            dict1[temp]=['','This could be a default email address.',const_EMAIL]
        
        temp = getEmailPattern4(xFirstName, xSecondName, xThirdName, initials)
        if temp != "":
            dict1[temp]=['','This could be a default email address.',const_EMAIL]

        dict1[getEmailPattern5(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.',const_EMAIL]

        dict1[getEmailPattern6(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.',const_EMAIL]

        dict1[getEmailPattern7(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.',const_EMAIL]

        dict1[getEmailPattern8(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.',const_EMAIL]

        return render.index(namevalue = nameString, dict = dict1)

if __name__ == "__main__":
    app.run()
