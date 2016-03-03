"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
__appname__ = "name-checker"
__author__  = "David Bradway (dpb6 @ duke)"
__version__ = "0.0pre0"
__license__ = "GNU GPL 3.0 or later"

import re,os
from string import ascii_uppercase
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask import flash, session, g
from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

import names
bad = names.badNames()

import icons
icons = icons.pngNames()

const_GIVEN = 0
const_EMAIL = 1
const_MARRIED = 2

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', ';l123ksdr89_(*HGJF')

def getNames (x):
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

class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])

###
# Routing for your application.
###

@app.before_request
def before_request():
    g.search_form = SearchForm()

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index(page = 1):
    """Render the website's homepage."""
    form = g.search_form
    return render_template('home.html',
                            namevalue = None, 
                            form=form)

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html',
                            namevalue = None)

@app.route('/search', methods=['POST','GET','PUT'])
def search():
    """Receive post data and redirect to Render Results"""
    form = g.search_form
    if not g.search_form.validate_on_submit():
        return redirect(url_for('index'))
    return redirect(url_for('search_results',query=g.search_form.search.data))

@app.route('/search_results/<query>')
def search_results(query):
    dict1 = {}
    nameString = query

    # Parse the input string and return the two or three names (Second name could be 'None;)
    xFirstName, xSecondName, xThirdName = getNames(nameString)

    initials = getInitials(xFirstName, xSecondName, xThirdName)
    initials_married1 = getListOfRemovedMiddleShiftedMarriageNames(initials)
    initials_hyphen = getListOfHyphenatedMarriageNames(initials)
    initials_married = getListOfConventionalMarriageNames(initials)

    if initials_married1 != None:
        for initial in initials_married1:
            if initial in bad:
                if initial in icons:
                    dict1[initial]=[bad[initial],'If he/she marries, drops middle name, and adds married name.',const_MARRIED,icons[initial]]
                else:
                    dict1[initial]=[bad[initial],'If he/she marries, drops middle name, and adds married name.',const_MARRIED,0]

    for initial in initials_hyphen:
        if initial in bad:
            if initial in icons:
                dict1[initial]=[bad[initial],'If he/she marries and hyphenates married name.',const_MARRIED,icons[initial]]
            else:
                dict1[initial]=[bad[initial],'If he/she marries and hyphenates married name.',const_MARRIED,0]

    for initial in initials_married:
        if initial in bad:
            if initial in icons:
                dict1[initial]=[bad[initial],'If he/she marries and takes new surname.',const_MARRIED,icons[initial]]
            else:
                dict1[initial]=[bad[initial],'If he/she marries and takes new surname.',const_MARRIED,0]

    # Always show the given initials
    if initials in bad:
        if initial in icons:
            dict1[initials]=[bad[initials],'These are the given initials.',const_GIVEN,icons[initial]]
        else:
            dict1[initials]=[bad[initials],'These are the given initials.',const_GIVEN,0]
    else:
        if initial in icons:
            dict1[initials]=['','These are the given initials.',const_GIVEN,icons[initial]]
        else:
            dict1[initials]=['','These are the given initials.',const_GIVEN,0]

    # Show the given first and last initials if three names were given
    temp = getInitials2(initials)
    if temp != None:
        if temp in bad:
            if temp in icons:
                dict1[temp]=[bad[temp],'These are the given initials.',const_GIVEN,icons[temp]]
            else:
                dict1[temp]=[bad[temp],'These are the given initials.',const_GIVEN,0]
        else:
            if temp in icons:
                dict1[temp]=['','These are the given initials.',const_GIVEN,icons[temp]]
            else:
                dict1[temp]=['','These are the given initials.',const_GIVEN,0]

    # Show the given monogram if a valid one is returned (need three initials)
    temp = getMonogram(initials)
    if temp != None:
        if temp in bad:
            if temp in icons:
                dict1[temp]=[bad[temp],'This is the monogram for the given name.',const_GIVEN,icons[temp]]
            else:
                dict1[temp]=[bad[temp],'This is the monogram for the given name.',const_GIVEN,0]
        else:
            if temp in icons:
                dict1[temp]=['','This is the monogram for the given name',const_GIVEN,icons[temp]]
            else:
                dict1[temp]=['','This is the monogram for the given name',const_GIVEN,0]

    dict1[getNamePattern1(xFirstName, xThirdName)]=['','Given last name, first name.',const_GIVEN,0]
    dict1[getNamePattern2(xFirstName, initials)]=['','Given first name and last initial.',const_GIVEN,0]

    # Always show 2 to 4 possible email addresses
    dict1[getEmailPattern1(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.',const_EMAIL,0]
    dict1[getEmailPattern2(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.',const_EMAIL,0]

    temp = getEmailPattern3(xFirstName, xSecondName, xThirdName, initials)
    if temp != "":
        dict1[temp]=['','This could be a default email address.',const_EMAIL,0]

    temp = getEmailPattern4(xFirstName, xSecondName, xThirdName, initials)
    if temp != "":
        dict1[temp]=['','This could be a default email address.',const_EMAIL,0]

    dict1[getEmailPattern5(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.',const_EMAIL,0]
    dict1[getEmailPattern6(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.',const_EMAIL,0]
    dict1[getEmailPattern7(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.',const_EMAIL,0]
    dict1[getEmailPattern8(xFirstName, xSecondName, xThirdName, initials)]=['','This could be a default email address.',const_EMAIL,0]

    print nameString
    print dict1

    return render_template('search_results.html',
                               namevalue = nameString,
                               dict = dict1,
                               form = g.search_form)

if __name__ == '__main__':
    app.run(debug=True)
