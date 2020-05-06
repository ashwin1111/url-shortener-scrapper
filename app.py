from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import jsonify
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import time as time_
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
timestamp = int(time_.time())


app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route("/get_page_details", methods=["POST","GET"])
def get_page_details():
    try:
        URL = request.args.get('web_address')
        
        page = requests.get(URL)
        print(page)

        soup = BeautifulSoup(page.content, 'html.parser')
        title=[]
        meta_data=[]
        first_ptag=[]
        try:
          for strong_tag in soup.find_all('title'):
              title.append(strong_tag.text)
        except:
          title=[]
        try:
          for strong_tag in soup.find_all('p'):
              first_ptag.append(strong_tag.text)
              break
        except:
          first_ptag=[]
        try:
          metas = soup.find_all('meta')
          for meta in metas:
            if ('name' in meta.attrs and meta.attrs['name'] == 'description'):
              meta_data.append( meta.attrs['content'] )
        except:
          meta_data=[]
        
        return jsonify({'data':{'title':title,'meta_data':meta_data,'first_p_tag':first_ptag}})
    except Exception as e:
        return jsonify({"status": "false"})

  
  





if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0',port=5005)