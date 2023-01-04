import sys
import inspect
import datetime
import color
import PipeClient
from FuncInfo import FuncInfo
from Message import Message
from MT4Runtime import MT4Runtime

# グローバル変数
frame = inspect.currentframe().f_back    
    
class Connector:
    DebugMode = False

    def OnPreInit(self, debug : bool):
        DebugMode = debug
        return
    def OnInit(self) -> int:
        return MT4Runtime.INIT_SUCCEEDED
    def OnTick(self):
        return
    def OnTimer(self):
        return
    def OnDeinit(self, reason : int):
        return
    def OnTimerInternal(self):
        return
    
    #  ----------  MT4のグローバル変数に相当するもの  ----------
    Ask = 0
    Bid = 0
    Volume = 0
    Bars = 0
    Digits = 0
    DecimalPoint = 0
    LastError = 0  #  GetLastError関数で取得するため
    FlagEmergencyStop = False

    #  サーバー側が返却したエラーコード（LastError変数に格納されている）を返却する。MT4のGetLastError関数と同じように使える。
    def GetLastError(self) -> int:
        return self.LastError

    def PrintDebugMessage(self, msg : str):
        if self.DebugMode:
            print(msg)

    def GetPlatformVersion(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "GetPlatformVersion"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataInt()

    def PlaySound(self, FileName : str) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "PlaySound"
        funcInfo.Parameter[0].SetData(FileName)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataBool()

    def iBars(self, CurrencyPair : str, TimeFrame : int) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "iBars"
        funcInfo.Parameter[0].SetData(CurrencyPair)
        funcInfo.Parameter[1].SetData(TimeFrame)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataInt()

    def TimeCurrent(self) -> datetime:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "TimeCurrent"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataDateTime()

    def TimeLocal(self) -> datetime:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "TimeLocal"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataDateTime()

    def TimeGMT(self) -> datetime:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "TimeGMT"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataDateTime()

    def TimeDaylightSavings(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "TimeDaylightSavings"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataInt()

    def AccountInfoInteger(self, property_id : int) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "AccountInfoInteger"
        funcInfo.Parameter[0].SetData(property_id)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataInteger()

    def AccountInfoDouble(self, property_id : int) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "AccountInfoDouble"
        funcInfo.Parameter[0].SetData(property_id)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataFloat()

    def AccountInfoString(self, property_id : int) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "AccountInfoString"
        funcInfo.Parameter[0].SetData(property_id)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataString()

    def AccountBalance(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "AccountBalance"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def AccountCredit(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'AccountCredit'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def AccountCompany(self) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "AccountCompany"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataString()

    def AccountCurrency(self) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'AccountCurrency'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataString()

    def AccountEquity(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'AccountEquity'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def AccountFreeMargin(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'AccountFreeMargin'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def AccountFreeMarginCheck(self, symbol : str, cmd : int, volume : float) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'AccountFreeMarginCheck'
        funcInfo.Parameter[0].SetData(symbol)
        funcInfo.Parameter[1].SetData(cmd)
        funcInfo.Parameter[2].SetData(volume)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def AccountFreeMarginMode(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'AccountFreeMarginMode'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def AccountLeverage(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'AccountLeverage'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    def AccountMargin(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'AccountMargin'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def AccountName(self) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "AccountName"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataString()

    def AccountNumber(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "AccountNumber"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    def AccountProfit(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'AccountProfit'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def AccountServer(self) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'AccountServer'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataString()

    def AccountStopoutLevel(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'AccountStopoutLevel'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    def AccountStopoutMode(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'AccountStopoutMode'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    def IsStopped(self) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'IsStopped'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataBool()

    def UninitializeReason(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'UninitializeReason'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    def TerminalInfoInteger(self, property_id : int) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'TerminalInfoInteger'
        funcInfo.Parameter[0].SetData(property_id)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    def TerminalInfoDouble(self, property_id : int) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'TerminalInfoDouble'
        funcInfo.Parameter[0].SetData(property_id)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def TerminalInfoString(self, property_id : int) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'TerminalInfoString'
        funcInfo.Parameter[0].SetData(property_id)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataString()

    def MQLInfoInteger(self, property_id : int) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'MQLInfoInteger'
        funcInfo.Parameter[0].SetData(property_id)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    def MQLInfoString(self, property_id : int) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'MQLInfoString'
        funcInfo.Parameter[0].SetData(property_id)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataString()

    def MQLSetInteger(self, property_id : int, property_value : int):
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'MQLSetInteger'
        funcInfo.Parameter[0].SetData(property_id)
        funcInfo.Parameter[1].SetData(property_value)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return

    def Symbol(self) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "Symbol"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataString()

    def Period(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "Period"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataInt()

    def Digits(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "Digits"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataInt()

    def Point(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "Point"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataFloat()

    def TerminalCompany(self) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "TerminalCompany"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataString()

    def TerminalName(self) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "TerminalName"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataString()

    def TerminalPath(self) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "TerminalPath"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataString()

    def MarketInfo(self, symbol, type) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "MarketInfo"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def SymbolsTotal(self,  selected : bool) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "SymbolsTotal"
        funcInfo.Parameter[0] = selected
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    def SymbolName(self, pos : int, selected : bool) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'SymbolName'
        funcInfo.Parameter[0].SetData(pos)
        funcInfo.Parameter[1].SetData(selected)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataString()

    def SymbolSelect(self, name : str, select : bool) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'SymbolSelect'
        funcInfo.Parameter[0].SetData(name)
        funcInfo.Parameter[1].SetData(select)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataBool()

    def SymbolInfoInteger(self, name : str, prop_id : int) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'SymbolInfoInteger'
        funcInfo.Parameter[0].SetData(name)
        funcInfo.Parameter[1].SetData(prop_id)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInteger()

    def SymbolInfoDouble(self, name : str, prop_id : int) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'SymbolInfoDouble'
        funcInfo.Parameter[0].SetData(name)
        funcInfo.Parameter[1].SetData(prop_id)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def SymbolInfoString(self, name : str, prop_id : int) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'SymbolInfoString'
        funcInfo.Parameter[0].SetData(name)
        funcInfo.Parameter[1].SetData(prop_id)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataString()

    def SeriesInfoInteger(self, symbol_name : str, timeframe : int, prop_id : int) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'SeriesInfoInteger'
        funcInfo.Parameter[0].SetData(symbol_name)
        funcInfo.Parameter[1].SetData(timeframe)
        funcInfo.Parameter[2].SetData(prop_id)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    def RefreshRates(self):
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'RefreshRates'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return

    def OrdersHistoryTotal(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "OrdersHistoryTotal"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()
    
    def OrdersTotal(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "OrdersTotal"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()
    
    def OrderSelect(self, index, select, pool) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "OrderSelect"
        funcInfo.Parameter[0].SetData(index)
        funcInfo.Parameter[1].SetData(select)
        funcInfo.Parameter[2].SetData(pool)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataBool()
    
    def MarketInfo(self, symbol : str, info_type : int) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "MarketInfo"
        funcInfo.Parameter[0].SetData(symbol)
        funcInfo.Parameter[1].SetData(info_type)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()
    
    def OrdersHistoryTotal(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrdersHistoryTotal'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    def OrdersTotal(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrdersTotal'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    def OrderSelect(self, index : int, select : int, pool : int) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderSelect'
        funcInfo.Parameter[0].SetData(index)
        funcInfo.Parameter[1].SetData(select)
        funcInfo.Parameter[2].SetData(pool)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataBool()

    def OrderSend(self, symbol : str, cmd : int, volume : float, price : float, slippage : int, stoploss : float, takeprofit : float, comment : str, magic : int, expiration : datetime, arrow_color : color) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "OrderSend"
        funcInfo.Parameter[0].SetData(symbol)
        funcInfo.Parameter[1].SetData(cmd)
        funcInfo.Parameter[2].SetData(volume)
        funcInfo.Parameter[3].SetData(price)
        funcInfo.Parameter[4].SetData(slippage)
        funcInfo.Parameter[5].SetData(stoploss)
        funcInfo.Parameter[6].SetData(takeprofit)
        funcInfo.Parameter[7].SetData(comment)
        funcInfo.Parameter[8].SetData(magic)
        funcInfo.Parameter[9].SetData(expiration)
        funcInfo.Parameter[10].SetData(arrow_color)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    def OrderClose(ticket : int, lots : float, price : float, slippage : int, arrow_color : color) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "OrderClose"
        funcInfo.Parameter[0].SetData(ticket)
        funcInfo.Parameter[1].SetData(lots)
        funcInfo.Parameter[2].SetData(price)
        funcInfo.Parameter[3].SetData(slippage)
        funcInfo.Parameter[4].SetData(arrow_color)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataBool()

    def OrderCloseBy(self, ticket : int, opposite : int, arrow_color : color) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderCloseBy'
        funcInfo.Parameter[0].SetData(ticket)
        funcInfo.Parameter[1].SetData(opposite)
        funcInfo.Parameter[2].SetData(arrow_color)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataBool()

    def OrderModify(self, ticket : int, price : float, stoploss : float, takeprofit : float, expiration : datetime, arrow_color : color) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderModify'
        funcInfo.Parameter[0].SetData(ticket)
        funcInfo.Parameter[1].SetData(price)
        funcInfo.Parameter[2].SetData(stoploss)
        funcInfo.Parameter[3].SetData(takeprofit)
        funcInfo.Parameter[4].SetData(expiration)
        funcInfo.Parameter[5].SetData(arrow_color)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataBool()

    def OrderDelete(self, ticket : int, arrow_color : color) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderDelete'
        funcInfo.Parameter[0].SetData(ticket)
        funcInfo.Parameter[1].SetData(arrow_color)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataBool()

    def OrderPrint(self):
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderPrint'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return

    def OrderTicket(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderTicket'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    def OrderOpenTime(self) -> datetime:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderOpenTime'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataDateTime()
    
    def OrderOpenPrice(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderOpenPrice'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def OrderType(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderType'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    def OrderLots(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderLots'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def OrderSymbol(self) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderSymbol'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataString()

    def OrderStopLoss(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderStopLoss'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def OrderTakeProfit(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderTakeProfit'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def OrderCloseTime(self) -> datetime:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderCloseTime'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataDateTime()

    def OrderClosePrice(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderClosePrice'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def OrderCommission(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderCommission'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def OrderExpiration(self) -> datetime:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderExpiration'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataDateTime()

    def OrderSwap(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderSwap'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def OrderProfit(self) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderProfit'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def OrderComment(self) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderComment'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataString()

    def OrderMagicNumber(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'OrderMagicNumber'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    #  トレードシグナル
    #  このプログラムはインジケータの開発を目的としたものではないためトレードシグナル系の関数の実装はしません。
    
    #   クライアントターミナルのグローバル変数
    def GlobalVariableCheck(self, name : str) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'GlobalVariableCheck'
        funcInfo.Parameter[0].SetData(name)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataBool()

    def GlobalVariableTime(self, name : str) -> datetime:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'GlobalVariableTime'
        funcInfo.Parameter[0].SetData(name)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataDateTime()

    def GlobalVariableDel(self, name : str) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'GlobalVariableDel'
        funcInfo.Parameter[0].SetData(name)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataBool()

    def GlobalVariableGet(self, name : str) -> float:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'GlobalVariableGet'
        funcInfo.Parameter[0].SetData(name)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataFloat()

    def GlobalVariableName(self, index : int) -> str:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'GlobalVariableName'
        funcInfo.Parameter[0].SetData(index)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataString()

    def GlobalVariableSet(self, name : str, value : float) -> datetime:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'GlobalVariableSet'
        funcInfo.Parameter[0].SetData(name)
        funcInfo.Parameter[1].SetData(value)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataDateTime()

    def GlobalVariablesFlush(self):
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'GlobalVariablesFlush'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return

    def GlobalVariableTemp(self, name : str) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'GlobalVariableTemp'
        funcInfo.Parameter[0].SetData(name)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataBool()

    def GlobalVariableSetOnCondition(self, name : str, value : float, check_value : float) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'GlobalVariableSetOnCondition'
        funcInfo.Parameter[0].SetData(name)
        funcInfo.Parameter[1].SetData(value)
        funcInfo.Parameter[2].SetData(check_value)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataBool()

    def GlobalVariablesDeleteAll(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'GlobalVariablesDeleteAll1'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataInt()

    def GlobalVariablesDeleteAll(self, prefix_name : str) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'GlobalVariablesDeleteAll2'
        funcInfo.Parameter[0].SetData(prefix_name)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataInt()

    def GlobalVariablesDeleteAll(self, prefix_name : str, limit_date :datetime) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'GlobalVariablesDeleteAll3'
        funcInfo.Parameter[0].SetData(prefix_name)
        funcInfo.Parameter[1].SetData(limit_date)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return funcInfo.ReturnValue.GetDataInt()

    def GlobalVariablesTotal(self) -> int:
        funcInfo = FuncInfo()
        funcInfo.FuncName = 'GlobalVariablesTotal'
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataInt()

    # ！オブジェクト関数は実装しません

    #  イベント操作
    def EventSetMillisecondTimer(self, milliseconds : int) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "EventSetMillisecondTimer"
        funcInfo.Parameter[0].SetData(milliseconds)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataBool()

    def EventSetTimer(self, seconds : int) -> bool:
        funcInfo = FuncInfo()
        funcInfo.FuncName = "EventSetTimer"
        funcInfo.Parameter[0].SetData(seconds)
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        self.LastError = funcInfo.ErrorCode
        return funcInfo.ReturnValue.GetDataBool()

    def EventKillTimer(self):
        funcInfo = FuncInfo()
        funcInfo.FuncName = "EventKillTimer"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return

    def ExpertRemove(self):
        funcInfo = FuncInfo()
        funcInfo.FuncName = "ExpertRemove"
        if not self.SendReceiveRequest(funcInfo):
            self.FlagEmergencyStop = True
        return
    
    def CallFunc(self, funcInfo):
        if self.MT4StringCompare(funcInfo.FuncName, "OnPreInit"):
            debug = True if funcInfo.Parameter[0].GetDataFloat() != 0 else False
            self.OnPreInit(debug)
        else:
            self.Ask = funcInfo.Parameter[0].GetDataFloat()
            self.Bid = funcInfo.Parameter[1].GetDataFloat()
            self.Volume = funcInfo.Parameter[7].GetDataLong()
            self.Bars = funcInfo.Parameter[8].GetDataInt()
            self.Digits = funcInfo.Parameter[9].GetDataInt()
            self.DecimalPoint = funcInfo.Parameter[10].GetDataInt()
            
            if self.MT4StringCompare(funcInfo.FuncName, "OnInit"):
                funcInfo.ReturnValue.SetData(self.OnInit())
            elif self.MT4StringCompare(funcInfo.FuncName, "OnTick"):
                self.OnTick()
            elif self.MT4StringCompare(funcInfo.FuncName, "OnTimer"):
                self.OnTimer()
            elif self.MT4StringCompare(funcInfo.FuncName, "OnDeinit"):
                self.OnDeinit(funcInfo.Parameter[0].GetDataInt())
            elif self.MT4StringCompare(funcInfo.FuncName, "OnPreInit"):
                funcInfo.ReturnValue.SetData(self.OnPreInit())
            elif self.MT4StringCompare(funcInfo.FuncName, "OnTimerInternal"):
                self.OnTimerInternal()
            else:
                print('不明な関数が呼び出されました' + funcInfo.FuncName + '。')
            return
    
    def CallExpertRemove(self):
        # クライアント側なので何もしない。ソース共通化のため残している
        return
    
    def MT4StringCompare(self, a : str, b : str) -> bool:
        return a == b
    
    def SendReceiveRequest(self, funcInfo : FuncInfo) -> bool:
        self.PrintDebugMessage('SendReceiveRequestが呼ばれました。')
        PosParameter = 0
        PosAuxiliary = 0
        s = Message()
        r = Message()
        funcInfoReceived = FuncInfo()
        
        if funcInfo.FuncName != None:
            # 呼び出す関数が決まっている
            s.SetMessageType(Message.MSG_REQUEST_CALL_FUNCTION)
            s.Data[1].SetData(funcInfo.FuncName)
        else:
            # 呼び出す関数が決まっていない（最初だけ何も要求を送らない）
            s.SetMessageType(Message.MSG_NOP)
        
        while r.GetMessageType() != Message.MSG_AUXILIARY_END:
            self.PrintDebugMessage('リクエスト情報を送受信するためのループ')
            s.SetEmergencyStop(1 if self.FlagEmergencyStop == True else 0)
            
            if not self.Pipe.SendMessage(s):
                print("%s: %s, %s, %d" % ('メッセージの送信に失敗しました', sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno))
                del s
                del r
                del funcInfoReceived
                return False
            
            if (funcInfoReceived.FuncName != None and self.MT4StringCompare(funcInfoReceived.FuncName, "OnDeinit") and s.GetMessageType() == Message.MSG_AUXILIARY_END):
                break
            
            #  ----  ここまでで関数呼び出し依頼は完了している  ----
            
            r.Clear()
            if not self.Pipe.ReceiveMessage(r):
                print("%s: %s, %s, %d" % ('メッセージの受信に失敗しました', sys._getframe().f_code.co_filename, sys._getframe().f_code.co_name, sys._getframe().f_lineno))
                del s
                del r
                del funcInfoReceived
                return False

            if r.GetMessageType() == Message.MSG_NULL:
                print('空のメッセージを受信しました。緊急停止します:')
                self.CallExpertRemove()
                del s
                del r
                del funcInfoReceived
                return False
                
            #  緊急終了フラグの確認
            if r.GetEmergencyStop() != 0:
                self.CallExpertRemove()
                        
            #  先方からのメッセージを処理する
            if r.GetMessageType() == Message.MSG_REQUEST_PARAMETER:
                self.PrintDebugMessage('MSG_REQUEST_PARAMETERを受信しました')
                # 関数呼び出しの結果
                # 関数呼び出し依頼をした場合
                s.Clear()
                s.SetMessageType(Message.MSG_PARAMETER)
                funcInfo.Parameter[PosParameter].CopyDataGramTo(s.Data[1])
                if PosParameter >= funcInfo.GetNumberOfParameters():
                    s.SetMessageType(Message.MSG_PARAMETER_END)
                PosParameter = PosParameter + 1
            elif r.GetMessageType() == Message.MSG_RETURN_VALUE:
                self.PrintDebugMessage('MSG_RETURN_VALUEを受信しました')
                s.Clear()
                s.SetMessageType(Message.MSG_REQUEST_ERROR_CODE)
                r.Data[1].CopyDataGramTo(funcInfo.ReturnValue)
            elif r.GetMessageType() == Message.MSG_ERROR_CODE:
                self.PrintDebugMessage('MSG_ERROR_CODEを受信しました')
                s.Clear()
                s.SetMessageType(Message.MSG_REQUEST_AUXILIARY)
                funcInfo.ErrorCode = r.Data[1].GetDataInt()
                PosAuxiliary = 0
            elif r.GetMessageType() == Message.MSG_AUXILIARY or r.GetMessageType() == Message.MSG_AUXILIARY_END:
                self.PrintDebugMessage('MSG_AUXILIARYまたはMSG_AUXILIARY_ENDを受信しました')
                s.Clear()
                s.SetMessageType(Message.MSG_REQUEST_AUXILIARY)
                r.Data[1].CopyDataGramTo(funcInfo.Auxiliary[PosAuxiliary])
                PosAuxiliary = PosAuxiliary + 1
            #  関数呼び出し依頼
            elif r.GetMessageType() == Message.MSG_REQUEST_CALL_FUNCTION:
                self.PrintDebugMessage('MSG_REQUEST_CALL_FUNCTIONを受信しました')
                s.Clear()
                s.SetMessageType(Message.MSG_REQUEST_PARAMETER)
                funcInfoReceived.Clear()
                funcInfoReceived.FuncName = r.Data[1].GetDataString()
                PosParameter = 0
            elif r.GetMessageType() == Message.MSG_PARAMETER:
                self.PrintDebugMessage('MSG_PARAMETER受信を受信しました')
                s.Clear()
                s.SetMessageType(Message.MSG_REQUEST_PARAMETER)
                r.Data[1].CopyDataGramTo(funcInfoReceived.Parameter[PosParameter])
                PosParameter = PosParameter + 1
            elif r.GetMessageType() == Message.MSG_PARAMETER_END:
                self.PrintDebugMessage('MSG_PARAMETER_END受信を受信しました')
                r.Data[1].CopyDataGramTo(funcInfoReceived.Parameter[PosParameter])
                PosParameter = PosParameter + 1
                
                #  関数実行
                self.CallFunc(funcInfoReceived)
                
                #  関数呼び出し後
                s.Clear()
                s.SetMessageType(Message.MSG_RETURN_VALUE)
                funcInfoReceived.ReturnValue.CopyDataGramTo(s.Data[1])
            elif r.GetMessageType() == Message.MSG_REQUEST_ERROR_CODE:
                self.PrintDebugMessage('MSG_REQUEST_ERROR_CODEを受信しました')
                s.Clear()
                s.SetMessageType(Message.MSG_ERROR_CODE)
                s.Data[1].SetData(funcInfoReceived.ErrorCode)
            elif r.GetMessageType() == Message.MSG_REQUEST_AUXILIARY:
                self.PrintDebugMessage('MSG_REQUEST_AUXILIARYを受信しました')
                s.Clear()
                s.SetMessageType(Message.MSG_AUXILIARY)
                funcInfoReceived.Auxiliary[PosAuxiliary].CopyDataGramTo(s.Data[1])
                if PosAuxiliary >= funcInfoReceived.GetNumberOfAuxiliaries():
                    s.SetMessageType(Message.MSG_AUXILIARY_END)
                PosAuxiliary = PosAuxiliary + 1
        del s
        del r
        del funcInfoReceived
        self.PrintDebugMessage('リクエスト情報の送受信を行いました。')
        return True
    
    # コンストラクタ
    def __init__(self):
        self.Pipe = PipeClient.PipeClient()
    
    def ConnectToMT4(self, PipeName : str):
        self.FlagEmergencyStop = False  # サーバーの停止等によりメッセージの送受信ができなくなった場合
        #protected HashMap<String/*通貨ペア*/, HashMap<Integer/*時間足*/, TickData>> ChartData = new HashMap<>(100)
        
        filename = '\\\\.\\pipe\\' + PipeName
        self.Pipe.ConnectToServer(PipeName)
        # ！ここにctrl+C押下時のシャットダウン処理を追加する必要がある
        
        fi = FuncInfo()
        fi.FuncName = None
        self.SendReceiveRequest(fi)

        self.PrintDebugMessage('リクエストの送受信がすべて終わりました。プログラムを終了します。')
        
        self.PrintDebugMessage('サーバーとの接続を切断します。')
        self.Pipe.Close()
