import requests;from urllib.parse import quote;import user_agent, re, flask, time# created By @arifi_ios
app = flask.Flask(__name__)
def e(text):
    data_string = f"[[[\"MkEWBc\",\"[[\\\"{text}\\\",\\\"auto\\\",\\\"ar\\\",1,null,2],[]]\",null,\"generic\"]]]" #u can change ar to any language you want
    return "f.req=" + quote(data_string, safe='') + "&"
def T(text):
    s = requests.session()
    s.headers.update({'Host': 'translate.google.com', 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8','Accept-Language': 'en-US,en;q=0.9','User-Agent': user_agent.generate_user_agent()})
    p={'rpcids': '','source-path': '/','f.sid': '','bl': '','hl': 'fr','soc-app': '1','soc-platform': '1','soc-device': '1','_reqid': '','rt': 'c',}
    r1=s.post('https://translate.google.com/_/TranslateWebserverUi/data/batchexecute',params=p)
    print(r1)
    if 'NID' not in r1.cookies:return False
    d=e(text)
    r2 = s.post('https://translate.google.com/_/TranslateWebserverUi/data/batchexecute',params=p,data=d)
    print(r2)
    if r2.status_code == 200:st = re.search(r'\[\[\[null,null,null,null,null,\[\[\\"', r2.text).span()[-1];en = re.search(r'\\",null,null,null,null,null,\\"', r2.text).span()[0];return {'status' : 'success','Real_Text': text, 'Translated_Text' : r2.text[st:en], 'Time' : int(time.time())}
    else:return False
@app.route('/translate')
def to_ar():
    text = flask.request.args.get('q')
    if not text:return flask.jsonify({'status' : '/translate/q=your_text_here'})
    sa=T(text)
    return flask.jsonify(sa) if sa else flask.jsonify({'status':'failed'})
app.run()
