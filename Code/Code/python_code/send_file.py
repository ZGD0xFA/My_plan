import os
import paramiko

ip = ""
port = 50222
username = ""
password = ""
path = ""


def uploadfiletoserver(local,remote):
    if not path:
        print("Error: Cann't find the path for upload, please check out build.json.")
        return None
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)
    remote = os.path.join(path, remote)
    
    sftp = ssh.open_sftp()
    sftp.put(local, remote)
    return remote

def test():
    print(ip, port )

if __name__ == "__main__":
    try:
        uploadfiletoserver("src", "dest")
    except Exception as e:
        print(e)

