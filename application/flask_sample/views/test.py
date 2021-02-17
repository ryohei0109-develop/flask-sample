from flask import request, redirect, url_for, render_template, flash, session
from flask_sample import app

@app.route('/test', methods=['GET', 'POST'])
def show_entries():
    return render_template('test/index.html')
