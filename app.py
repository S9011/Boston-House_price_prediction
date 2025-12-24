from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
       
        features = [
            float(request.form.get('CRIM', 0)),
            float(request.form.get('ZN', 0)),
            float(request.form.get('INDUS', 0)),
            float(request.form.get('CHAS', 0)),
            float(request.form.get('NOX', 0)),
            float(request.form.get('RM', 0)),
            float(request.form.get('AGE', 0)),
            float(request.form.get('DIS', 0)),
            float(request.form.get('RAD', 0)),
            float(request.form.get('TAX', 0)),
            float(request.form.get('PTRATIO', 0)),
            float(request.form.get('BLACK', 0)),
            float(request.form.get('LSTAT', 0))
        ]

        # Dummy prediction (instead of using the real model)
        output = round(np.random.uniform(10, 50), 2)  

        return render_template('index.html', prediction_text=f'🏠 Predicted House Price: ${output}k')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
