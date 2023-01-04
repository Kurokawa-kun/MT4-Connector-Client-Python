import sys
import datetime
from Connector import Connector
from MT4Runtime import MT4Runtime
from MarketInfo import MarketInfo
from color import color

class MyApp1(Connector):
    digits = 0              #  このシンボルの小数点以下の桁数
    currency_format = None  #  このシンボルを表示するためのフォーマット

    def OnInit(self) -> int:
        print('5秒間スリープして成行注文を1回発行するだけのプログラムです。')
        self.digits = int(self.MarketInfo(self.Symbol(), MarketInfo.DoubleProperty.MODE_DIGITS))
        self.currency_format = '{:.' + str(self.digits) + 'f}'
        self.EventSetTimer(5)
        return MT4Runtime.InitializeRetCode.INIT_SUCCEEDED

    def OnTick(self):
        #  現在価格を表示する
        print(self.Symbol().ljust(10) +": Bid:" + self.currency_format.format(self.Bid) + " Ask:" + self.currency_format.format(self.Ask))
        return

    def OnTimer(self):
        t = self.OrderSend(self.Symbol(), MT4Runtime.OrderType.OP_BUY, 1.00, self.Ask, 0, self.Ask - 100 * self.Point(), self.Ask + 250 * self.Point(), 'comment here', 15, datetime.datetime(3000, 1, 1, 0, 0, 0), color(0, 0, 0, 0)) #  成行注文
        if t == -1:
            print("OrderSendが失敗しました。エラーコードは'{:d}'".format(self.GetLastError()))
        print("チケット番号は'{:d}'。".format(t))
        self.ExpertRemove() #  プログラムの終了
        return

    def OnDeinit(self, reason : int):
        #  特に何もしない
        return
    
    # コンストラクタ
    def __init__(self):
        super().__init__()

# メイン
print('MyApp1(Python版)を開始します。')
if len(sys.argv) < 2:
    print('必要なパラメタが指定されていません。')
    print('MyApp1(Python版)を終了します。')
    exit()
p = MyApp1()
p.ConnectToMT4(sys.argv[2])
print('MyApp1(Python版)を終了します。')
