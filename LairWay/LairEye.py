from flask import Flask
from flask import request
from threading import Thread
from time import sleep
from github import Github
import os

LairEyeV="RenderGH-1.0"

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




def GitWay():
  while True:
    sleep(60*60*24)
    GHS('LW.db')


def GHS(file_name):
  try:
    print("\nLairWay Save to GitHub...\n")
    g = Github(os.environ['GitHub'])
    repo = g.get_repo(os.environ['path'])
    with open(file_name, "rb") as file: content = file.read()
    try:
        old_file = repo.get_contents(file_name)
        repo.update_file(old_file.path, "LairWay-U", content, old_file.sha)
    except:
        repo.create_file(file_name, "LairWay-C", content)
  except:
      print("Some GHS Error!")


  