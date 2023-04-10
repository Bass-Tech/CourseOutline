from flask import Flask, request, jsonify, render_template
from App.database import db
from App.models import document
from maker.py import *


app = Flask(__name__)

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

