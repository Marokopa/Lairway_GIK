from flask import Flask
from threading import Thread
from time import sleep
from github import Github
from LairWay.LWjson import *


app = Flask('')
@app.route('/')
def home():
  return "Lairway Life System Activated"
  
def run():
  app.run(host=FindIp(), port=80)

def LWLS():
  Thread(target=run).start()
  if core["SleepySave"]: Thread(target=SleepySave).start()

def SleepySave():
  while True:
    sleep(60*60*24)
    GHS('data/LW.db')


def GHS(file_name) -> bool:
  try:
    GithubToken, path = FindGithubToken()
    g = Github(GithubToken)
    repo = g.get_repo(path)
    with open(file_name, "rb") as file: content = file.read()
    try:
        old_file = repo.get_contents(file_name)
        repo.update_file(old_file.path, "LairWay-U", content, old_file.sha)
    except:
        repo.create_file(file_name, "LairWay-C", content)
    return True, None
  except Exception as e:
      print("Some GHS Error!")
      return False, e


  