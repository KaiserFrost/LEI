import subprocess
import sys
import platform
import distro
import importlib
import win32com.client
#cp = subprocess.run(["apt","list", "--installed"], stdout=subprocess.PIPE)
#output = subprocess.check_output("apt list --installed", shell=True)
#output = output.decode("utf-8")

#print("Version info: ",output)
if platform.system() == "Windows":
    print("i knew it")
    strComputer = "." 
    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
    objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2") 
    colItems = objSWbemServices.ExecQuery("Select * from Win32_Product") 
    for objItem in colItems:
        print("\n") 
        print ("Caption: ", objItem.Caption)
        #print ("Description: ", objItem.Description) 
        #print ("Identifying Number: ", objItem.IdentifyingNumber )
        #print ("Install Date: ", objItem.InstallDate )
        #print ("Install Date 2: ", objItem.InstallDate2 )
        #print ("Install Location: ", objItem.InstallLocation )
        #print ("Install State: ", objItem.InstallState )
        print ("Name: ", objItem.Name )
        #print ("Package Cache: ", objItem.PackageCache )
        #print ("SKU Number: ", objItem.SKUNumber )
        print ("Vendor: ", objItem.Vendor )
        print ("Version: ", objItem.Version )
        print("\n")

elif platform.system() == "linux":
    if distro.like() == "ubuntu" or "debian":
        output = subprocess.check_output("dpkg-query -f '${Package} ${Version}\n' -W", shell=True)
        output = output.decode("utf-8")
        print (output)

    """if distro.like() == "rhel":
        output = subprocess.check_output("dnf list installed", shell=True)
        output = output.decode("utf-8")
        print (output)"""

    
    
#p1 = subprocess.Popen(["apt","list", "--installed"], stdout=subprocess.PIPE)
#output = p1.communicate()[0]
#output = output.decode("utf-8")
#print (output)
