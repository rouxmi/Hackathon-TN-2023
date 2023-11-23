from flask import Blueprint,session, request
from flask.templating import render_template

import paramiko

# Definition of the blueprint
generationBP = Blueprint('generationBP', __name__)

# Definition of the main route
@generationBP.route("/generation", methods=["GET", "POST"])
def generation():
    if request.method == "POST":
        input_user = request.form.get("input")
        host = 'tesla.telecomnancy.univ-lorraine.fr'
        username = 'bourdais4u'
        password = 'X.W.E5L3Rb'

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh_client.connect(hostname=host, username=username, password=password)
            print("Connected to SSH server")
            
            stdin, stdout, stderr = ssh_client.exec_command('cd PI/Remi/Hackathon2/;source venv/bin/activate;python3 python/core/lyrics_generator.py '+input_user+';cat lyrics.txt')
            print("Done!")
            output = stdout.read().decode('utf-8')
            lyrics_list = output.split("--sep--")
            return render_template("generation.html", lyrics=lyrics_list)
        except paramiko.AuthenticationException:
            print("Authentication failed, please check your credentials.")
        except paramiko.SSHException as ssh_exception:
            print("SSH connection failed:", ssh_exception)
        finally:
            ssh_client.close()
    elif request.method == "GET":
        return render_template("generation.html", lyrics="")
