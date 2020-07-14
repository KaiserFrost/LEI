import winreg
from CleaningService import *

def foo(hive, flag):
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

software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + foo(winreg.HKEY_CURRENT_USER, 0)

for software in software_list:
    dicpe = {"part" : "a",
        "vendor" : PrepVendorName(software['publisher']),
        "product" : PrepProductString(software['name']),
        "version" : software['version'],
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

    #print('Name=%s, Version=%s, Publisher=%s' % (software['name'], software['version'], software['publisher']))
#print('Number of installed apps: %s' % len(software_list))