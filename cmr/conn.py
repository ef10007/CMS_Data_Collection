import paramiko
import os
from pprint import pprint

def start_connection(cmd):
    username = os.getenv('gibbs_user')
    pw = os.getenv('gibbs_pw')
    port = 22
    remote_ip = os.getenv('gibbs_host')

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(remote_ip, username =username, password=pw, port=port)
    ssh.invoke_shell()
    (stdin, stdout, stderr) = ssh.exec_command(cmd)

    pprint(stdout.read())
    pprint(stderr.read())
    ssh.close()


if __name__ == '__main__':
    sqlitecmd = 'sqlite3 /home/mtg/jinny/c2db.db' 
    start_connection('ls -al')