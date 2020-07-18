import requests

url = "https://services.nvd.nist.gov/rest/json/cves/1.0?keyword="
getcpe23 = requests.get(url + "net core&isExactMatch=true")

if getcpe23.ok:
    data = getcpe23.json()
    for cves in data["result"]['CVE_Items']:
        '''print((
            cves['cve']['CVE_data_meta']['ID'],
            cves['cve']['data_type'],
            cves['cve']['data_format'],
            cves['cve']['data_version'],
            cves['cve']['description']['description_data'][0]['value'],
            cves['publishedDate'],
            cves['lastModifiedDate']))'''
        if cves['configurations']['nodes'] != []:
            #for i in range(len(cves['configurations']['nodes'])):
            if "children" in cves['configurations']['nodes'][0]:
                for j in range(len(cves['configurations']['nodes'][0]['children'])):
                    for cpe in cves['configurations']['nodes'][0]['children'][j]['cpe_match']:
                        print((
                            cves['cve']['CVE_data_meta']['ID'],
                            cpe['cpe23Uri'],
                            cpe['vulnerable']))
            else:
                #for j in range(len(cves['configurations']['nodes'][i])):
                #if "cpe_match" in cves['configurations']['nodes'][0]:
                for cpe in cves['configurations']['nodes'][0]['cpe_match']:
                    print((
                        cves['cve']['CVE_data_meta']['ID'],
                        cpe['cpe23Uri'],
                        cpe['vulnerable']))