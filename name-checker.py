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

import logging
log = logging.getLogger(__name__)

import re

from string import ascii_uppercase

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

    p4 = re.compile(r'(?P<firstName>\b\w+\b)\s+(?P<secondName>\b\w+\b)\s+(?P<thirdName>\b\w+\b)')
    m = p4.search(xAlphabetic)
    # Get first name
    xFirstName =  m.group('firstName')
    # Get second name
    xSecondName = m.group('secondName')    
    # Get third name
    xThirdName = m.group('thirdName')

    return xFirstName, xSecondName, xThirdName

def getInitials (x):
    xFirstName, xSecondName, xThirdName = getNames(x)
    
    # Get first initial
    xFirstInitial = getInitialFromName(xFirstName)
    # Get second initial
    xSecondInitial = getInitialFromName(xSecondName)
    # Get third initial
    xThirdInitial = getInitialFromName(xThirdName)

    # Combine initlals
    initials = xFirstInitial + xSecondInitial + xThirdInitial    
    return initials

def getListOfConventionalMarriageNames (initials):
    nameList = []
    for c in ascii_uppercase:
        nameList.append(initials[:-1] + c)
    return nameList
    
def getListOfHyphenatedMarriageNames (initials):
    nameList = []
    for c in ascii_uppercase:
        nameList.append(initials + c)
    return nameList
    
def getListOfRemovedMiddleShiftedMarriageNames (initials):
    nameList = []
    for c in ascii_uppercase:
        nameList.append(initials[0:1] + initials[-1:] + c)
    return nameList

def getInitialFromName (name):
    # Get initial
    p = re.compile('^[a-zA-Z]')
    initialTemp = p.match(name)
    initial = initialTemp.group()
    return initial

def getEmailPattern1 (x):
    firstName, secondName, thirdName = getNames(x)
    initials = getInitials(x)
    return initials[0:1]+thirdName+"@company.com"

def getEmailPattern2 (x):
    firstName, secondName, thirdName = getNames(x)
    initials = getInitials(x)
    return thirdName+initials[0:1]+"@company.com"

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser(version="%%prog v%s" % __version__,
            usage="%prog [options] <argument> ...",
            description=__doc__.replace('\r\n', '\n').split('\n--snip--\n')[0])
    parser.add_option('-v', '--verbose', action="count", dest="verbose",
        default=2, help="Increase the verbosity. Use twice for extra effect")
    parser.add_option('-q', '--quiet', action="count", dest="quiet",
        default=0, help="Decrease the verbosity. Use twice for extra effect")
    #Reminder: %default can be used in help strings.

    # Allow pre-formatted descriptions
    parser.formatter.format_description = lambda description: description

    opts, args  = parser.parse_args()

    # Set up clean logging to stderr
    log_levels = [logging.CRITICAL, logging.ERROR, logging.WARNING,
                  logging.INFO, logging.DEBUG]
    opts.verbose = min(opts.verbose - opts.quiet, len(log_levels) - 1)
    opts.verbose = max(opts.verbose, 0)
    logging.basicConfig(level=log_levels[opts.verbose],
                        format='%(levelname)s: %(message)s')
    
    in1 = "   Henrietta Inga Vance"
    print in1
    initials1 = getInitials(in1)
    print initials1

    in2 = "Francine9 Anne Smith"
    print in2
    initials2 = getInitials(in2)
    print initials2    
    
    in3 = "Frank Germane Arts"
    print in3
    print getEmailPattern1(in3)
    print getEmailPattern2(in3)
    initials3 = getInitials(in3)
    print initials3

    in4 = "   Brandy      Anderson-Damon"
    print in4
    initials4 = getInitials(in4)
    print initials4
    print getListOfConventionalMarriageNames(initials4)
    print getListOfHyphenatedMarriageNames(initials4)
    print getListOfRemovedMiddleShiftedMarriageNames(initials4)
    
