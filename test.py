import requests
import sqlite3
import json
import os
from managedb import databaseManager
import time
from multiprocessing import Process
import threading

with open("extracthere\\nvdcve-1.1-2012.json", encoding='utf-8') as f:
    datas = json.load(f)




#for (dirpath, dirnames, filenames) in os.walk("extracthere"):
#    for jfile in filenames:
#        with open(dirpath + '\\' + jfile, encoding='utf-8') as f:
#            print("doing " + jfile)
#            data = json.load(f)


dbmanager = databaseManager()

def StoreCVE(data):
    for cves in data['CVE_Items']:

        '''# TABELA AllCVE
        #ID do cve
        print(cves['cve']['CVE_data_meta']['ID'])
        #Tipo de Dado (CVE neste caso)
        print(cves['cve']['data_type'])
        #formato dos dados (deve ser sempre MITRE)
        print(cves['cve']['data_format'])
        #data_version
        print(cves['cve']['data_version'])
        #descrição
        print(cves['cve']['description']['description_data'][0]['value'])
        #data de publicação
        print(cves['publishedDate'])
        #data de modificação
        print(cves['lastModifiedDate'])'''

        dbmanager.insertintoALLCVE((
            cves['cve']['CVE_data_meta']['ID'],
            cves['cve']['data_type'],
            cves['cve']['data_format'],
            cves['cve']['data_version'],
            cves['cve']['description']['description_data'][0]['value'],
            cves['publishedDate'],
            cves['lastModifiedDate']))

        # TABELA cpeuri
        if cves['configurations']['nodes'] != []:
            #for i in range(len(cves['configurations']['nodes'])):
            if "children" in cves['configurations']['nodes'][0]:
                for j in range(len(cves['configurations']['nodes'][0]['children'])):
                    for cpe in cves['configurations']['nodes'][0]['children'][j]['cpe_match']:
                        dbmanager.insertintoCPE((
                            cves['cve']['CVE_data_meta']['ID'],
                            cpe['cpe23Uri'],
                            cpe['vulnerable']))
                        #print(cves['cve']['CVE_data_meta']['ID'])
                        #print(cpe['cpe23Uri'])
                        #print(cpe['vulnerable'])

            else:
                #for j in range(len(cves['configurations']['nodes'][i])):
                #if "cpe_match" in cves['configurations']['nodes'][0]:
                for cpe in cves['configurations']['nodes'][0]['cpe_match']:
                    dbmanager.insertintoCPE((
                        cves['cve']['CVE_data_meta']['ID'],
                        cpe['cpe23Uri'],
                        cpe['vulnerable']))
                    #print(cves['cve']['CVE_data_meta']['ID'])
                    #print(cpe['cpe23Uri'])
                    #print(cpe['vulnerable'])

           # TABELA CVSS3 e CVSS2
        if cves['impact'] != {}:

            if 'baseMetricV3' in cves['impact'] and cves['impact']['baseMetricV3'] != {}:
                cvss3 = cves['impact']['baseMetricV3']['cvssV3']
                dbmanager.insertintoCVSS3((
                                        cves['cve']['CVE_data_meta']['ID'],
                                        cvss3['version'],
                                        cvss3['vectorString'],
                                        cvss3['attackVector'],
                                        cvss3['attackComplexity'],
                                        cvss3['privilegesRequired'],
                                        cvss3['userInteraction'],
                                        cvss3['scope'],
                                        cvss3['confidentialityImpact'],
                                        cvss3['integrityImpact'],
                                        cvss3['availabilityImpact'],
                                        cvss3['baseScore'],
                                        cvss3['baseSeverity'],
                                        cves['impact']['baseMetricV3']['exploitabilityScore'],
                                        cves['impact']['baseMetricV3']['impactScore']
                                        ))

            if 'baseMetricV2' in cves['impact'] and cves['impact']['baseMetricV2'] != {}:
                cvss2 = cves['impact']['baseMetricV2']['cvssV2']
                dbmanager.insertintoCVSS2((
                    cves['cve']['CVE_data_meta']['ID'],
                    cvss2['version'],
                    cvss2['vectorString'],
                    cvss2['accessVector'],
                    cvss2['accessComplexity'],
                    cvss2['authentication'],
                    cvss2['confidentialityImpact'],
                    cvss2['integrityImpact'],
                    cvss2['availabilityImpact'],
                    cvss2['baseScore'],
                    cves['impact']['baseMetricV2']['severity'],
                    cves['impact']['baseMetricV2']['exploitabilityScore'],
                    cves['impact']['baseMetricV2']['impactScore'],
                    cves['impact']['baseMetricV2']['acInsufInfo'] if 'acInsufInfo' in cves['impact']['baseMetricV2'] else "",
                    cves['impact']['baseMetricV2']['obtainAllPrivilege'],
                    cves['impact']['baseMetricV2']['obtainUserPrivilege'],
                    cves['impact']['baseMetricV2']['obtainOtherPrivilege'],
                    cves['impact']['baseMetricV2']['userInteractionRequired'] if 'userInteractionRequired' in cves['impact']['baseMetricV2'] else ""
                    ))

#print(data['CVE_Items'][1]['cve']['CVE_data_meta']['ID'])
start_time = time.time()
StoreCVE(datas)
elapsed_time = time.time() - start_time
print(elapsed_time)
'''
create table AllCVE (
   cveID varchar(20) NOT NULL,
   datatype varchar(5) NOT NULL,
   dataformat varchar(5) NOT NULL,
   dataversion varchar(5) NOT NULL,
   description text,
   publishedDate date,
   lastModifiedDate date
);

create table CPE23URI (
    cveID varchar(20) NOT NULL,
    cpe23uri text,
    vulnerable bool
);

create table CVSS3 (
    cveID varchar(20) NOT NULL,
    version varchar(5),
    vectorString varchar(50),
    attackVector  varchar(20),
    attackComplexity varchar(10),
    privilegesRequired varchar(10),
    userInteraction varchar(10),
    scope varchar(10),
    confidentialityImpact varchar(10),
    integrityImpact varchar(10),
    availabilityImpact varchar(10),
    baseScore float,
    baseSeverity varchar(10),
    exploitabilityScore float,
    impactScore float
);


create table CVSS2 (
cveID varchar(20) NOT NULL,
version
vectorString
attackVector
accessComplexity
authentication
confidentialityImpact
integrityImpact
availabilityImpact
baseScore
severity


Main Table composition

ID      Type       version      valueCWE          description     publishedDate         lastModifiedDate     



CVSS3 Metrics Table

ID      version         vectorString        attackVector          attackComplexity      privilegesRequired        userInteraction           scope           confidentialityImpact           integrityImpact             availabilityImpact          baseScore           baseSeverity    exploitabilityScore         impactScore 



CPE23URI Table

ID      cpe23uri        vulnerable


cvssV2

ID      version         vectorString        attackVector          accessComplexity      authentication        confidentialityImpact           integrityImpact           availabilityImpact           baseScore            severity    exploitabilityScore         impactScore       acInsufInfo         obtainAllPrivilege         obtainUserPrivilege              obtainOtherPrivilege                  userInteractionRequired

'''
