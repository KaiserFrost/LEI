import win32com.client
import requests
import CleaningService
from CleaningService import PrepString

cpematch = "https://services.nvd.nist.gov/rest/json/cves/1.0?cpeMatchString="

strComputer = "." 
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2") 
colItems = objSWbemServices.ExecQuery("Select * from Win32_Product") 
cpelist = []
for objItem in colItems:
    if(objItem.Vendor == "Microsoft Corporation"):
            objItem.Vendor = "microsoft"
    dicpe = {"part" : "a",
    "vendor" : objItem.vendor,
    "product" : PrepString(objItem.Name),
    "version" : objItem.Version,
    "Update" : "",
    "Edition" : "",
    "Language" : "",
    "Software" : "",
    "Target_Software" : "",
    "Target_Hardware" : "",
    "Other" : ""}
    for x in dicpe:
        if dicpe[x] == "":
            dicpe[x] = "*"
    cpe23 = "cpe:2.3:"+ ':'.join(str(x) for x in dicpe.values())
    cpe23 = cpe23.replace(" ","_")
    with open ("file.txt","a")  as file:
        file.write(cpe23 + "\n")

    
    '''getcpe23 = requests.get(cpematch +cpe23)
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
                cves['lastModifiedDate']))'''
