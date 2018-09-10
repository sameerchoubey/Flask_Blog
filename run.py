from flaskblog import create_app
from flask import render_template, url_for, flash, redirect

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)