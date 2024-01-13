from flask import Flask
from flask import request
from threading import Thread
# ФРОМ ГАСАНБЕК ИМПОРТ КОПИРОВАНИЕ (@thebestfriendGAsanBekbot)

app = Flask('')

@app.route('/')
def home():
  return "Lairway Life System Activated"

def run():
  app.run(host='0.0.0.0', port=80)

def keep_alive():
  t = Thread(target=run)
  t.start()