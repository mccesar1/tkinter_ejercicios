from digi.xbee.devices import XBeeDevice
 


 
# TODO: Replace with the serial port where your local module is connected to.
PORT = "COM1"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600
DATA_TO_SEND = "Hola XBee!"
 
resultado = 0
 
def main():
    print(" +--------------------------------------------------+")
    print(" | Sistema de Monitreo de Paneles Solares del SESLab|")
    print(" +--------------------------------------------------+\n")
 
    device = XBeeDevice(PORT, BAUD_RATE)
 
    try:
        device.open()
        print(" +--------------------------------------------------+")
 
        device.flush_queues() # Limpia las colas de recepcion y envio
 
        #print("Inicializando Xbee´s : %s..." % DATA_TO_SEND)
 
        #device.send_data_broadcast(DATA_TO_SEND)
 
        #print("Completado")
 
        print("Esperando Datos de Sensores...\n")
 
        while True:
            xbee_message = device.read_data()
            if xbee_message is not None:
                 
                print("Dirección de Xbee %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),
                                         xbee_message.data.decode()))
                 
                data = xbee_message.data.decode()
                voltage = data.split(",")[0]
                tiempo= data.split(",")[2]
                print (tiempo)
                print (voltage)
                 
                 
                 
 
    finally:
        if device is not None and device.is_open():
            device.close()
 
 
if __name__ == '__main__':
    main()