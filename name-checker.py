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
    print "name: " + x

    # Replace hyphens with spaces
    p = re.compile('[-]+')
    xNoHyphen = p.sub(' ', x)

    # Remove non alphabetic characters
    p2 = re.compile('[^a-zA-Z ]*')
    xAlphabetic = p2.sub('', xNoHyphen)
    
    print "name: " + xAlphabetic
        

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
    
    getInitials("'Anne9 Black Cat'")
    getInitials("Program*ming Hi&st-orian")
