#Actualment no funciona, era per provar de soluciionar un error de comunicacions comentat a la memòria

from pynfc import Nfc

class Rfid:

    def __init__(self):
        i=0
        while i < 10:
            try:
                print("Conectando")
                self.nfc = Nfc("pn532_uart:/dev/ttyS0:115200")
                i = 1000
            except:
                self.nfc = None
                i += 1

    def read_uid(self):
        i=0
        while i < 100:
            try:
                print("Cargando")
                for target in self.nfc.poll():
                    if target.uid: 
                        return target.uid.decode('utf-8').upper() #passar de byts a hexadecimal
                    i = 1000
            except:
                    print("No se pudieron extraer datos.")
                    i += 1
            



if __name__ == "__main__":
    rf = Rfid()
    uid = rf.read_uid()
    print(uid)
    #print(rf.capacity)
