from captcha.image import ImageCaptcha
import random
from flask import Flask, request, redirect, url_for
import time

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def index():
  global num1
  if request.method=="GET":
    print("this is executing")
    num = random.randint(1000,9999)
    image = ImageCaptcha()
    data = image.generate(str(num))
    tstr = time.strftime("%Y%m%d-%H%M%S")
    image.write(str(num), f'./static/{tstr}.png')
    num1 = num
    return f'''
    <form method="POST">
    <img src="./static/{tstr}.png">
    <input type="text" name="ip">
    <button type"submit">submit</button>
    '''
  elif request.method=="POST":
    ip = request.form["ip"]
    if int(ip)==int(num1):
      return '{"status":Success}'
    else:
      return redirect(url_for(".index"))

if __name__=="__main__":
  app.debug=True
  app.run(host="0.0.0.0",threaded=True,use_reloader=True)
