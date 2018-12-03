*** Settings ***
Resource    ./../init.robot
Test Timeout    ${TIMEOUT}

*** Test Cases ***
Line bus test 01
    [Template]    TestLineBusApi
    216
    214
    215
    212
    213
    210
    211
    264
    29B
    151區
    218
    219
    133
    132
    131
    68延(繞國安國小)
    285副
    165
    95
    956
    93
    901副(原100副)
    658延
    67
    25
    26
    27
    20
    21
    23
    323區

Line bus test 02
    [Template]    TestLineBusApi
    9區
    668
    28
    29
    289
    288
    A2
    97
    281
    280
    283
    220
    285
    284
    155副
    286
    306區1
    306區2
    67繞
    181區1
    181區2
    211區
    58副
    677
    69繞
    263
    261
    123
    267
    266
    265

Line bus test 03
    [Template]    TestLineBusApi
    127
    128
    269
    29A
    69
    91
    A1
    59
    58
    55
    54
    58區1
    56
    51
    50
    53
    52
    99延
    58區2
    45區
    91延
    821
    811區
    290
    291
    164
    989
    199
    92繞
    310
    700

Line bus test 04
    [Template]    TestLineBusApi
    270
    271
    272
    273
    111
    128區
    276
    277
    278
    279
    5
    281副
    85
    75區1
    153副
    66
    305E
    305區
    213繞
    3
    20區
    7
    92
    206延
    308
    309
    201(原100)
    300
    301
    302
    303

Line bus test 05
    [Template]    TestLineBusApi
    304
    305
    306
    307
    108
    246
    226繞
    102
    90延
    101
    107
    105
    39
    98繞
    33
    32
    30
    37
    290繞
    35
    811
    160
    105區2
    70A
    70B
    14延
    699
    219延
    53區
    70
    151A

Line bus test 06
    [Template]    TestLineBusApi
    60
    61
    258
    63
    65
    179
    178
    252
    253
    250
    251
    172
    171
    170
    658
    850
    657
    153區
    306W
    90
    182
    183
    180
    181
    186
    185
    200延
    68延
    21延1
    500
    659

Line bus test 07
    [Template]    TestLineBusApi
    152區
    105區1
    661
    6
    900
    220繞
    142A
    163A
    163B
    142B
    8
    229
    228
    227
    226
    166
    167
    223
    161
    162
    163
    11
    12
    15
    14
    17
    19
    18
    266繞
    45延1
    99

Line bus test 08
    [Template]    TestLineBusApi
    989延
    89
    287
    21延2
    275
    151
    153
    152
    155
    154
    157
    156
    159
    158
    901(原100)
    352延
    82
    68繞
    238
    239
    235
    14副
    237
    677區
    232
    65延
    81
    48
    49
    272繞
    45

Line bus test 09
    [Template]    TestLineBusApi
    40
    41
    1
    323
    A3
    354
    326
    324
    325
    9
    305W
    688
    200
    203
    202
    142
    95副
    207
    206
    209
    208
    616
    617
    45延
    77
    75
    74
    73
    72
    71
    68

Line bus test 10
    [Template]    TestLineBusApi
    275區
    655
    79
    282
    306E
    98
    199延
    74繞
    357
    356
    355
    260
    353
    352
    351
    108區
    800
    359
    358

# Line bus test error 01
#     [Template]    TestLineBusApi

*** Keywords ***
TestLineBusApi
    [Arguments]    ${bus_num}
    ${resp}    Bus Test    ${bus_num}
    Verify Status Code As Expected    ${resp}    200
