import sqlite3

database = "dbtest.db"

class databaseManager():

    def __init__(self):
        self.conn = None
        try:
            self.conn = sqlite3.connect(database, check_same_thread=False)
            self.cur = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)
    
    def insertintoCPEinPC(self,values):
        sqlquery = '''insert into CPEinPC(cpeID,vendorname,
        productname,version,lastSearch) values(?,?,?,?,?);'''
        try:
            self.cur.execute(sqlquery,(values))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
    
    def checkifCPEalreadyinPC(self,Cpe):
        sqlquery = "SELECT EXISTS(SELECT 1 FROM CPEinPC WHERE cpeID = ?)"
        try:
            self.cur.execute(sqlquery,(Cpe,))
            return self.cur.fetchone()[0]
        except sqlite3.Error as e:
            print(e)
    def UpdateCPEinPCTable(self,date,Cpe):
        sqlquery = "UPDATE CPEinPC Set lastSearch = ? WHERE cpeID = ?"
        try:
            self.cur.execute(sqlquery,(date,Cpe,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
            
    def insertintoCPECVE(self,values):
        '''CPECVE(cpeID,cveID)'''
        sqlquery = '''insert into CPECVE(cpeID,cveID) values(?,?);'''
        try:
            self.cur.execute(sqlquery,(values))
            self.conn.commit()
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

    def getCPE(self):
        sqlquery = '''SELECT * FROM CPECVE'''
        try:
            self.cur.execute(sqlquery)
            self.cur.row_factory = lambda cursor, row: {'CPEID': row[0],'CVEID' : row[1]}
            rows = self.cur.fetchall()
            return rows
        except sqlite3.Error as e:
            print(e)

    def getCVEData(self,cveid):
        sqlquery = "SELECT * FROM ALLCVE where cveID =?"
        try:
            self.cur.execute(sqlquery,(cveid,))
            self.cur.row_factory = lambda cursor, row: {'cveID': row[0],'datatype':row[1],'dataformat':row[2],
                                                        'dataversion':row[3],'description' : row[4],
                                                        'publishedDate':row[5],'lastModifiedDate':row[5]}
            rows = self.cur.fetchone()
            return rows
        except sqlite3.Error as e:
            print(e)
    