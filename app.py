from flask import Flask, request, render_template
from src.CreditCard.pipeline.Prediction_pipeline import CustomData, PredictPipeline

app = Flask(__name__)



# Define the home route

@app.route("/",methods=["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")
    
    else:
        data=CustomData (   
        LIMIT_BAL=float(request.form.get("LIMIT_BAL")),
        SEX=int(request.form.get("SEX")),
        EDUCATION=int(request.form.get("EDUCATION")),
        MARRIAGE=int(request.form.get("MARRIAGE")),
        AGE=int(request.form.get("AGE")),
        PAY_SEPT=int(request.form.get("PAY_SEPT")),
        PAY_AUG =int(request.form.get('PAY_AUG')),
        PAY_JUL=int(request.form.get("PAY_JUL")),
        PAY_JUN=int(request.form.get("PAY_JUN")),
        PAY_MAY=int(request.form.get("PAY_MAY")),
        PAY_APR=int(request.form.get("PAY_APR")),
        BILL_AMT_SEPT=float(request.form.get("BILL_AMT_SEPT")),
        BILL_AMT_AUG=float(request.form.get("BILL_AMT_AUG")),
        BILL_AMT_JUL=float(request.form.get("BILL_AMT_JUL")),
        BILL_AMT_JUN =float(request.form.get('BILL_AMT_JUN')),
        BILL_AMT_MAY=float(request.form.get("BILL_AMT_MAY")),
        BILL_AMT_APR=float(request.form.get("BILL_AMT_APR")),
        PAY_AMT_SEPT=float(request.form.get("PAY_AMT_SEPT")),
        PAY_AMT_AUG=float(request.form.get("PAY_AMT_AUG")),
        PAY_AMT_JUL=float(request.form.get("PAY_AMT_JUL")),
        PAY_AMT_JUN=float(request.form.get("PAY_AMT_JUN")),
        PAY_AMT_MAY=float(request.form.get("PAY_AMT_MAY")),
        PAY_AMT_APR = float(request.form.get('PAY_AMT_APR'))
        )
            
            
        # this is my final data
        final_data=data.get_data_as_dataframe()
        
        predict_pipeline=PredictPipeline()
        
        pred=predict_pipeline.predict(final_data)
        
        result=round(pred[0],2)
        #if pred[0]==1:
                #result ='Person is not Healthy as suffering with Kidney Disease'
                
        #else:
               # result='Person is Healthy, Do not have Kidney Disease'
        
        return render_template("result.html",final_result=result)
     
        
@app.route('/about', methods=['GET', 'POST'])
def about():

    return render_template('about.html')  

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return render_template('result.html')  
    

#execution begin
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)           