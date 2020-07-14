import re
from unidecode import unidecode

def CapsToLowAndAccent(capsstring):
    return unidecode(capsstring.lower())

def SplitonNumber(fixstring):
    if re.findall("\d+",fixstring):
        return re.split("\d+", fixstring)[0]
    return fixstring

def CheckForMicrosoftonName(name):
    if "microsoft" in name:
        return name.replace("microsoft","")
    return name


def PrepProductString(prepingstring):
    lowstring = CapsToLowAndAccent(prepingstring)
    lowstring = SplitonNumber(lowstring)
    lowstring = CheckForMicrosoftonName(lowstring)
    return lowstring.strip()

def PrepVendorName(prepvendor):
    vendorname = CapsToLowAndAccent(prepvendor)
    vendorname = CheckForCorporationonVendor(vendorname)
    
    return vendorname.strip()

def CheckForCorporationonVendor(name):
    if "corporation" in name:
        return name.replace("corporation","")
    return name



