from DataGram import DataGram

class Message:
    # 定数
    MSG_NULL = 0x00
    MSG_NOP = 0x0A
    MSG_REQUEST_CALL_FUNCTION = 0x23
    MSG_REQUEST_PARAMETER = 0x24
    MSG_PARAMETER = 0x25
    MSG_PARAMETER_END = 0x26
    MSG_RETURN_VALUE = 0x27
    MSG_REQUEST_ERROR_CODE = 0x28
    MSG_ERROR_CODE = 0x29
    MSG_REQUEST_AUXILIARY = 0x2A
    MSG_AUXILIARY = 0x2B
    MSG_AUXILIARY_END = 0x2C
    NUMBER_OF_DATAGRAMS = 2 #  1メッセージあたりのデータグラムの数
    
    # コンストラクタ
    def __init__(self):
        self.Data = []
        for i in range(0, self.NUMBER_OF_DATAGRAMS):
            self.Data.append(DataGram())
        self.Clear()
    
    def Clear(self):
        for i in range(0, self.NUMBER_OF_DATAGRAMS):
            self.Data[i].Clear()
    
    def SetMessageType(self, mt):
        self.Data[0].Buffer[DataGram.BUFFER_SIZE - 1] = self.MSG_NULL
        self.Data[0].Buffer[0] = mt
        return

    def SetEmergencyStop(self, flg):
        self.Data[0].Buffer[DataGram.BUFFER_SIZE - 1] = self.MSG_NULL
        self.Data[0].Buffer[1] = flg
        return

    def SetSequenceNumber(self, num):
        self.Data[0].Buffer[DataGram.BUFFER_SIZE - 1] = self.MSG_NULL
        self.Data[0].Buffer[2] = num
        return

    def GetMessageType(self):
        return self.Data[0].Buffer[0]

    def GetEmergencyStop(self):
        return self.Data[0].Buffer[1]

    def GetSequenceNumber(self):
        return self.Data[0].Buffer[2]
