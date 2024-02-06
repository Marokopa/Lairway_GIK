from flask import Flask
from flask import request
from threading import Thread
from time import sleep
from github import Github
import os

LairEyeV="RenderV1"

app = Flask('')
@app.route('/')
def home():
  return "Lairway Life System Activated"
  
def run():
  app.run(host='0.0.0.0', port=80)

def LWLS():
  LWLS = Thread(target=run)
  LWLS.start()
  Git = Thread(target=GitWay)
  Git.start()


def GHS():
    g = Github(os.environ['GitHub'])
    repo = g.get_repo(os.environ['path'])
    with open("LW.db", "rb") as file:
        content = file.read()
    old_file = repo.get_contents("LW.db")
    repo.update_file(old_file.path, "commit message", content, old_file.sha)
    g.close()
    print("Save successful/Сохранение удачно")
    return True
    print("Save failed/Сохранение неудачно")
    return False

def GitWay():
  while True:
    sleep(60*60*24)
    GHS()

