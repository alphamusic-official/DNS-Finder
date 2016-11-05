import urllib
import json
import subprocess

def checkIp(site):
    proc = subprocess.Popen('cmd.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
    while 1:
        output = proc.stdout.readline()
        if "." in output:
            break

    proc.stdin.write('ping {0}\n'.format(site))
    while 1:
        output = proc.stdout.readline()
        if site in output:
            output = proc.stdout.readline()
            output = proc.stdout.readline()
            break
    proc.kill()
    i = output.find(site)+len(site)+2
    ii = output.find(']')
    return output[i:ii]

def CheckSite(site):
    local_ip = checkIp(site)
    req = urllib.urlopen('http://api.whois7.ru/?s=ip&q={0}'.format(local_ip)).read()
    info = json.loads(req)
    if info['hostname'] == site:
        return '0'
    else:
        return '1'