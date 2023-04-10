from flask import Flask, request, jsonify
from App.database import db
from App.models import document


app = Flask(__name__)


@app.route('/CompiledForm')
def compiled_form():
    return render_template('CompiledForm.html')

@app.route('/App/views/form.py', methods=['POST'])
def handle_form_data():
    data = request.get_json()
    function_name = data.get('function_name')
  
    if function_name == "submitForm":
        doc = document(binary_data=data)
        db.session.add(doc)
        db.session.commit()

        return jsonify({'message': 'Data received successfully!'})
    else:
        return jsonify({'error': 'Invalid function name'})