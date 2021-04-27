import subprocess

subprocess.call("set FLASK_APP=main.py & flask run", shell=True, cwd="Flask")
