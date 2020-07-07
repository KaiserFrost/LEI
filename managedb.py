import sqlite3

database = "dbtest.db"

class databaseManager():

    def __init__(self):
        self.conn = None
        try:
            self.conn = sqlite3.connect(database,check_same_thread=False)
            self.cur = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)
    

    def insertintoALLCVE(self,values):
        sqlquery = '''insert into ALLCVE(cveID,datatype,dataformat,
        dataversion,description,publishedDate,lastModifiedDate) values(?,?,?,?,?,?,?);'''
        try:
            self.cur.execute(sqlquery,(values))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
    
    def insertintoCPE(self,values):
        sqlquery = '''insert into CPE23URI(cveID,cpe23uri,vulnerable) values(?,?,?);'''

        try:
            self.cur.execute(sqlquery,(values))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def insertintoCVSS3(self,values):
        sqlquery = '''insert into CVSS3(cveID,version,vectorString,attackVector,attackComplexity
        ,privilegesRequired,userInteraction,scope,confidentialityImpact,integrityImpact,
        availabilityImpact,baseScore,baseSeverity,exploitabilityScore,impactScore) 
        values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''
        try:

            self.cur.execute(sqlquery,(values))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def insertintoCVSS2(self,values):
        sqlquery = '''insert into CVSS2(cveID,version,vectorString,accessVector,accessComplexity,authentication,
        confidentialityImpact,integrityImpact,availabilityImpact,baseScore,severity,exploitabilityScore,
        impactScore,acInsufInfo,obtainAllPrivilege,obtainUserPrivilege,obtainOtherPrivilege,
        userInteractionRequired) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''
        try:
            self.cur.execute(sqlquery,(values))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)