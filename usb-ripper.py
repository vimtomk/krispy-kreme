# Credits to Joshua Natan of Medium.

# Cross-check the serial number.
checked_number = []
auth_list = open("auth.txt", "r")
auth_list = auth_list.read()
for i in range(1, 10):
    sysfile = open("syslog-{}".format(i),"r")
    for j in sysfile:
        if ': SerialNumber:' in j:
            serialnumber = j.rstrip()[67:]
            if serialnumber not in checked_number:
                if serialnumber not in auth_list:

                    report = "{serialnumber} from syslog-{lognumber} file is not found in auth file".format(serialnumber=serialnumber,lognumber=i)
                    report += "\n==================================================\n"
                    file = open("not-found-report.txt","a")
                    file.write(report)
                    file.close()
                else:
                    print("{} is found in auth".format(serialnumber))
                    checked_number.append(serialnumber)
                    