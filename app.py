
from config import Config
from flask import Flask
from flask_graphql import GraphQLView
from query import schema
from schema import db
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
    init_db()
    return "User added successfully!"
  
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run()
    