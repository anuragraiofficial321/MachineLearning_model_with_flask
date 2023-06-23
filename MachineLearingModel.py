from flask import Flask,render_template,request
import joblib
import numpy as np
model=joblib.load("svc.joblib")
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("frontend.html") 

@app.route('/result',methods=['POST'])
def result():
    cgpa=float(request.form.get("CGPA"))
    iq=int(request.form.get("IQ"))
    ps=int(request.form.get("PROFILE_SCORE"))


    resu=model.predict(np.array([cgpa,iq,ps]).reshape(1,3))
    if resu[0]==1:
        resulttext="Placed"
    else:
        resulttext="Not Placed"
    
    return render_template("result.html",result=resulttext)
if __name__=='__main__':
    app.run(debug=True)