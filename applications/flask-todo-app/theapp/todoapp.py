from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://faisalm:mypasswd@localhost/todoapp'

from views import *

if __name__ == '__main__':
    app.run()
    