import pickle
import numpy as np
from flask import Flask
from flask import request
from flask import jsonify


model_file = 'house_price_model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask("price")

@app.route("/predict", methods=["POST"])

def predict():
    house = request.get_json()
    X = dv.transform([house])
    y_pred = np.expm1(model.predict(X)).tolist()

    result = {
        'predicted price': y_pred
    }

    return jsonify(result)


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=9696)