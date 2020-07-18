import requests
import json
import pprint
import urllib.request, json 


dicpe = {"part" : "a",
"vendor" : "microsoft",
"product" : ".net core",
"version" : 3.0,
"Update" : "",
"Edition" : "",
"Language" : "",
"Software" : "",
"Target_Software" : "",
"Target_Hardware" : "",
"Other" : ""}

url = "https://services.nvd.nist.gov/rest/json/cve/1.0/"
cpematch = "https://services.nvd.nist.gov/rest/json/cves/1.0?cpeMatchString="

dicpe23 = {}
for x in dicpe:
    if dicpe[x] == "":
        dicpe23[x] = "*"
    else:
        dicpe23[x] = dicpe[x]
cpe23 = "cpe:2.3:"+ ':'.join(str(x) for x in dicpe23.values())
cpe23 = cpe23.replace(" ","_")
print(cpe23)

dicpe22 = {}
for x in dicpe:
    if dicpe[x] != "":
        dicpe22[x] = dicpe[x]
cpe22 = "cpe:/" + ':'.join(str(x) for x in dicpe22.values())
cpe22 = cpe22.replace(" ","_")
print (cpe22)

#value = requests.get(url + "CVE-2020-0220")


getcpe23 = requests.get(cpematch +cpe23)
if getcpe23.ok:

    data = getcpe23.json()
    for cves in data["result"]['CVE_Items']:
        print((
            cves['cve']['CVE_data_meta']['ID'],
            cves['cve']['data_type'],
            cves['cve']['data_format'],
            cves['cve']['data_version'],
            cves['cve']['description']['description_data'][0]['value'],
            cves['publishedDate'],
            cves['lastModifiedDate']))

getcpe22 = requests.get(cpematch +cpe22)
if getcpe22.ok:

    data = getcpe22.json()
    for cves in data["result"]['CVE_Items']:
        print((
            cves['cve']['CVE_data_meta']['ID'],
            cves['cve']['data_type'],
            cves['cve']['data_format'],
            cves['cve']['data_version'],
            cves['cve']['description']['description_data'][0]['value'],
            cves['publishedDate'],
            cves['lastModifiedDate']))
