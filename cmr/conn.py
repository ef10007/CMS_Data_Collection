import paramiko
import os


def start_connection(cmd):
    username = os.getenv('gibbs_user')
    pw = os.getenv('gibbs_pw')
    port = 22
    remote_ip = os.getenv('gibbs_host')

    myconn = paramiko.SSHClient()
    myconn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    session = myconn.connect(remote_ip, username =username, password=pw, port=port)
    (stdin, stdout, stderr) = myconn.exec_command(cmd)

    print("{}".format(stdout.read()))
    print("{}".format(type(myconn)))
    print("Options available to deal with the connectios are many like\n{}".format(dir(myconn)))
    myconn.close()


if __name__ == '__main__':
    start_connection('sqlite3 /home/mtg/jinny/c2db.db')