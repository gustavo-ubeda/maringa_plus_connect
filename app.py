#https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask
import requests
app = Flask(__name__)

@app.route('/<string:id>&<string:id2>')
def hello_world(id, id2):
    envio = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSffkPZfyY722D8Tit54xgWEMkh2WzIqMLIk8TOY5SZm4ul5Mg/formResponse?usp=pp_url&entry.1803429885='+id+id2+'&submit=Submit'
    requests.get(envio)
    return envio

if __name__ == "__main__":
  debug = True
  app.run(debug=debug) #app.run(host='0.0.0.0', port=5000, debug=debug)