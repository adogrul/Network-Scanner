import scapy.all as scapy

pdst_value = input("Enter IP Filed : ")
if pdst_value.strip() == "":
        pdst_value = "10.0.2.1/24"

hwtype_value = input("Enter HardWare Type : ")
if hwtype_value.strip() =="":
        hwtype_value =1

ptype_value =input("Enter Protocol Type : ")
if ptype_value.strip() =="":
        ptype_value = 2048

op_value = input("1:ARP Request \n 2: ARP Reply\n 3: RARP Request(Reverses Arp Request) \n 4:RARP Reply\n Enter Operation Code : ")
if op_value.strip() == "":
        op_value = 1

arp_request_packet = scapy.ARP(pdst=pdst_value ,hwtype = hwtype_value , ptype = ptype_value , op = op_value )
scapy.ls(arp_request_packet)

broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff" )

unified_packet = broadcast_packet/arp_request_packet

(answeredList , unansweredList) = scapy.srp(unified_packet,timeout=1)
print("\n------------ANSWERED----------\n")
answeredList.summary()

