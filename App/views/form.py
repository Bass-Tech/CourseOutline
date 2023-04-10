from flask import Flask, request, jsonify
from App.database import db
from App.models import document


app = Flask(__name__)


@app.route('/CompiledForm', methods=['POST'])
def compiled_form():
    return render_template('CompiledForm.html')

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

