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

def getInitials (x):
    print "Input : " + x

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
    
    # Get first name
    p4 = re.compile('[ ]+[a-zA-Z ]*')
    xFirstName = p4.sub('', xAlphabetic)
    print "FirstName : " + xFirstName

    # Get second name
    # first, remove first name
    p5 = re.compile('^[a-zA-Z]+[ ]+')
    xNoFirstName = p5.sub('', xAlphabetic)
    #print "NoFirst: " + xNoFirstName
    # then, remove everything after what is now first remaining name
    p6 = re.compile('^[ ]+')
    xNoSpacesBeforeSecondName = p6.sub('', xNoFirstName)
    #print "NoSpacesBeforeSecondName: " + xNoSpacesBeforeSecondName
    p7 = re.compile('[ ]+[a-zA-Z]+')
    xSecondName = p7.sub('', xNoSpacesBeforeSecondName)
    print "SecondName: " + xSecondName
    
    # Get third name
    # remove what is now first remaining name
    p8 = re.compile('[a-zA-Z]+[ ]+')
    xThirdName = p8.sub('', xNoSpacesBeforeSecondName)
    print "ThirdName : " + xThirdName

    # Get first initial
    p9 = re.compile('^[a-zA-Z]')
    xFirstInitialtemp = p9.match(xFirstName)
    xFirstInitial = xFirstInitialtemp.group()
    print "FirstInitial : " + xFirstInitial

    # Get second initial
    p10 = re.compile('^[a-zA-Z]')
    xSecondInitialtemp = p10.match(xSecondName)
    xSecondInitial = xSecondInitialtemp.group()
    print "SecondInitial: " + xSecondInitial

    # Get third initial
    p11 = re.compile('^[a-zA-Z]')
    xThirdInitialtemp = p11.match(xThirdName)
    xThirdInitial = xThirdInitialtemp.group()
    print "ThirdInitial: " + xThirdInitial

    # Combine initlals
    initials = xFirstInitial + xSecondInitial + xThirdInitial    
    return initials

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
    
    i1 = getInitials("   Anne Black Cat")
    print i1
    i2 = getInitials("Anne9 Black Cat")
    print i2
    i3 = getInitials("Programming Hist-orian")
    print i3
    i4 = getInitials("   Anne      Black Cat")
    print i4
