from flask import Flask
from flask_script import Manager
from flask_script import Server
import jinja2
from jinja2 import Environment, PackageLoader
import requests

app = Flask(__name__)

templateLoader = jinja2.FileSystemLoader(searchpath=".")
env = Environment(loader=templateLoader)

@app.route('/search')
def hello_world():
    template = env.get_template('mytemplate.html')

    response = requests.get('http://127.0.0.1:8000/search.json')
    data = response.json()

    markup = template.render(data=data)
    return markup


manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=9000))

if __name__ == '__main__':
    manager.run()