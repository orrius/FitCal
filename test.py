from __future__ import with_statement
import calendar
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

DEBUG = True


app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/')
def show_test():
    return render_template('test.html')
    


if __name__ == '__main__':    
    app.run()
