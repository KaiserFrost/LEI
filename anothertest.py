import wmi
import win32com.client
#wmi_conn = wmi.WMI() for local.
 
w = wmi.WMI()

for p in w.Win32_Product():
    print (p)


def wincom():
    
#cp = subprocess.run(["apt","list", "--installed"], stdout=subprocess.PIPE)
#output = subprocess.check_output("apt list --installed", shell=True)
#output = output.decode("utf-8")

#print("Version info: ",output)
    
    strComputer = "." 
    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
    objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2") 
    colItems = objSWbemServices.ExecQuery("Select * from Win32_Product") 
    for objItem in colItems:
        if(objItem.Vendor == "Microsoft Corporation"):
            objItem.Vendor = "microsoft"
        print("\n")
        print ("Caption: ", objItem.Caption)
        print ("Description: ", objItem.Description) 
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
    
