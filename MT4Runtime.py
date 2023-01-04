# íËêî
class MT4Runtime:
    class InitializeRetCode:
        INIT_SUCCEEDED              = 0x00
        INIT_FAILED                 = 0x01
        INIT_PARAMETERS_INCORRECT   = 0x7FFF
        INIT_AGENT_NOT_SUITABLE     = 0xFFFF
        
    class UninitializeReason:
        REASON_PROGRAM       = 0x00
        REASON_REMOVE        = 0x01
        REASON_RECOMPILE     = 0x02
        REASON_CHARTCHANGE   = 0x03
        REASON_CHARTCLOSE    = 0x04
        REASON_PARAMETERS    = 0x05
        REASON_ACCOUNT       = 0x06
        REASON_TEMPLATE      = 0x07
        REASON_INITFAILED    = 0x08
        REASON_CLOSE         = 0x09
    
    #  íçï∂éÌï 
    class OrderType:    
        OP_BUY = 0x00
        OP_SELL = 0x01
        OP_BUYLIMIT = 0x02
        OP_SELLLIMIT = 0x03
        OP_BUYSTOP = 0x04
        OP_SELLSTOP = 0x05    
    
    #  MT4ÇÃéûä‘ë´
    class TimeFrame:    
        PERIOD_CURRENT = 0
        PERIOD_M1 = 1
        PERIOD_M5 = 5
        PERIOD_M15 = 15
        PERIOD_M30 = 30
        PERIOD_H1 = 60
        PERIOD_H4 = 240
        PERIOD_D1 = 1440
        PERIOD_W1 = 10080
        PERIOD_MN1 = 43200

        MT4TimeFrames = [PERIOD_M1, PERIOD_M5, PERIOD_M15, PERIOD_M30, PERIOD_H1, PERIOD_H4, PERIOD_D1, PERIOD_W1, PERIOD_MN1]
