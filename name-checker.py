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
    
    intials1 = getInitials("   Anne Black Cat")
    print intials1
    intials2 = getInitials("Anne9 Black Cat")
    print intials2
    intials3 = getInitials("Programming Hist-orian")
    print intials3
    intials4 = getInitials("   Anne      Black Cat")
    print intials4
