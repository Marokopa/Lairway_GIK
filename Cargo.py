from github import Github
import os, subprocess, json



def Download(repo, folder_path, path=""):
    print(folder_path)
    contents = repo.get_contents(path)
    for content_file in contents:
        if content_file.type == "file":
            file_content = content_file.decoded_content
            file_name = os.path.join(folder_path, content_file.name)

            with open(file_name, 'wb') as file:
                file.write(file_content)
                print(f"File {content_file.name} downloaded successfully.")
        
        elif content_file.type == "dir":
            dir_name = os.path.join(folder_path, content_file.name)
            os.makedirs(dir_name, exist_ok=True)
            Download(repo, dir_name, content_file.path )

            
def FindGithubToken():
   if core["env"]:
      return os.environ['GitHub'], os.environ["path"]
   else:
      return core["GitHub"], core["path"]


with open('lairway_core.json', 'r') as core_file:
    core = dict(json.load(core_file))
    token, path = FindGithubToken()
    G = Github(token)
    repo = G.get_repo(path)

script_path = os.path.dirname(__file__)

Download(repo, script_path)

print("download was successful")

try: subprocess.Popen(["python", "lairway.py"])
except: subprocess.Popen(["python3", "lairway.py"])


















