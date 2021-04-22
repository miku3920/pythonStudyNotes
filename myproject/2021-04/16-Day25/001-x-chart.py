# project 5
import subprocess

subprocess.call("start cmd /k python server-backend.py", shell=True, cwd="dist")
subprocess.call("start cmd /k python server-frontend.py", shell=True, cwd="dist")
subprocess.call("127.0.0.1.url", shell=True, cwd="dist")
