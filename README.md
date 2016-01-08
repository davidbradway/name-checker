# README

This is a tool to identify if an entered name has any bad initials or email patterns
or if that name could become a problem upon a marriage name change.

## Dependendies

### Linux/Mac

#### Get web.py

    sudo pip install web.py

#### Get and setup authbind if you want to use port 80

Note: change "bitnami" to your user account 

    sudo apt-get install authbind
    sudo touch /etc/authbind/byport/80
    sudo chown bitnami:bitnami /etc/authbind/byport/80
    sudo chmod 755 /etc/authbind/byport/80

#### Get and launch name-checker

    git clone git@gitlab.oit.duke.edu:dpb6/name-checker.git
    cd name-checker/
    authbind --deep python bin/app.py 80 > log.txt 2>&1 & 

Note: If you don't want to use port 80, you can omit authbind and call Python as below

    python bin/app.py > log.txt 2>&1 &


## Reference

[Learn Python the Hard Way tutorials](http://learnpythonthehardway.org/book/ex51.html)

