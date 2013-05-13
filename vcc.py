from bottle import Bottle, run, request,response,static_file,template
import requests
from lxml import etree,objectify

app = Bottle()
auth = ('admin','TANDBERG')
headers = {'Content-type':'text/xml'}

def sendXML(ip,tmpl):
    data = template(tmpl)
    r = requests.post('http://%s/putxml' % ip, headers=headers, auth=auth, data=data)
    return r.text

@app.route('/favicon.ico', method='GET')
def get_favicon():
    return static_file('favicon.ico', root='./static/')

@app.route('/<ip>')
def index(ip):
    req = requests.get('http://%s/getxml?location=/Status' % ip, auth=auth)
    xml = objectify.fromstring(req.content)
    response.content_type = 'text/plain'
    return xml.SystemUnit.Software.Version.text

@app.route('/connect/<ip>')
def connect(ip):
    return sendXML(ip,'connect')

@app.route('/hangup/<ip>')
def hangup(ip):
    return sendXML(ip, 'disconnectall')

run(app,host='0.0.0.0',port='9900',reloader=True)
