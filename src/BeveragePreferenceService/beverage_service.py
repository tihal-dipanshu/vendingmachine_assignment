import random
import sys
sys.path.append('/gen-py')

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from vending_machine import BeveragePreferenceService
from vending_machine.ttypes import BeverageType

class BeveragePreferenceHandler(BeveragePreferenceService.Iface):
    def getBeverage(self, btype):
        if btype == BeverageType.HOT:
            return random.choice(["cappuccino", "latte", "espresso"])
        else:
            return random.choice(["lemonade", "ice tea", "soda"])

if __name__ == '__main__':
    handler = BeveragePreferenceHandler()
    processor = BeveragePreferenceService.Processor(handler)
    transport = TSocket.TServerSocket(host='0.0.0.0', port=9092)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the beverage preference server...')
    server.serve() 