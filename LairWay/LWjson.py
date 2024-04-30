import json, os

def JSONread():
   with open('lairway_core.json', 'r') as core_file:
      return dict(json.load(core_file))

core=JSONread()



def FindBotToken():
   if core["env"]:
      return os.environ['bot']
   else:
      return core["bot"]
   
def FindGithubToken():
   if core["env"]:
      return os.environ['GitHub'], os.environ["path"]
   else:
      return core["GitHub"], core["path"]

def FindIp():
   if core["env"]: ip = os.environ['IP']
   else: ip = core["IP"]
   if ip == False: ip = "0.0.0.0"
   return ip