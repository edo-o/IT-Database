from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///solutions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Solution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    problem = db.Column(db.String(500), nullable=False)
    solution = db.Column(db.Text, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    search_query = request.form.get("search", "")
    solutions = Solution.query.filter(Solution.problem.contains(search_query)).all()
    return render_template("index.html", solutions=solutions, search_query=search_query)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)

#TEST DATA

#with app.app_context():
... #    s1 = Solution(problem="No sound on laptop", solution="restart")
...  #   s2 = Solution(problem="Wifi not working", solution="restart")
... #    db.session.add(s1)
... #    db.session.add(s2)
...   #  db.session.commit()
...   #  print("test data added successfully!)
