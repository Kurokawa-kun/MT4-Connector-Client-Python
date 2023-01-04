import struct
from DataGram import DataGram
from Message import Message

class PipeClient:
    # コンストラクタ
    def __init__(self):
        self.DataStream = []
        for i in range(0, Message.NUMBER_OF_DATAGRAMS * DataGram.BUFFER_SIZE):
            self.DataStream.append(Message.MSG_NULL)
        return
    
    def ConnectToServer(self, PipeName : str):
        f = '\\\\.\\pipe\\' + PipeName
        self.pipeClient = open(f, mode='w+b')
        return
    
    def SendMessage(self, msg : Message):
        if msg.GetMessageType() == Message.MSG_NOP:
            return True
        for d in range(0, Message.NUMBER_OF_DATAGRAMS, 1):
            rd = self.pipeClient.write(bytearray(msg.Data[d].Buffer))
            if rd != DataGram.BUFFER_SIZE:
                return False
        return True
    
    def ReceiveMessage(self, msg : Message):
        bt = self.pipeClient.read(Message.NUMBER_OF_DATAGRAMS * DataGram.BUFFER_SIZE)
        if len(bt) != Message.NUMBER_OF_DATAGRAMS * DataGram.BUFFER_SIZE:
            return False
        p = 0
        for d in range(0, Message.NUMBER_OF_DATAGRAMS, 1):
            for i in range(0, DataGram.BUFFER_SIZE, 1):
                msg.Data[d].Buffer[i] = bt[p]
                p = p + 1
        return True
    
    def Close(self):
        self.pipeClient.close()
        return
