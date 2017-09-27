"""
Data map based on FSUIPC offset.
"""

COM1 = int('034E',16) # 0x2345 => 123.45, 1 is implied
TRANSPONDER = int('0354',16) # 0x1200 => 1200 set
AIRCRAFT_ON_GROUND = int('0366',16) # 1 yes 0 no
AIRCRAFT_HGD_T = int('0580',16) # deg
NEAREST_APT = int('0658',16)
HOT_KEY_COUNTER = int('32FE',16)
TEXT_DSP_ON = int('32FA',16)
TEXT_DSP_MSG = int('3380',16)
ACFT_LAT = int('6010',16) # nn.nn
ACFT_LONG = int('6018',16) # nn.nn
ACFT_HEIGHT = int('6028',16) # m
ACFT_MAG_VAR = int('6028',16)
WRITE_ICAO_FOR_METAR = int('CC04',16)
METAR = int('B800',16)

byte = {COM1: 2, TRANSPONDER: 2, \
        AIRCRAFT_ON_GROUND: 2, NEAREST_APT: 120,\
        HOT_KEY_COUNTER: 1, TEXT_DSP_ON: 2, TEXT_DSP_MSG: 128,\
        ACFT_LAT: 8, ACFT_LONG: 8, ACFT_HEIGHT: 8, ACFT_MAG_VAR: 8,\
        WRITE_ICAO_FOR_METAR: 8, METAR: 2048}
