from bottle import Bottle, run, request,response,static_file,template
import requests
from lxml import etree,objectify

app = Bottle()
auth = ('admin','TANDBERG')
headers = {'Content-type':'text/xml'}
offices = {
'kenora':{'ip':'69.26.70.18','type':'mxp'},
'kenora2':{'ip':'69.26.70.21','type':'mxp'},
'dryden':{'ip':'70.76.112.226', 'type':'c'},
'siouxlookout':{'ip':'70.76.146.59','type':'c'},
'redlake':{'ip':'76.66.221.36','type':'mxp'},
'fortfrances':{'ip':'209','type':'c'}
}

def sendXML(office,tmpl):
    tmpl = tmpl + '_%s' % offices[office]['type']
    data = template(tmpl)
    ip = offices[office]['ip']
    r = requests.post('http://%s/putxml' % ip, headers=headers, auth=auth, data=data)
    return r.text

@app.route('/favicon.ico', method='GET')
def get_favicon():
    return static_file('favicon.ico', root='./static/')

@app.route('/<office>')
def index(office):
    ip = offices[office]['ip']
    req = requests.get('http://%s/getxml?location=/Status' % ip, auth=auth)
    xml = objectify.fromstring(req.content)
    data = dict()
    data['ip'] = xml.Network.IPv4.Address.text
    return template('status', data)

@app.route('/connect/<office>')
def connect(office):
    return sendXML(office,'connect')

@app.route('/hangup/<office>')
def hangup(office):
    return sendXML(office, 'disconnectall')

run(app,host='0.0.0.0',port='9900',reloader=True)
