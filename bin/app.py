# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 20:52:29 2016

pip install lpthw.web

@author: David
"""
import web

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        form = web.input(name="Nobody")
        greeting = "Hello, %s" % form.name

        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
    