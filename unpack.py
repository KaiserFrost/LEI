import requests
import zipfile
import os

for i in range(2002,2020):
    filename = "nvdcve-1.1-"+str(i)+".json.zip"
    r_file = requests.get("https://nvd.nist.gov/feeds/json/cve/1.1/" + filename, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r_file:
            f.write(chunk)
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall("extracthere")
    os.remove(filename)