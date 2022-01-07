import sys
import socket
from datetime import datetime

#request target
target = input("Enter the IP address to scan:")
portRange = input("Enter the port range to scan (eg 5-200):")

lowPort = int(portRange.split('-')[0])
highPort = int(portRange.split('-')[1])


"""
#define target via argument, if you want to use this instead of request target block above. Remove / ammend if lowport and highport line, and change in range eg: (10,50) <- example here scans port 10-50
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("syntax: python3 portScanner.py <ip>")
"""

#add pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started "+str(datetime.now()))
print("-" * 50)

if lowPort > 0 and highPort < 65535:
    try:
        for port in range(lowPort, highPort):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)                                                #if port not connected after 1 second, move on
            result = s.connect_ex((target,port))                                    #returns an error indicator (0 when port found)
            if result == 0: 
                print("Port "+str(port)+" open")
                s.close()
    except KeyboardInterrupt:
        print("\nExiting program")

    except socket.gaierror:
	    print("Hostname could not be resolved")

    except socket.error:
	    print("Couldn't connect to server")
else:
    print("Please enter a valid port range next time")
    sys.exit()
