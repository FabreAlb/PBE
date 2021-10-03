from pynfc import Nfc, Desfire, Timeout

class Rfid:
    
    # return uid in hexa str 
    def read_uid(self):
        n = Nfc("pn532_uart:/dev/ttyS0:115200")
        for target in n.poll():
            hexa=target.uid.decode(encoding='utf-8')
            return hexa.upper()
        
if __name__ == "__main__":

    rf = Rfid()
    uid = rf.read_uid()
    print(uid)
