import serial.tools.list_ports
import time
def main():
    ports=serial.tools.list_ports.comports()
    ListPort=[]
    for port in sorted(ports):
        ListPort.append(port)
    if len(ListPort)>0:
        for i in ListPort:
            if i.description.find("Arduino")>0:
                print("Quello giusto")
            print(i.description)
    time.sleep(1)
    main()

if __name__=="__main__":
    main()
