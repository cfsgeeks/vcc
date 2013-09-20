from bottle import Bottle, run, request,response,static_file,template
import requests
from lxml import etree,objectify
import time

app = Bottle()
auth = ('admin','TANDBERG')
headers = {'Content-type':'text/xml'}
offices = {
'kenora':{'ip':'69.26.70.18','type':'mxp'},
'kenora2':{'ip':'69.26.70.21','type':'mxp'},
'dryden':{'ip':'70.76.112.50', 'type':'c'},
'siouxlookout':{'ip':'70.76.146.59','type':'c'},
'redlake':{'ip':'76.66.221.36','type':'mxp'},
'fortfrances':{'ip':'209.91.170.102','type':'mxp'},
'fortfrances2':{'ip':'209.91.170.54','type':'mxp'},
'atikokan':{'ip':'184.69.51.50','type':'mxp'}
}

def sendXML(office,tmpl,meeting="000000000",code="0000"):
    tmpl = tmpl + '_%s' % offices[office]['type']
    data = template(tmpl, {'meeting':meeting, 'code':code})
    ip = offices[office]['ip']
    r = requests.post('http://%s/putxml' % ip, headers=headers, auth=auth, data=data)
    return r.text

@app.route('/favicon.ico', method='GET')
def get_favicon():
    return static_file('favicon.ico', root='./static/')

@app.route('/<office>')
def index(office):
    ip = offices[office]['ip']
    vctype = offices[office]['type']
    req = requests.get('http://%s/getxml?location=/Status' % ip, auth=auth)
    xml = objectify.fromstring(req.content)
    data = dict()
    data['ip'] = xml.Network.IPv4.Address.text
    return template('status_'+'%s' % vctype, data)

@app.route('/connect/<office>')
def connect(office):
    return sendXML(office,'connect')

@app.route('/hangup/<office>')
def hangup(office):
    return sendXML(office, 'disconnectall')

@app.route('/join/<meeting>/<office>')
def join_meeting(meeting,office):
    return sendXML(office,'join_meeting',meeting)

@app.route('/join/<meeting>/<code>/<office>')
def join_meeting(meeting,office,meeting,code):
    return sendXML(office,'join_meeting',meeting,code)

run(app,host='0.0.0.0',port='9900',reloader=True)
