from __future__ import with_statement
import calendar
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

DATABASE = '/tmp/calender.db'
DEBUG = True
SECRET_KEY = 'Oscar Key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])



def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_calendar():
    cal = calendar.Calendar()
    days = cal.itermonthdays2(2012,7)
    dates = []
    for day in days:
        dates.append(day)
    print(dates)
    return render_template('show_calendar.html', dates=dates)


#@app.route('/add', methods=['POST'])
#def add_entry():
#    g.db.execute('insert into events (title, datestamp) values (?, ?)', [request.form['title'], request.form['datestamp']])
#    g.db.commit()
#    flash('New entry was successfully posted')
#    return redirect(url_for('show_entries'))


if __name__ == '__main__':    
    app.run()


'''
@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text, id from entries order by id desc')
    entries = [dict(title=row[0], text=row[1], id=row[2]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/edit_entry/<entry_title>', methods=['GET', 'POST'])
def edit_entry(entry_title):
    if not session.get('logged_in'):
        abort(401)
    cur = g.db.execute('select title, text, id from entries where id = ?', [request.args['id']])
    tmp = cur.fetchall()
    if not tmp:
        abort(404)
    tmp = tmp[0]
    entry = dict(title=tmp[0], text=tmp[1], id=tmp[2])
    if request.method == 'POST':
        if not request.form['title']:
            error = 'You must input a title!'
        elif not request.form['text']:
            error = 'You must input a text!'
        else:
            g.db.execute('update entries set text = ?, title = ? where id = ?', [request.form['text'], request.form['title'], entry['id']])
            g.db.commit()
            flash('Entry successfully edited!') 
            return redirect(url_for('show_entries'))
    return render_template('edit_entry.html', entry=entry)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
'''
