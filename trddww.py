import os
import requests



print ("downloading with requests")
url = ('http://novo-diveevo.org/Areas/kaptl/Content/vendor.js')
r = requests.get(url)
with open("vendor.js", "wb") as code:
    code.write(r.content)

    
f = open('vendor.js') # 
line = f.readline()
line_2 = f.readline()
kek = ('')


if line_2 == kek:
    print('minified')
elif line_2 != kek:
    print('non-minified')
    

f.close()

folder_size = os.path.getsize('vendor.js') #
mb = float(1024000.0)
mbb = float(folder_size) / float(mb)
max_mb = float(1.1)
if mbb > max_mb:
    print('bida,bilshe 1mb')
elif mbb < max_mb:
    print('file menshe 1mb')

