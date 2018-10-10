import subprocess
import re

try:
    command = "dig TXT +short o-o.myaddr.l.google.com @ns1.google.com"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    public_ip, err = process.communicate()
    ip_regex_pattern = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
    public_ip = public_ip.split("\"")[1]
    if re.match(ip_regex_pattern, public_ip):
        print (public_ip)
    else:
        public_ip = None
except Exception, e:
    public_ip = None
    print("ERROROROROR %s" % e)

