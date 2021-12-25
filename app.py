
from flask import Flask, render_template, request
import age_model

app = Flask(__name__)




@app.route('/',methods=['GET'])
def homePage():
    return render_template("index.html")

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        age=float(request.form['age'])
        prediction = age_model.bmi_prediction(age)
        output = round(prediction[0], 2)
        print('prediction is = ', output)

    return render_template('index.html', pred = output )



if __name__ == "__main__":
    app.run( debug = True , port = 8000)
