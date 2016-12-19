from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hey_mama():
    # return 'Hey mama! <p><a href="/start">Begin application</a></p>'
    return render_template('govuk_template.html', asset_path='http://localhost:9999/assets/')

@app.route('/start')
def begin_request():
    return 'So you want to request for an assessment?'


# /assets/stylesheets/govuk-template.css
