
from config import Config
import os
from flask import Flask
from flask_graphql import GraphQLView
from app_schema import schema
from models import db
from dataset import init_db

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)

# Initialize the MongoEngine connection
db.init_app(app)

default_query = '''
{
  allEmployees {
    edges {
      node {
        id,
        name,
        department {
          id,
          name
        },
        role {
          id,
          name
        }
      }
    }
  }
}'''.strip()

@app.route('/add_data')
def add_user():
    if os.getenv("ENV")=='dev':
      init_db()
      return "Data added successfully"
    return "Data for production environment not required!"
  
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()
    