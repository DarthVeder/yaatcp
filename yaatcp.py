import pyuipc as fsuipc
import time
import binascii
from maps.fsx import *

DWORD, WORD = (4,2) # common bytes variables
call_frequency = 1

def requestAicraftData():
    """
    Returns a tuple with aircraft latitude, longitude, FL, Altitude AMSL,
    true heading and mag dev at aircraft position
    """
    data = [ (int('6010',16),8) ] #,\
##             (ACFT_LONG,byte[ACFT_LONG]),
##             (ACFT_ALT,byte[ACFT_ALT]),
##             (ACFT_HDG_T,byte[ACFT_HDG_T]),
##             (ACFT_MAG_VAR,byte[ACFT_MAG_VAR]),
##             (ACFT_FL,byte[ACFT_FL]) ]

    pdata = fsuipc.prepare_data(data)
    acft_data = fsuipc.read(pdata)

    return acft_data

def requestMETAR(ICAOid):
    """
    Returns a METAR string given the 4 code ICAO. The METAR is
    in FSX enanched format.
    """
    # Writing both signature ('05FC'+ICAO) as 8 byte. Signature is the
    # required trigger.
    data = [ (WRITE_ICAO_FOR_METAR, byte[WRITE_ICAO_FOR_METAR]) ]
    signature = '05FC'
    pdata = fsuipc.prepare_data(data)
    fsuipc.write(pdata, [signature+ICAOid])

    time_delay = 250e-3 # ms. Required for FSX reading.
    time.sleep(time_delay)

    data = [ (METAR, byte[METAR]) ]
    pdata = fsuipc.prepare_data(data)
    metar = fsuipc.read(pdata)

    return metar[0].rstrip('\x00')
    

def hotkey(data):
    """
    Read any hotkey trapped
    """
    byte=[data[0][i:(i+DWORD)] for i in range(0,len(data[0]),DWORD)]


flight_in_progress = True
counter = 1
stop_counter = 10
starttime = time.time()
ICAO = ['EGGD','LIRF']
try:
    fsuipc.open(fsuipc.SIM_FSX)

    while flight_in_progress:
        # MENU ON - wip
        #text = '1 - Request Clearance\n'
        #data = [(int('3380',16),len(text)), (int('32FA',16),'h')]
        #fdata = fsuipc.prepare_data(data, False)
        #fsuipc.write(fdata, [text, 100])

        #data = [(int('0x3210',16),224)]
        #rdata = fsuipc.prepare_data(data)
        #call = fsuipc.read(rdata)
        #hotkey(call)
        # MENU OFF

        # WEATHER START
##        metar = requestMETAR('EDDF')
##        print(metar)
        #  WEATHER END

        acft_data = requestAicraftData()
        print(acft_data)
        
        print time.time() - starttime
    
        time.sleep(1.0/call_frequency - time.time()%(1/call_frequency))

        counter = counter + 1
        if counter > stop_counter:
            flight_in_progress = False

    # Ok, Closing connection
    fsuipc.close()
    
except fsuipc.FSUIPCException as e:  
    print e.errorString
    exit(1)


