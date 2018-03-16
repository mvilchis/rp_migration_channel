from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from utils import *
import os
import ast
from flask import jsonify
app = FlaskAPI(__name__)

@app.route("/by_id", methods=['GET'])
def get_user_by_id_view():
    id_user = request.args.get('id')
    json_user= get_user_by_id(id_user)
    return jsonify(json_user)

@app.route("/by_phone", methods=['GET'])
def get_user_by_phone_view():
    phone_user = request.args.get('phone')
    json_user= get_user_by_phone(phone_user)
    return jsonify(json_user)


if __name__ == "__main__":
    #Cambiar ip a 0.0.0.0
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True,host="0.0.0.0", port= int(os.getenv('WEBHOOK_PORT', 5000)))
