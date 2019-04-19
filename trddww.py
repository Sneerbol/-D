import os
import requests
import sys


print ('downloading with requests')
url = ('http://novo-diveevo.org/Areas/kaptl/Content/vendor.js') ''' url here '''
r = requests.get(url)
with open('vendor.js', 'wb') as code: 
    code.write(r.content)

    

f=open('vendor.js','r',encoding='utf-8') ''' open file below '''
n = 0
for s in f:
    i = s.find('/n') ''' if downloaded code contains more than 1 "/n" than code is not minified '''
    if i > -1:        
        n += 1
      
if n > 1:
    print('no-min')
elif n <= 1:
    print('min')
f.close()


folder_size = os.path.getsize('vendor.js') '''Check file size. File must be less than 1 mb to be minified '''
mb = float(1024000.0)
mbb = float(folder_size) / float(mb) 
max_mb = float(1.1)
if mbb > max_mb:
    print('File higer than 1mb')
elif mbb < max_mb:
    print('File less than 1 mb')

