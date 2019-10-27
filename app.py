from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
cors= CORS(app)
app.config['CORS_HEADERS']= 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
db = SQLAlchemy(app)

class HGame(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	keyPress = db.Column(db.String(20), nullable=False)
	started = db.Column(db.DateTime)
	count = db.Column(db.Integer, default= 1)
	player = db.Column(db.Boolean, nullable=False)

	def __repr__(self):
		return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():
	if request.method == 'POST':
		req_data = request.get_json()
		now = datetime.strptime(req_data['started'], "%Y-%m-%dT%H:%M:%S.%fZ")
		task_keyPress = req_data['keyPress']
		task_started = req_data['started']
		task_count = req_data['count']
		task_player = req_data['player']

		new_task = HGame(keyPress= task_keyPress, count= task_count, started=now, player= task_player)

		try: 
			db.session.add(new_task)
			db.session.commit()
			return "success"
		except:
			return 'There was an issue adding your task'

	else:
		tasks = db.session.query(HGame).order_by(HGame.started).all()
		result= []
		for task in tasks:
			result.append([task.keyPress, task.started, task.count, task.player])
		# print(json.dumps(tasks))
		return jsonify(result)
		# return render_template('index.html', tasks= tasks)

@app.route('/delete', methods=['GET'])
def delete():
	try: 
		db.session.query(HGame).delete()
		db.session.commit()
		return "success"
	except:
		return 'There was a problem deleting that task'

@app.route('/select/<int:id>', methods=['GET'])
def select(id):
		tasks = db.session.query(HGame).filter(HGame.id> id).order_by(HGame.started).all()
		result= []
		for task in tasks:
			result.append([task.keyPress, task.started, task.count, task.player])
		return jsonify(result)


if __name__ == "__main__":
	app.run(debug=True)
