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
    
    #client = secretmanager.SecretManagerServiceClient()
    
    #name = "projects/655129271851/secrets/compute-api-key/versions/1"
    #response = client.access_secret_version(name=name)
    
    return "ya29.a0AfB_byA0FtIs6QpyjW8mhXuStxsVedK1j2Pz0sGMi93f2wO1VtIrawq_kG-qWDaVCw4XAurmxE3Ot680xVjXoAF5VDMk1sEZoJaZGUDTvL5rqRvbwahbSaf9GWPQIClxICjgg-QVvPW6sQCkaPrKQxMwFQ_Xv-LlOzR314BKC9FrHju31douPfpu30oNFpVAMxQkLjtbdETcJTMjXKZU2d2QeC8oxQ0Jbh0DvpmDtim1c0lGEhPgjdp-2CoHicMbfHqqxdeUxxqL9g-sp4QVEevMCiZeqZRfF_diWhDcYGhTVKMyoODN-vBnbqYMC64ePEFVHu9X2DuG10ItQDcy_mBF5bOG21o1rtOGig3cYPHTPRcA1-uUQt6gjinhMX9ntvtVy_x69PQK-Sm6leSpFlgK8hOlH0EaCgYKASwSARMSFQHGX2MizTFRA9z9x7fiv41yt1QO_Q0422"
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
    return "Use post to add" # replace with form template
  else:
    token=get_api_key()
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
