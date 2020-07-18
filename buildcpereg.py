import winreg
from CleaningService import *
import requests
from storeData import *
from datetime import datetime

def getWinProduct(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            try:
                software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
            except EnvironmentError:
                software['version'] = 'undefined'
            try:
                software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
            except EnvironmentError:
                software['publisher'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list


cpelist = []
def turnCPEWin(software_list,NoVersion=False):

    for software in software_list:

        vendor = PrepVendorName(software['publisher'])
        product = PrepProductString(software['name'])
        version = software['version']
        if NoVersion==False:
            dicpe = {"part" : "a",
            "vendor" : vendor,
            "product" : product,
            "version" : version,
            "Update" : "",
            "Edition" : "",
            "Language" : "",
            "Software" : "",
            "Target_Software" : "",
            "Target_Hardware" : "",
            "Other" : ""}
        else:
            dicpe = {"part" : "a",
            "vendor" : vendor,
            "product" : product,
            "version" : "",
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
        cpelist.append((vendor,product,version,cpe23))
    return cpelist
cpematch = "https://services.nvd.nist.gov/rest/json/cves/1.0?cpeMatchString="

def getCVE(cpelist):
    '''
    Procura pelos CVE na base de dados da NIST, usando para isto
    a API especificada.
    Recebe um tuple, que contem o vendor, o nome do programa, a versão e o cpe
    '''
    for cpe in cpelist:
        getcpe = requests.get(cpematch +cpe[3])
        if getcpe.ok:
            
            data = getcpe.json()
            print("checking  " + cpe[3])
            StoreCPEinPC(cpe,datetime.today().strftime('%Y-%m-%d'))
            StoreCVE(data,cpe[3])

software_list = getWinProduct(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + getWinProduct(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + getWinProduct(winreg.HKEY_CURRENT_USER, 0)
cpelist = turnCPEWin(software_list)
print(cpelist)
#getCVE(cpelist)