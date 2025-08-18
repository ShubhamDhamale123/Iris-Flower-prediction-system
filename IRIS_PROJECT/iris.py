from flask import Flask,render_template,jsonify,request
import pickle
# import config
import numpy as np
app=Flask(__name__)

with open ("iris_model.pkl","rb") as f:
     model=pickle.load(f)

@app.route("/")
def home():
    print("iris")
    return render_template("iris_project.html")


@app.route("/prediction",methods=['POST',"GET"])
def pred():
    # features = [eval(x) for x in request.form.values()]

    # print(features)
    # final = np.array(features).reshape((1,4))
    # print(final)
    # pred = model.predict(final)[0]
    # print(pred)
 

    test_data=np.zeros(4)
    test_data[0]=request.form["name"]
    test_data[1]=request.form["name1"]
    test_data[2]=request.form["name2"]
    test_data[3]=request.form["name3"]
    
    print(test_data)
    test_data=list(test_data)
    print(test_data)
    print("shubham")
    pred = model.predict([test_data])
    print(pred)
    if pred==0:
        return render_template("iris_setosa.html")
    elif pred==1:
        return render_template("iris_versicolor.html")
    else:
        return render_template("iris_virginica.html")

     
    # return render_template("success.html", pred=f'Expected amount is :{pred}'.format(pred))
if __name__=="__main__":
    app.run(host="0.0.0.0",port=2005,debug=True)
