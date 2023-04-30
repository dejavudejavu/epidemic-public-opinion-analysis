from flask import Flask,request,make_response,jsonify, render_template,send_from_directory
from flask_cors import *
import os

app = Flask(__name__,static_folder='static',static_url_path='')
CORS(app, supports_credentials=True)


@app.route('/',methods=['GET'])
def login():
    return send_from_directory('static','jiayingWeb.html')


@app.route('/receiveFile',methods=['GET','POST'])
def receiveFile():
    print(request.files.get('file'))
    img = request.files.get('file')
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/img')
    if img:
        filepath,fullname = os.path.split(img.filename)
        file_dir = os.path.join(UPLOAD_FOLDER, filepath)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)    
        file_path = os.path.join(file_dir, fullname)                  
        img.save(file_path)                
    return 'ok'

if __name__ == '__main__':
    print('打开http://localhost:8080/')
    app.run(debug=True,host='0.0.0.0',port=8001)#上服务器的时候不要加debug=true