MSG_DICT = {
    0: 'WM_NULL',                              # 0x0000
    1: 'WM_CREATE',                            # 0x0001
    2: 'WM_DESTROY',                           # 0x0002
    3: 'WM_MOVE',                              # 0x0003
    5: 'WM_SIZE',                              # 0x0005
    6: 'WM_ACTIVATE',                          # 0x0006
    7: 'WM_SETFOCUS',                          # 0x0007
    8: 'WM_KILLFOCUS',                         # 0x0008
    10: 'WM_ENABLE',                           # 0x000A
    11: 'WM_SETREDRAW',                        # 0x000B
    12: 'WM_SETTEXT',                          # 0x000C
    13: 'WM_GETTEXT',                          # 0x000D
    14: 'WM_GETTEXTLENGTH',                    # 0x000E
    15: 'WM_PAINT',                            # 0x000F
    16: 'WM_CLOSE',                            # 0x0010
    17: 'WM_QUERYENDSESSION',                  # 0x0011
    19: 'WM_QUERYOPEN',                        # 0x0013
    22: 'WM_ENDSESSION',                       # 0x0016
    18: 'WM_QUIT',                             # 0x0012
    20: 'WM_ERASEBKGND',                       # 0x0014
    21: 'WM_SYSCOLORCHANGE',                   # 0x0015
    24: 'WM_SHOWWINDOW',                       # 0x0018
    26: 'WM_WININICHANGE',                     # 0x001A
    27: 'WM_DEVMODECHANGE',                    # 0x001B
    28: 'WM_ACTIVATEAPP',                      # 0x001C
    29: 'WM_FONTCHANGE',                       # 0x001D
    30: 'WM_TIMECHANGE',                       # 0x001E
    31: 'WM_CANCELMODE',                       # 0x001F
    32: 'WM_SETCURSOR',                        # 0x0020
    33: 'WM_MOUSEACTIVATE',                    # 0x0021
    34: 'WM_CHILDACTIVATE',                    # 0x0022
    35: 'WM_QUEUESYNC',                        # 0x0023
    36: 'WM_GETMINMAXINFO',                    # 0x0024
    38: 'WM_PAINTICON',                        # 0x0026
    39: 'WM_ICONERASEBKGND',                   # 0x0027
    40: 'WM_NEXTDLGCTL',                       # 0x0028
    42: 'WM_SPOOLERSTATUS',                    # 0x002A
    43: 'WM_DRAWITEM',                         # 0x002B
    44: 'WM_MEASUREITEM',                      # 0x002C
    45: 'WM_DELETEITEM',                       # 0x002D
    46: 'WM_VKEYTOITEM',                       # 0x002E
    47: 'WM_CHARTOITEM',                       # 0x002F
    48: 'WM_SETFONT',                          # 0x0030
    49: 'WM_GETFONT',                          # 0x0031
    50: 'WM_SETHOTKEY',                        # 0x0032
    51: 'WM_GETHOTKEY',                        # 0x0033
    55: 'WM_QUERYDRAGICON',                    # 0x0037
    57: 'WM_COMPAREITEM',                      # 0x0039
    61: 'WM_GETOBJECT',                        # 0x003D
    65: 'WM_COMPACTING',                       # 0x0041
    68: 'WM_COMMNOTIFY',                       # 0x0044
    70: 'WM_WINDOWPOSCHANGING',                # 0x0046
    71: 'WM_WINDOWPOSCHANGED',                 # 0x0047
    72: 'WM_POWER',                            # 0x0048
    74: 'WM_COPYDATA',                         # 0x004A
    75: 'WM_CANCELJOURNAL',                    # 0x004B
    78: 'WM_NOTIFY',                           # 0x004E
    80: 'WM_INPUTLANGCHANGEREQUEST',           # 0x0050
    81: 'WM_INPUTLANGCHANGE',                  # 0x0051
    82: 'WM_TCARD',                            # 0x0052
    83: 'WM_HELP',                             # 0x0053
    84: 'WM_USERCHANGED',                      # 0x0054
    85: 'WM_NOTIFYFORMAT',                     # 0x0055
    123: 'WM_CONTEXTMENU',                     # 0x007B
    124: 'WM_STYLECHANGING',                   # 0x007C
    125: 'WM_STYLECHANGED',                    # 0x007D
    126: 'WM_DISPLAYCHANGE',                   # 0x007E
    127: 'WM_GETICON',                         # 0x007F
    128: 'WM_SETICON',                         # 0x0080
    129: 'WM_NCCREATE',                        # 0x0081
    130: 'WM_NCDESTROY',                       # 0x0082
    131: 'WM_NCCALCSIZE',                      # 0x0083
    132: 'WM_NCHITTEST',                       # 0x0084
    133: 'WM_NCPAINT',                         # 0x0085
    134: 'WM_NCACTIVATE',                      # 0x0086
    135: 'WM_GETDLGCODE',                      # 0x0087
    136: 'WM_SYNCPAINT',                       # 0x0088
    160: 'WM_NCMOUSEMOVE',                     # 0x00A0
    161: 'WM_NCLBUTTONDOWN',                   # 0x00A1
    162: 'WM_NCLBUTTONUP',                     # 0x00A2
    163: 'WM_NCLBUTTONDBLCLK',                 # 0x00A3
    164: 'WM_NCRBUTTONDOWN',                   # 0x00A4
    165: 'WM_NCRBUTTONUP',                     # 0x00A5
    166: 'WM_NCRBUTTONDBLCLK',                 # 0x00A6
    167: 'WM_NCMBUTTONDOWN',                   # 0x00A7
    168: 'WM_NCMBUTTONUP',                     # 0x00A8
    169: 'WM_NCMBUTTONDBLCLK',                 # 0x00A9
    171: 'WM_NCXBUTTONDOWN',                   # 0x00AB
    172: 'WM_NCXBUTTONUP',                     # 0x00AC
    173: 'WM_NCXBUTTONDBLCLK',                 # 0x00AD
    254: 'WM_INPUT_DEVICE_CHANGE',             # 0x00FE
    255: 'WM_INPUT',                           # 0x00FF
    256: 'WM_KEYFIRST',                        # 0x0100
    257: 'WM_KEYUP',                           # 0x0101
    258: 'WM_CHAR',                            # 0x0102
    259: 'WM_DEADCHAR',                        # 0x0103
    260: 'WM_SYSKEYDOWN',                      # 0x0104
    261: 'WM_SYSKEYUP',                        # 0x0105
    262: 'WM_SYSCHAR',                         # 0x0106
    263: 'WM_SYSDEADCHAR',                     # 0x0107
    265: 'WM_UNICHAR',                         # 0x0109
    264: 'WM_KEYLAST',                         # 0x0108
    269: 'WM_IME_STARTCOMPOSITION',            # 0x010D
    270: 'WM_IME_ENDCOMPOSITION',              # 0x010E
    271: 'WM_IME_COMPOSITION',                 # 0x010F
    272: 'WM_INITDIALOG',                      # 0x0110
    273: 'WM_COMMAND',                         # 0x0111
    274: 'WM_SYSCOMMAND',                      # 0x0112
    275: 'WM_TIMER',                           # 0x0113
    276: 'WM_HSCROLL',                         # 0x0114
    277: 'WM_VSCROLL',                         # 0x0115
    278: 'WM_INITMENU',                        # 0x0116
    279: 'WM_INITMENUPOPUP',                   # 0x0117
    281: 'WM_GESTURE',                         # 0x0119
    282: 'WM_GESTURENOTIFY',                   # 0x011A
    287: 'WM_MENUSELECT',                      # 0x011F
    288: 'WM_MENUCHAR',                        # 0x0120
    289: 'WM_ENTERIDLE',                       # 0x0121
    290: 'WM_MENURBUTTONUP',                   # 0x0122
    291: 'WM_MENUDRAG',                        # 0x0123
    292: 'WM_MENUGETOBJECT',                   # 0x0124
    293: 'WM_UNINITMENUPOPUP',                 # 0x0125
    294: 'WM_MENUCOMMAND',                     # 0x0126
    295: 'WM_CHANGEUISTATE',                   # 0x0127
    296: 'WM_UPDATEUISTATE',                   # 0x0128
    297: 'WM_QUERYUISTATE',                    # 0x0129
    306: 'WM_CTLCOLORMSGBOX',                  # 0x0132
    307: 'WM_CTLCOLOREDIT',                    # 0x0133
    308: 'WM_CTLCOLORLISTBOX',                 # 0x0134
    309: 'WM_CTLCOLORBTN',                     # 0x0135
    310: 'WM_CTLCOLORDLG',                     # 0x0136
    311: 'WM_CTLCOLORSCROLLBAR',               # 0x0137
    312: 'WM_CTLCOLORSTATIC',                  # 0x0138
    512: 'WM_MOUSEFIRST',                      # 0x0200
    513: 'WM_LBUTTONDOWN',                     # 0x0201
    514: 'WM_LBUTTONUP',                       # 0x0202
    515: 'WM_LBUTTONDBLCLK',                   # 0x0203
    516: 'WM_RBUTTONDOWN',                     # 0x0204
    517: 'WM_RBUTTONUP',                       # 0x0205
    518: 'WM_RBUTTONDBLCLK',                   # 0x0206
    519: 'WM_MBUTTONDOWN',                     # 0x0207
    520: 'WM_MBUTTONUP',                       # 0x0208
    521: 'WM_MBUTTONDBLCLK',                   # 0x0209
    522: 'WM_MOUSEWHEEL',                      # 0x020A
    523: 'WM_XBUTTONDOWN',                     # 0x020B
    524: 'WM_XBUTTONUP',                       # 0x020C
    525: 'WM_XBUTTONDBLCLK',                   # 0x020D
    526: 'WM_MOUSEHWHEEL',                     # 0x020E
    528: 'WM_PARENTNOTIFY',                    # 0x0210
    529: 'WM_ENTERMENULOOP',                   # 0x0211
    530: 'WM_EXITMENULOOP',                    # 0x0212
    531: 'WM_NEXTMENU',                        # 0x0213
    532: 'WM_SIZING',                          # 0x0214
    533: 'WM_CAPTURECHANGED',                  # 0x0215
    534: 'WM_MOVING',                          # 0x0216
    536: 'WM_POWERBROADCAST',                  # 0x0218
    537: 'WM_DEVICECHANGE',                    # 0x0219
    544: 'WM_MDICREATE',                       # 0x0220
    545: 'WM_MDIDESTROY',                      # 0x0221
    546: 'WM_MDIACTIVATE',                     # 0x0222
    547: 'WM_MDIRESTORE',                      # 0x0223
    548: 'WM_MDINEXT',                         # 0x0224
    549: 'WM_MDIMAXIMIZE',                     # 0x0225
    550: 'WM_MDITILE',                         # 0x0226
    551: 'WM_MDICASCADE',                      # 0x0227
    552: 'WM_MDIICONARRANGE',                  # 0x0228
    553: 'WM_MDIGETACTIVE',                    # 0x0229
    560: 'WM_MDISETMENU',                      # 0x0230
    561: 'WM_ENTERSIZEMOVE',                   # 0x0231
    562: 'WM_EXITSIZEMOVE',                    # 0x0232
    563: 'WM_DROPFILES',                       # 0x0233
    564: 'WM_MDIREFRESHMENU',                  # 0x0234
    568: 'WM_POINTERDEVICECHANGE',             # 0x0238
    569: 'WM_POINTERDEVICEINRANGE',            # 0x0239
    570: 'WM_POINTERDEVICEOUTOFRANGE',         # 0x023A
    576: 'WM_TOUCH',                           # 0x0240
    577: 'WM_NCPOINTERUPDATE',                 # 0x0241
    578: 'WM_NCPOINTERDOWN',                   # 0x0242
    579: 'WM_NCPOINTERUP',                     # 0x0243
    581: 'WM_POINTERUPDATE',                   # 0x0245
    582: 'WM_POINTERDOWN',                     # 0x0246
    583: 'WM_POINTERUP',                       # 0x0247
    585: 'WM_POINTERENTER',                    # 0x0249
    586: 'WM_POINTERLEAVE',                    # 0x024A
    587: 'WM_POINTERACTIVATE',                 # 0x024B
    588: 'WM_POINTERCAPTURECHANGED',           # 0x024C
    589: 'WM_TOUCHHITTESTING',                 # 0x024D
    590: 'WM_POINTERWHEEL',                    # 0x024E
    591: 'WM_POINTERHWHEEL',                   # 0x024F
    593: 'WM_POINTERROUTEDTO',                 # 0x0251
    594: 'WM_POINTERROUTEDAWAY',               # 0x0252
    595: 'WM_POINTERROUTEDRELEASED',           # 0x0253
    641: 'WM_IME_SETCONTEXT',                  # 0x0281
    642: 'WM_IME_NOTIFY',                      # 0x0282
    643: 'WM_IME_CONTROL',                     # 0x0283
    644: 'WM_IME_COMPOSITIONFULL',             # 0x0284
    645: 'WM_IME_SELECT',                      # 0x0285
    646: 'WM_IME_CHAR',                        # 0x0286
    648: 'WM_IME_REQUEST',                     # 0x0288
    656: 'WM_IME_KEYDOWN',                     # 0x0290
    657: 'WM_IME_KEYUP',                       # 0x0291
    673: 'WM_MOUSEHOVER',                      # 0x02A1
    675: 'WM_MOUSELEAVE',                      # 0x02A3
    672: 'WM_NCMOUSEHOVER',                    # 0x02A0
    674: 'WM_NCMOUSELEAVE',                    # 0x02A2
    689: 'WM_WTSSESSION_CHANGE',               # 0x02B1
    704: 'WM_TABLET_FIRST',                    # 0x02C0
    735: 'WM_TABLET_LAST',                     # 0x02DF
    736: 'WM_DPICHANGED',                      # 0x02E0
    738: 'WM_DPICHANGED_BEFOREPARENT',         # 0x02E2
    739: 'WM_DPICHANGED_AFTERPARENT',          # 0x02E3
    740: 'WM_GETDPISCALEDSIZE',                # 0x02E4
    768: 'WM_CUT',                             # 0x0300
    769: 'WM_COPY',                            # 0x0301
    770: 'WM_PASTE',                           # 0x0302
    771: 'WM_CLEAR',                           # 0x0303
    772: 'WM_UNDO',                            # 0x0304
    773: 'WM_RENDERFORMAT',                    # 0x0305
    774: 'WM_RENDERALLFORMATS',                # 0x0306
    775: 'WM_DESTROYCLIPBOARD',                # 0x0307
    776: 'WM_DRAWCLIPBOARD',                   # 0x0308
    777: 'WM_PAINTCLIPBOARD',                  # 0x0309
    778: 'WM_VSCROLLCLIPBOARD',                # 0x030A
    779: 'WM_SIZECLIPBOARD',                   # 0x030B
    780: 'WM_ASKCBFORMATNAME',                 # 0x030C
    781: 'WM_CHANGECBCHAIN',                   # 0x030D
    782: 'WM_HSCROLLCLIPBOARD',                # 0x030E
    783: 'WM_QUERYNEWPALETTE',                 # 0x030F
    784: 'WM_PALETTEISCHANGING',               # 0x0310
    785: 'WM_PALETTECHANGED',                  # 0x0311
    786: 'WM_HOTKEY',                          # 0x0312
    791: 'WM_PRINT',                           # 0x0317
    792: 'WM_PRINTCLIENT',                     # 0x0318
    793: 'WM_APPCOMMAND',                      # 0x0319
    794: 'WM_THEMECHANGED',                    # 0x031A
    797: 'WM_CLIPBOARDUPDATE',                 # 0x031D
    798: 'WM_DWMCOMPOSITIONCHANGED',           # 0x031E
    799: 'WM_DWMNCRENDERINGCHANGED',           # 0x031F
    800: 'WM_DWMCOLORIZATIONCOLORCHANGED',     # 0x0320
    801: 'WM_DWMWINDOWMAXIMIZEDCHANGE',        # 0x0321
    803: 'WM_DWMSENDICONICTHUMBNAIL',          # 0x0323
    806: 'WM_DWMSENDICONICLIVEPREVIEWBITMAP',  # 0x0326
    831: 'WM_GETTITLEBARINFOEX',               # 0x033F
    856: 'WM_HANDHELDFIRST',                   # 0x0358
    863: 'WM_HANDHELDLAST',                    # 0x035F
    864: 'WM_AFXFIRST',                        # 0x0360
    895: 'WM_AFXLAST',                         # 0x037F
    896: 'WM_PENWINFIRST',                     # 0x0380
    911: 'WM_PENWINLAST',                      # 0x038F
    32768: 'WM_APP',                           # 0x8000
    1024: 'WM_USER',                           # 0x0400
}
