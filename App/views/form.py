from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from App.database import db
from App.models import document
from App.maker import *

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = "sqlite:///temp-database.db"
db = SQLAlchemy(app)

@app.route('/CompiledForm', methods=['POST'])
def compiled_form():
    handle_form_data()
    return render_template('CompiledForm.html')

def handle_form_data():
    data = request.get_json()
    function_name = data.get('function_name')

    if function_name == "submitForm":
        formdata = writeDoc(data)
        doc = document(binary_data=formdata)
        doc = document(binary_data=data.get('data'))
        db.session.add(doc)
        db.session.commit()

        return jsonify({'message': 'Data received successfully!'})
    else:
        return jsonify({'error': 'Invalid function name'})

