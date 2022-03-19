from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def home():  
  return render_template("index.html")


@app.route('/form', methods = ["GET", "POST"])
def bmi_calc():
  bmi =" "
  if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
    weight = float(request.form.get('weight'))
    height = float(request.form.get('height'))
    bmi = round(weight/((height/100)**2),2)
    
    if bmi < 18.5:
      text = f"Risk of developing health problems is increased (underweight)"
    elif bmi >= 18.5 and bmi <= 24.9:
      text = f"Risk of developing health problems is least (normal weight)"
    elif bmi >= 25.0 and bmi <= 29.9:
      text = f"Risk of developing health problems is increased (over weight)"
    elif bmi >= 30.0 and bmi <= 34.9:
      text = f"Risk of developing health problems is high (obese class I)"
    elif bmi >= 35.0 and bmi <= 39.9:
      text = f"Risk of developing health problems is very high (obese class II)"
    elif bmi >= 40.0:
      text = f"Risk of developing health problems is extremely high (obese class III)"
    
    result=bmi
    
    return render_template("index.html", result=result, text=text)

app.run(host='0.0.0.0', port=8080, debug=True)