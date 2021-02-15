"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Kymone Chang")


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/profile')
def profile():
    userData = {
        'profile_url': url_for('static', filename='images/Kymone.jpg'),
        'name': 'Kymone Chang',
        'username': 'Kymone876',
        'locate': 'St Amdrew, Jamaica',
        'joindate': format_date_joined(),
        'bio': "I am final year student at the University of the West Indies Mona (UWI). I work part to help with school tution",
        'noposts': '8',
        'nofollowers': '30',
        'nofollowing': '28'
    }
    
    return render_template('profile.html', userdata = userData);

def format_date_joined():
    setdate = datetime.date(2021,2,2)
    formatdate = setdate.strftime("%B, %Y")
    return formatdate


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
