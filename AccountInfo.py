# íËêî
class AccountInfo:
    class IntegerPropertyID:
        ACCOUNT_LOGIN                   = 0x00
        ACCOUNT_TRADE_MODE              = 0x20
        ACCOUNT_LEVERAGE                = 0x23
        ACCOUNT_LIMIT_ORDERS            = 0x2F
        ACCOUNT_MARGIN_SO_MODE          = 0x2C
        ACCOUNT_TRADE_ALLOWED           = 0x21
        ACCOUNT_TRADE_EXPERT            = 0x22

    class DoublePropertyID:
        ACCOUNT_BALANCE                 = 0x25
        ACCOUNT_CREDIT                  = 0x26
        ACCOUNT_PROFIT                  = 0x27
        ACCOUNT_EQUITY                  = 0x28
        ACCOUNT_MARGIN                  = 0x29
        ACCOUNT_FREEMARGIN              = 0x2A
        ACCOUNT_MARGIN_FREE             = 0x2A
        ACCOUNT_MARGIN_LEVEL            = 0x2B
        ACCOUNT_MARGIN_SO_CALL          = 0x2D
        ACCOUNT_MARGIN_SO_SO            = 0x2E
        ACCOUNT_MARGIN_INITIAL          = 0x30
        ACCOUNT_MARGIN_MAINTENANCE      = 0x31
        ACCOUNT_ASSETS                  = 0x32
        ACCOUNT_LIABILITIES             = 0x33
        ACCOUNT_COMMISSION_BLOCKED      = 0x34
    
    class StringPropertyID:
        ACCOUNT_NAME                    = 0x01
        ACCOUNT_SERVER                  = 0x03
        ACCOUNT_CURRENCY                = 0x24
        ACCOUNT_COMPANY                 = 0x02
        ACCOUNT_TRADE_MODE_DEMO         = 0x00
        ACCOUNT_TRADE_MODE_CONTEST      = 0x01
        ACCOUNT_TRADE_MODE_REAL         = 0x02
    
    class StopOutMode:
        ACCOUNT_STOPOUT_MODE_PERCENT    = 0x00
        ACCOUNT_STOPOUT_MODE_MONEY      = 0x01    
