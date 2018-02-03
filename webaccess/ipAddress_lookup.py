import urllib.request, urllib.parse, urllib.error
import json
import time

# get input file (use: IPs.txt)
infile = input('Input filename: ')
if len(infile) < 1:
    print()
    print('No file supplied!')
    exit()

dict = {}
# open input file and parse into dictionary
with open(infile) as f:
    for line in f.readlines():
        line = line.rstrip()
        if not line.startswith('CNAME'):
            if 'IN A' in line or 'CNAME' in line:
                splitline = line.split(' ')
                dict[splitline[0]] = splitline[-1]

# create output CSV and begin writing
outfile = infile.split('.')[0]  + '.csv'
out_file = open(outfile, 'w')
out_file.write('Domain Name,Status,IP or CNAME,Organization Name,ISP,AS Number,City,State,Country,Zip Code\n')

url = 'http://ip-api.com/json/'
# pull API and decode
for key, value in dict.items():

    uh = urllib.request.urlopen(url + value)
    data = uh.read().decode()
    try:
        js = json.loads(data)
    except:
        js = None

    print(json.dumps(js, indent=4))
    # parse JSON into output CSV
    if js['status'] == 'success':
        out_file.write(key + ',' + js['status'] + ',' + value + ',' + '"' + js['org'] + '"' + ',' + '"' + js['isp'] +\
                       '"' + ',' + '"' + js['as'] + '"' + ',' + js['city'] + ',' + js['regionName']\
                       + ',' + js['country'] + ',' + js['zip'] + ',' + '\n')
    else:
        out_file.write(key + ',' + js['status'] + ',' + value + '\n')

    time.sleep(1)

out_file.close()
