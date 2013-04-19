import re
with open('i') as f:t=f.read()
s=re.findall('".*"|\'.+?\'',t)
for r in s:t=t.replace(r,'@@')
t=re.sub('//.*','',t)
t=re.sub('/\*.+\*/', '',t,0,16)
l=t.replace('\t', '').split('\n')
w=[]
for i in l:w+=[j for j in i.split(' ') if j]
r=[]
for o in w:r+=re.findall('[\d\.]+|;|,|==|=|#|[~<>\+-=%\*\^&\|]+|\w+|\(|\)|{|}|\[|\]|@@|::', o)
i=0
for (j,o) in enumerate(r):
 if o=='@@':
  r[j]=s[i]
  i+=1
print "\n".join(r)
