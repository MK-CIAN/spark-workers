from flask import Flask
from flask import request
import requests
import os
import json
from google.cloud import secretmanager
app = Flask(__name__)

def get_api_key() -> str:
    #secret = os.environ.get("compute-api-key ")
    #project_id = "655129271851"
    #secret_id = "compute-api-key"
    
    client = secretmanager.SecretManagerServiceClient()
    
    name = "projects/655129271851/secrets/compute-api-key"
    response = client.access_secret_version(name=name)
    
    return response.payload.data.decode("UTF-8")
    # if secret:
    #     return secret
    # else:
    #     #local testing
    #     with open('.key') as f:
    #         return f.read()
      
@app.route("/")
def hello():
    return "Add workers to the Spark cluster with a POST request to add"

@app.route("/test")
def test():
    #return "Test" # testing 
    return(get_api_key())

@app.route("/add",methods=['GET','POST'])
def add():
  if request.method=='GET':
    return render_template('index.html')
  else:
    token=access_secret_version("compute-api-key")
    ret = addWorker(token,request.form['num'])
    return ret

def addWorker(token, num):
    with open('payload.json') as p:
      tdata=json.load(p)
    tdata['name']='slave'+str(num)
    data=json.dumps(tdata)
    url='https://www.googleapis.com/compute/v1/projects/even-trainer-401512/zones/europe-west1-b/instances'
    headers={"Authorization": "Bearer "+token}
    resp=requests.post(url,headers=headers, data=data)
    if resp.status_code==200:     
      return "Done"
    else:
      print(resp.content)
      return "Error\n"+resp.content.decode('utf-8') + '\n\n\n'+data



if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
