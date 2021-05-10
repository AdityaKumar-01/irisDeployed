from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

model = pickle.load(open('iris.pkl','rb'))

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    d = request.form['d']
    final_features = np.array([[a,b,c,d]])
    prediction = model.predict(final_features)
    
    output = prediction[0]
    #output = "Aditya"
    
    return render_template('index.html', prediction_text = f"{output} ")
if __name__ == '__main__':
    app.run(debug=True, port=8000)