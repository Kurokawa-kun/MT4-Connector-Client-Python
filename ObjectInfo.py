class ObjectInfo:
    #  GUI�I�u�W�F�N�g�̎��
    class ObjectType:    #  �I���̒萔��MQL4��MQL5�Ō݊������Ȃ�
        EMPTY                   = -0x01
        OBJ_VLINE               =  0x00
        OBJ_HLINE               =  0x01
        OBJ_TREND               =  0x02
        OBJ_TRENDBYANGLE        =  0x03
        OBJ_CYCLES              =  0x14
        OBJ_CHANNEL             =  0x05
        OBJ_STDDEVCHANNEL       =  0x06
        OBJ_REGRESSION          =  0x04
        OBJ_PITCHFORK           =  0x13
        OBJ_GANNLINE            =  0x07
        OBJ_GANNFAN             =  0x08
        OBJ_GANNGRID            =  0x09
        OBJ_FIBO                =  0x0A
        OBJ_FIBOTIMES           =  0x0B
        OBJ_FIBOFAN             =  0x0C
        OBJ_FIBOARC             =  0x0D
        OBJ_FIBOCHANNEL         =  0x0F
        OBJ_EXPANSION           =  0x0E
        OBJ_RECTANGLE           =  0x10
        OBJ_TRIANGLE            =  0x11
        OBJ_ELLIPSE             =  0x12
        OBJ_ARROW_THUMB_UP      =  0x1D
        OBJ_ARROW_THUMB_DOWN    =  0x1E
        OBJ_ARROW_UP            =  0x1F
        OBJ_ARROW_DOWN          =  0x20
        OBJ_ARROW_STOP          =  0x21
        OBJ_ARROW_CHECK         =  0x22
        OBJ_ARROW_LEFT_PRICE    =  0x23
        OBJ_ARROW_RIGHT_PRICE   =  0x24
        OBJ_ARROW_BUY           =  0x25
        OBJ_ARROW_SELL          =  0x26
        OBJ_ARROW               =  0x16
        OBJ_TEXT                =  0x15
        OBJ_LABEL               =  0x17
        OBJ_BUTTON              =  0x19
        OBJ_BITMAP              =  0x1A
        OBJ_BITMAP_LABEL        =  0x18
        OBJ_EDIT                =  0x1B
        OBJ_EVENT               =  0x2A
        OBJ_RECTANGLE_LABEL     =  0x1C

    class IntegerPropertyID:
        OBJPROP_COLOR = 0x06
        OBJPROP_STYLE = 0x07
        OBJPROP_WIDTH = 0x08
        OBJPROP_BACK = 0x09
        OBJPROP_ZORDER = 0xCF
        OBJPROP_FILL = 0x407
        OBJPROP_HIDDEN = 0xD0
        OBJPROP_SELECTED = 0x11
        OBJPROP_READONLY = 0x404
        OBJPROP_TYPE = 0x12
        OBJPROP_TIME = 0x13
        OBJPROP_SELECTABLE = 0x3E8
        OBJPROP_CREATETIME = 0x3E6
        OBJPROP_LEVELS = 0xC8
        OBJPROP_LEVELCOLOR = 0xC9
        OBJPROP_LEVELSTYLE = 0xCA
        OBJPROP_LEVELWIDTH = 0xCB
        OBJPROP_ALIGN = 0x40C
        OBJPROP_FONTSIZE = 0x64
        OBJPROP_RAY_RIGHT = 0x3EC
        OBJPROP_ELLIPSE = 0x0B
        OBJPROP_ARROWCODE = 0x0E
        OBJPROP_TIMEFRAMES = 0x0F
        OBJPROP_ANCHOR = 0x3F3
        OBJPROP_XDISTANCE = 0x66
        OBJPROP_YDISTANCE = 0x67
        OBJPROP_STATE = 0x3FA
        OBJPROP_XSIZE = 0x3FB
        OBJPROP_YSIZE = 0x3FC
        OBJPROP_XOFFSET = 0x409
        OBJPROP_YOFFSET = 0x40A
        OBJPROP_BGCOLOR = 0x401
        OBJPROP_CORNER = 0x65
        OBJPROP_BORDER_TYPE = 0x405
        OBJPROP_BORDER_COLOR = 0x40B

    class DoublePropertyID:
        OBJPROP_PRICE = 0x14
        OBJPROP_LEVELVALUE = 0xCC
        OBJPROP_SCALE = 0x0C
        OBJPROP_ANGLE = 0x0D
        OBJPROP_DEVIATION = 0x10

    class StringPropertyID:
        OBJPROP_NAME = 0x40D
        OBJPROP_TEXT = 0x3E7
        OBJPROP_TOOLTIP = 0xCE
        OBJPROP_LEVELTEXT = 0xCD
        OBJPROP_FONT = 0x3E9
        OBJPROP_BMPFILE = 0x3F9

    class ObjectProperty:
        OBJPROP_TIME1           = 0x00
        OBJPROP_PRICE1          = 0x01
        OBJPROP_TIME2           = 0x02
        OBJPROP_PRICE2          = 0x03
        OBJPROP_TIME3           = 0x04
        OBJPROP_PRICE3          = 0x05
        OBJPROP_COLOR           = 0x06
        OBJPROP_STYLE           = 0x07
        OBJPROP_WIDTH           = 0x08
        OBJPROP_BACK            = 0x09
        OBJPROP_RAY             = 0x0A
        OBJPROP_ELLIPSE         = 0x0B
        OBJPROP_SCALE           = 0x0C
        OBJPROP_ANGLE           = 0x0D
        OBJPROP_ARROWCODE       = 0x0E
        OBJPROP_TIMEFRAMES      = 0x0F
        OBJPROP_DEVIATION       = 0x10
        OBJPROP_FONTSIZE        = 0x64
        OBJPROP_CORNER          = 0x65
        OBJPROP_XDISTANCE       = 0x66
        OBJPROP_YDISTANCE       = 0x67
        OBJPROP_FIBOLEVELS      = 0xC8
        OBJPROP_LEVELCOLOR      = 0xC9
        OBJPROP_LEVELSTYLE      = 0xCA
        OBJPROP_LEVELWIDTH      = 0xCB
        OBJPROP_FIRSTLEVEL      = 0xD2
        OBJPROP_FIRSTLEVEL_1    = 0xD3
        OBJPROP_FIRSTLEVEL_2    = 0xD4
        OBJPROP_FIRSTLEVEL_3    = 0xD5
        OBJPROP_FIRSTLEVEL_4    = 0xD6
        OBJPROP_FIRSTLEVEL_5    = 0xD7
        OBJPROP_FIRSTLEVEL_6    = 0xD8
        OBJPROP_FIRSTLEVEL_7    = 0xD9
        OBJPROP_FIRSTLEVEL_8    = 0xDA
        OBJPROP_FIRSTLEVEL_9    = 0xDB
        OBJPROP_FIRSTLEVEL_10   = 0xDC
        OBJPROP_FIRSTLEVEL_11   = 0xDD
        OBJPROP_FIRSTLEVEL_12   = 0xDE
        OBJPROP_FIRSTLEVEL_13   = 0xDF
        OBJPROP_FIRSTLEVEL_14   = 0xE0
        OBJPROP_FIRSTLEVEL_15   = 0xE1
        OBJPROP_FIRSTLEVEL_16   = 0xE2
        OBJPROP_FIRSTLEVEL_17   = 0xE3
        OBJPROP_FIRSTLEVEL_18   = 0xE4
        OBJPROP_FIRSTLEVEL_19   = 0xE5
        OBJPROP_FIRSTLEVEL_20   = 0xE6
        OBJPROP_FIRSTLEVEL_21   = 0xE7
        OBJPROP_FIRSTLEVEL_22   = 0xE8
        OBJPROP_FIRSTLEVEL_23   = 0xE9
        OBJPROP_FIRSTLEVEL_24   = 0xEA
        OBJPROP_FIRSTLEVEL_25   = 0xEB
        OBJPROP_FIRSTLEVEL_26   = 0xEC
        OBJPROP_FIRSTLEVEL_27   = 0xED
        OBJPROP_FIRSTLEVEL_28   = 0xEE
        OBJPROP_FIRSTLEVEL_29   = 0xEF
        OBJPROP_FIRSTLEVEL_30   = 0xF0
        OBJPROP_FIRSTLEVEL_31   = 0xF1

    class AlignMode:
        ALIGN_LEFT = 0x01
        ALIGN_CENTER = 0x02
        ALIGN_RIGHT = 0x00

    class BorderType:
        BORDER_FLAT = 0x00
        BORDER_RAISED = 0x01
        BORDER_SUNKEN = 0x02