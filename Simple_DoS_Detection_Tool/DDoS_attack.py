from scapy.all import *
import socket
import struct


def dosDetect():

    s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)

    ipARrray = []
    uniqueArray = []
    # The following line of code will open a text file, having the details of DDoS attack in append mode.

    file_txt = open("attack_DDoS.txt", 'w')
    t1 = str(datetime.now())
    # With the help of following line of code,
    # current time will be written whenever the program runs.

    file_txt.writelines(t1)
    file_txt.writelines("\n")
    ''' 
    Now, we need to assume the hits from a particular IP. Here we are assuming 
    that if a particular IP is hitting for more than 15 times then it would be an attack.
    '''
    countIP = 0
    while True:
        pkt = s.recvfrom(2048)
        ipheader = pkt[0][14:34]
        ip_hdr = struct.unpack("!8sB3s4s4s", ipheader)
        IP = socket.inet_ntoa(ip_hdr[3])
        '''inet_ntoa(packed_ip) -> ip_address_string
                Convert an IP address from 32-bit packed
                binary format to string format'''
        ipARrray.append(IP)
        if IP not in uniqueArray:
            uniqueArray.append(IP)
            countIP = countIP + 1
            print("count: ", countIP)

        print("The Source of the IP is:", IP)
        if (countIP == 10 and IP != "127.0.0.1"):
            print("10 here!!!")
            break
        # The following line of code will check whether the IP exists in dictionary or not.
        # If it exists then it will increase it by 1.

    print("end of while")
    # print(ipARrray)
    # print(uniqueArray)
    consecHit = 0
    for i in range(1, len(ipARrray)):
        # Test here for consecutive IP hits, disregarding the Loop back address
        if(ipARrray[i] == ipARrray[i - 1]) and (ipARrray[i] != "127.0.0.1"):
            consecHit = consecHit + 1
            print("in here", ipARrray[i], end=" ")

    if consecHit > 10:
        line = "\n\n15 His exceeded: ", "\n", "IP Adreess: ", IP, "\n", "At time: ", t1, "\n"
        file_txt.writelines(line)
        line = "DDOS attack is Detected: \n"
        file_txt.writelines(line)
        line = "IP Address: "
        file_txt.writelines(line)

        file_txt.writelines(IP)

        file_txt.writelines("\n")
