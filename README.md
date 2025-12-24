# Boston Housing Price Prediction

A **Flask web app** to predict Boston housing prices.  
Currently, it uses a **dummy prediction model** (random values) but is ready to integrate a trained machine learning model.



## Features

- Modern and responsive **UI design** with gradient background.  
- Input fields for **all Boston Housing dataset features**:  
  CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, BLACK, LSTAT  
- Dropdown for **CHAS** (0 or 1).  
- Clean **prediction result display** in a green box.  
- Fully functional **Flask backend**.

## Screenshots

**Form Page**
(screenshots/form.png)

**Prediction Result**
(screenshots/result.png)


## Folder Structure
House_price_pprediction/
├── app.py
├── templates/
│ └── index.html
├── static/
│ └── style.css
├── screenshots/
│ ├── form.png
│ └── result.png
├── requirements.txt
├── house_price_prediction.pkl (optional real model)
└── README.md

## Usage

1. Fill in all fields in the form.  
2. Click **Predict Price**.  
3. The predicted house price appears below the form.

> Currently, prediction is random. To use a real model, place `boston_model.pkl` in the project folder and update `app.py`.


## Optional: Using a Real Model

import pickle
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()
X = boston.data
y = boston.target

model = LinearRegression()
model.fit(X, y)

with open('boston_model.pkl', 'wb') as f:
    pickle.dump(model, f)

License
This project is open source and free to use.

Author
Shivani Ghadge
GitHub Profile

Project Repository




### ✅ Next steps

1. Create a file in your project folder called `README.md`.  
2. Paste this full content and save.  
3. Optional: Add screenshots in a `screenshots/` folder (`form.png` and `result.png`).  
4. Commit and push to GitHub:

git add README.md screenshots/
git commit -m "Add final README with Author links and screenshots placeholders"
git push
