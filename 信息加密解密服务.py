from flask import Flask,render_template,request
from flask_wtf.csrf import CSRFProtect
from Crypto.Cipher import AES
import base64,codecs
app = Flask(__name__)
app.secret_key = b'google123'
CSRFProtect(app)
@app.route('/jiemi',methods=['GET', 'POST'])
def jm():
    if request.method == 'POST':
        key=str(request.form['key'])
        sjm=str(request.form['sjm'])
        word=str(request.form['word'])
        new_bytes = bytes(word[2:-1], encoding="utf-8")
        ciphertext = codecs.escape_decode(new_bytes, "hex-escape")[0]
        key=key.encode()
        sjm=sjm.encode()
        try:
            cipher = AES.new(key, AES.MODE_EAX, nonce=sjm)
            plaintext = cipher.decrypt(ciphertext)
        except:
            return "传入参数错误"
        try:
            xxx=str(plaintext.decode())
        except:
            return "无法完成解密"
        return render_template("jiemi.html",xxx=str(plaintext.decode()))
    else:
        return render_template("jiemi.html")
@app.route('/jiami',methods=['GET', 'POST'])
def jm2():
    if request.method == 'POST':
        key=str(request.form['key'])
        sjm=str(request.form['sjm'])
        word=str(request.form['word'])
        ciphertext=word.encode('utf-8','strict')
        key = key.encode()
        sjm = bytes(sjm,encoding="utf-8")
        sjm = codecs.escape_decode(sjm, "hex-escape")[0]
        try:
            cipher = AES.new(key, AES.MODE_EAX,nonce=sjm)
            ciphertext, tag = cipher.encrypt_and_digest(ciphertext)
            return render_template("jiami.html",xxx=str(ciphertext))
        except:
            return "传入参数格式错误"
    else:
        return render_template("jiami.html")
@app.route("/")
def zhu():
    return render_template("index.html")
@app.errorhandler(404)
def page_not_found(e):
    return "404"
@app.errorhandler(500)
def page_not_found(e):
    return "你输入有误,无法完成运算!"
if __name__=='__main__':
    app.run(host="0.0.0.0",port=8080,debug=True,ssl_context=('1.crt','1.key'))
        
    
