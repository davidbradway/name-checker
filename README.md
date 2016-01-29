# README

This is a tool to identify if an entered name has any bad initials or email patterns
or if that name could become a problem upon a marriage name change.

## Get name-checker

Download a snapshot: `https://gitlab.oit.duke.edu/dpb6/name-checker/repository/archive.zip`

Or:
    git clone git@gitlab.oit.duke.edu:dpb6/name-checker.git
    cd name-checker/

## Setup

In the installer script, change "bitnami" to your user account and decide if you want to use authbind.

Then run the install script:
    
    sh install.sh

## Try it out 
### On port 80, if you set up authbind

    authbind --deep python bin/app.py 80 > log.txt 2>&1 & 

### Or debug server on port 8080

Omit authbind and call Python as below:

    python bin/app.py > log.txt 2>&1 &

Go to the appropriate webpage depending on the port you selected:

- http://localhost:8080

- http://localhost:80

## Reference

[Learn Python the Hard Way tutorials](http://learnpythonthehardway.org/book/ex51.html)
