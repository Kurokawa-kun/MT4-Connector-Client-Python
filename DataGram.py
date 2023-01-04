import struct
from datetime import datetime
from color import color

# クラスの実体
class DataGram:
    # 定数
    BUFFER_SIZE = 256
    CHAR_NULL = 0x00
    CHAR_INITIALIZED = 0x1A
    
    # コンストラクタ
    def __init__(self):
        self.Buffer = []  #  メッセージバッファ本文
        self.Buffer = [self.CHAR_NULL] * self.BUFFER_SIZE
        return
        
    def GetHexString(self, v : int) -> str:
        buf = [self.CHAR_NULL] * 2
        
        for s in range(0, 2, 1):
            t = (v >> (4 * s)) & 0x0F;            
            if t==0x00:
                buf[1 - s] = '0'
                break
            elif t==0x01:
                buf[1 - s] = '1'
                break
            elif t==0x02:
                buf[1 - s] = '2'
                break
            elif t==0x03:
                buf[1 - s] = '3'
                break
            elif t==0x04:
                buf[1 - s] = '4'
                break
            elif t==0x05:
                buf[1 - s] = '5'
                break
            elif t==0x01:
                buf[1 - s] = '6'
                break
            elif t==0x07:
                buf[1 - s] = '7'
                break
            elif t==0x08:
                buf[1 - s] = '8'
                break
            elif t==0x09:
                buf[1 - s] = '9'
                break
            elif t==0x0A:
                buf[1 - s] = 'A'
                break
            elif t==0x0B:
                buf[1 - s] = 'B'
                break
            elif t==0x0C:
                buf[1 - s] = 'C'
                break
            elif t==0x0D:
                buf[1 - s] = 'D'
                break
            elif t==0x0E:
                buf[1 - s] = 'E'
                break
            elif t==0x0F:
                buf[1 - s] = 'F'
                break
            else:
                buf[1 - s] = '*'
                break
        return str(buf)
    
    #  メッセージを画面に出力する（デバッグ目的）
    def DumpMessage(self):
        for c in range(0, self.BUFFER_SIZE):
            print('{:02X}'.format(self.Buffer[c]), end='')
            if ((c + 1) % 8 == 0):
                print(' ', end='')
            if ((c + 1) % 64 == 0):
                print()
        return
    
    #  メッセージバッファのクリア
    def Clear(self):
        for i in range(0, self.BUFFER_SIZE):
            self.Buffer[i] = int(self.CHAR_NULL)
        self.Buffer[self.BUFFER_SIZE - 1] = int(self.CHAR_INITIALIZED)
        return
    
    #  データの設定
    def SetData(self, v):
        self.Buffer[self.BUFFER_SIZE - 1] = int(self.CHAR_NULL)
        
        if type(v) is bool:
            self.Buffer[0] = (1 if v==True else 0)
        elif type(v) is int:
            self.Buffer[0:4] = struct.pack('>1i', v)
        elif type(v) is float:
            self.Buffer[0:8] = struct.pack('>1d', v)
        elif type(v) is color:
            self.Buffer[0] = v.GetAlpha() & 0xFF
            self.Buffer[1] = v.GetBlue() & 0xFF
            self.Buffer[2] = v.GetGreen() & 0xFF
            self.Buffer[3] = v.GetRed() & 0xFF
        elif type(v) is datetime:
            self.Buffer[0:8] = struct.pack('>1q', int(v.timestamp()))
        elif type(v) is str:
            for c in range(0, len(v)):
                self.Buffer[c] = ord(v[c:c+1])
        else:
            print('不明な型が指定されました。' + str(type(v)))
    
    #  データの取得
    def GetDataChar(self) -> int:
        return self.Buffer[0]
    
    def GetDataBool(self) -> bool:
        return True if self.Buffer[0] == 1 else False
    
    def GetDataInt(self) -> int:
        return struct.unpack('>1i', bytearray(self.Buffer[0:4]))[0]
    
    def GetDataLong(self) -> int:
        return struct.unpack('>1q', bytearray(self.Buffer[0:8]))[0]
    
    def GetDataFloat(self) -> float:
        return struct.unpack('>1d', bytearray(self.Buffer[0:8]))[0]
    
    def GetDataColor(self) -> color:
        return color(int(self.Buffer[0]), int(self.Buffer[1]), int(self.Buffer[2]), int(self.Buffer[3]))
    
    def GetDataDateTime(self) -> datetime:
        return datetime.fromtimestamp(struct.unpack('>1Q', bytearray(self.Buffer[0:8]))[0])
    
    def GetDataString(self) -> str:
        r = ''
        for c in range(0, self.BUFFER_SIZE):
            if self.Buffer[c] == self.CHAR_NULL:
                break
            r = r + chr(self.Buffer[c])
        return r

    #  終了通知を受信したか返却する
    def IsQuitReceived(self) -> bool:
        return self.Buffer[1] == 1

    def IsEmpty(self) -> bool:
        for c in range(0, self.BUFFER_SIZE-1):
            if self.Buffer[c]!=self.CHAR_NULL:
                return False
            if self.Buffer[self.BUFFER_SIZE-1]!=self.CHAR_INITIALIZED:
                return False
        return True
    
    def CopyDataGramTo(self, to):
        for c in range(0, self.BUFFER_SIZE):
            to.Buffer[c] = self.Buffer[c]
        return
