import wmi
#wmi_conn = wmi.WMI() for local.
 
w = wmi.WMI()

for p in w.Win32_Product():
    print (p)