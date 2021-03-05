import subprocess
import time
from datetime import datetime

# We can specify ant of the adapter interfaces here with this flag, 
# note: enp3s0 is the VMs bridged adapter. 
# interface_name = "any"
interface_name = "enp3s0"


print("This is the DoS packet capure tool......\n\n")
option = input("For simple Verbose Shell output HIT [S] \n\nFor Wireshark Packet Capture (.pac) HIT [P]:  ")
# def run_tcpdump_on_local_machine():
if option == "S" or option == "s":
    t = subprocess.run(["tcpdump", "-i", interface_name, ">", "tee", "/tmp/tcpdump.out"], shell=True)

elif option == "P" or option == "p":
    func_name = "run_tcpdump_on_local_machine - "
    print(func_name + "start")
    interface_name = "any"
    curr_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    capture_file_name = "DoS_TCP_Dump - interface:" + interface_name + "_" + curr_time + ".cap"
    num_sec_to_sleep = 5
    print(func_name + "about to create capture with name:" + capture_file_name)
    # Use the Linux subsystem to run tcpdump in the background 
    p = subprocess.Popen(["tcpdump",
                          "--interface", interface_name,
                          "-w", capture_file_name],
                         stdout=subprocess.PIPE)
    time.sleep(num_sec_to_sleep)
    p.terminate()
    print(func_name + "end")


# sudo tcpdump -n -l | tee file.out
# sudo tcpdump -i any > tcp.txt
