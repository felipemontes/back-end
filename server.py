from flask import Flask, jsonify, request
import numpy as np

app = Flask(__name__)


@app.route("/", methods=["POST"])
def api():
    json_res = request.get_json()
    rotate = json_res.get('giros')
    matrix = json_res.get('matriz')
    new_matrix = rotate_matrix(matrix, rotate)
    return jsonify(new_matrix)

def rotate_matrix(matrix, rotate):
    np_matrix = np.rot90(matrix, k=rotate, axes=(1,0))
    return np_matrix.tolist()