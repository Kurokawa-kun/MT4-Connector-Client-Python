class MQLInfo:
    class IntegerPropertyID:
        MQL_CODEPAGE = 0x0F
        MQL_PROGRAM_TYPE = 0x02
        MQL_DLLS_ALLOWED = 0x03
        MQL_TRADE_ALLOWED = 0x04
        MQL_SIGNALS_ALLOWED = 0x0E
        MQL_DEBUG = 0x05
        MQL_PROFILER = 0x0A
        MQL_TESTER = 0x06
        MQL_OPTIMIZATION = 0x07
        MQL_VISUAL_MODE = 0x08
        MQL_FRAME_MODE = 0x0C
        MQL_LICENSE_TYPE = 0x09
    
    class StringPropertyID:
        MQL_PROGRAM_NAME = 0x00
        MQL_PROGRAM_PATH = 0x01
    
    class LicenseType:
        LICENSE_FREE = 0x00
        LICENSE_DEMO = 0x01
        LICENSE_FULL = 0x02
        LICENSE_TIME = 0x03
    
    class ProgramType:
        PROGRAM_SCRIPT = 0x01
        PROGRAM_EXPERT = 0x02
        PROGRAM_INDICATOR = 0x04
