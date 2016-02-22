#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 21:11:43 2015

@author: David Bradway
"""
__appname__ = "name-checker"
__author__  = "David Bradway (dpb6 @ duke)"
__version__ = "0.0pre0"
__license__ = "GNU GPL 3.0 or later"

import re
from string import ascii_uppercase
import names
bad = names.badNames()
import app


if __name__ == '__main__':

    in1 = "   Henrietta Inga Vance"
    print in1
    xFirstName, xSecondName, xThirdName = app.getNames(in1) 
    initials1 = app.getInitials(xFirstName, xSecondName, xThirdName)
    initials_married1 = app.getListOfRemovedMiddleShiftedMarriageNames(initials1)

    #print initials1
    if initials1 in bad:
        print "bad: " + initials1 + bad[initials1]

    """
    in2 = "Francine9 Anne Smith"
    print in2
    initials2 = app.getInitials(in2)
    #print initials2    
    if initials2 in bad:
        print "bad: " + initials2 + bad[initials2]
    initials2_married = app.getListOfConventionalMarriageNames(initials2);
    for initial in initials2_married:
        if initial in bad:
            print "bad: " + initial + bad[initial]

    initials2_hyphen = app.getListOfHyphenatedMarriageNames(initials2);
    for initial in initials2_hyphen:
        if initial in bad:
            print "bad: " + initial + bad[initial]
    
    initials2_married = app.getListOfRemovedMiddleShiftedMarriageNames(initials2);
    for initial in initials2_married:
        if initial in bad:
            print "bad: " + initial + bad[initial]
            
    in3 = "Frank Germane Arts"
    print in3
    print app.getEmailPattern1(in3)

    initials3 = app.getInitials(in3)
    #print initials3
    if initials3 in bad:
        print "bad: " + initials3 + bad[initials3]
    initials3_married = app.getListOfConventionalMarriageNames(initials3);
    for initial in initials3_married:
        if initial in bad:
            print "bad: " + initial + bad[initial]

    initials3_hyphen = app.getListOfHyphenatedMarriageNames(initials3);
    for initial in initials3_hyphen:
        if initial in bad:
            print "bad: " + initial + bad[initial]
    
    initials3_married = app.getListOfRemovedMiddleShiftedMarriageNames(initials3);
    for initial in initials3_married:
        if initial in bad:
            print "bad: " + initial + bad[initial]
    
    in4 = "   Brandy      Anderson-Damon"
    print in4
    initials4 = app.getInitials(in4)
    #print initials4
    #print getListOfConventionalMarriageNames(initials4)
    #print getListOfHyphenatedMarriageNames(initials4)
    #print getListOfRemovedMiddleShiftedMarriageNames(initials4)
    if initials4 in bad:
        print "bad: " + initials4 + bad[initials4]
    initials4_married = app.getListOfConventionalMarriageNames(initials4);
    for initial in initials4_married:
        if initial in bad:
            print "bad: " + initial + bad[initial]

    initials4_hyphen = app.getListOfHyphenatedMarriageNames(initials4);
    for initial in initials4_hyphen:
        if initial in bad:
            print "bad: " + initial + bad[initial]
    
    initials4_married = app.getListOfRemovedMiddleShiftedMarriageNames(initials4);
    for initial in initials4_married:
        if initial in bad:
            print "bad: " + initial + bad[initial]
    
    in5 = "Ishmael Naz"
    print in5
    firstName, secondName, thirdName = app.getNames(in5)
    print app.getEmailPattern2(in5)
    """
    
    dict1 = {}

    nameString = "Sylvia Elizabth Xi"

    xFirstName, xSecondName, xThirdName = app.getNames(nameString) 
    initials = app.getInitials(xFirstName, xSecondName, xThirdName)

    initials_married1 = app.getListOfRemovedMiddleShiftedMarriageNames(initials)

    # Parse the input string and return the two or three names (Second name could be 'None;)
    initials_hyphen = app.getListOfHyphenatedMarriageNames(initials)
    initials_married = app.getListOfConventionalMarriageNames(initials)

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
    # Show the given first and last initials if three names were given
    temp = app.getInitials2(initials)
    if temp != None:
        if temp in bad:
            dict1[temp]=[bad[temp],'These are the given initials.']
        else:
            dict1[temp]=['','These are the given initials.']
    # Show the given monogram if a valid one is returned (need three initials)
    temp = app.getMonogram(initials)
    if temp != None:
        if temp in bad:
            dict1[temp]=[bad[temp],'This is the monogram for the given name.']
        else:
            dict1[temp]=['','This is the monogram for the given name']
    dict1[app.getNamePattern1(xFirstName, xThirdName)]=['','Given last name, first name.']
    # Always show 2 to 4 possible email addresses
    dict1[app.getEmailPattern1(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.']    
    dict1[app.getEmailPattern2(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.']    
    temp = app.getEmailPattern3(xFirstName, xSecondName, xThirdName, initials)
    if temp != "":
        dict1[temp]=['','This could be a default email address.']    
    temp = app.getEmailPattern4(xFirstName, xSecondName, xThirdName, initials)
    if temp != "":
        dict1[temp]=['','This could be a default email address.']
    dict1[app.getEmailPattern5(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.']
    dict1[app.getEmailPattern6(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.']
    dict1[app.getEmailPattern7(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.']

    print dict1    
