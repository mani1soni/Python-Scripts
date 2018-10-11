import re,urllib2
email_pattern = re.compile(r'[\w.-_]+@[\w.]+')
html = urllib2.urlopen("www.example.com")
code = html.read()
m = email_pattern.findall(code)
writer = open('emails.csv','w')
for i in m:
    writer.write(i+'\n')
fopen.close()
