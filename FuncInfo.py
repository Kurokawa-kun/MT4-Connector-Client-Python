from Message import Message
from DataGram import DataGram

class FuncInfo:
    MAX_NUMBER_OF_PARAMETERS = 30
    MAX_NUMBER_OF_AUXILIARIES = 5000
    
    # コンストラクタ
    def __init__(self):
        self.FuncName = ''
        self.Parameter = []
        for i in range(0, FuncInfo.MAX_NUMBER_OF_PARAMETERS, 1):
            self.Parameter.append(DataGram)
        self.ReturnValue = 0
        self.ErrorCode = 0
        self.Auxiliary = []
        for i in range(0, FuncInfo.MAX_NUMBER_OF_AUXILIARIES, 1):
            self.Auxiliary.append(DataGram)
        self.Clear()
    # フィールドをクリアする
    def Clear(self):
        self.FuncName = None
        for c in range(0, FuncInfo.MAX_NUMBER_OF_PARAMETERS, 1):
            self.Parameter[c] = DataGram()
            self.Parameter[c].Clear()
        self.ReturnValue = DataGram()
        self.ReturnValue.Clear()
        self.ErrorCode = 0
        for c in range(0, FuncInfo.MAX_NUMBER_OF_AUXILIARIES, 1):
            self.Auxiliary[c] = DataGram()
            self.Auxiliary[c].Clear()
    # パラメタの数を取得する
    def GetNumberOfParameters(self) -> int:
        c = 0
        while (c < FuncInfo.MAX_NUMBER_OF_PARAMETERS):
            if self.Parameter[c].IsEmpty():
                break
            c = c + 1
        return c
    #  補助情報の数を取得する
    def GetNumberOfAuxiliaries(self) -> int:
        c = 0
        while (c < FuncInfo.MAX_NUMBER_OF_AUXILIARIES):
            if self.Auxiliary[c].IsEmpty():
                break
        c = c + 1
        return c

    