import pyuipc as fsuipc
import time

DWORD, WORD = (4,2)
call_frequency = 1

def hotkey(data):
    """
    Read any hotkey trapped
    """
    byte=[data[0][i:(i+DWORD)] for i in range(0,len(data[0]),DWORD)]


starttime = time.time()
try:
    #fsuipc.open(fsuipc.SIM_FSX)

    while True:
        #Ok, it works
        #text = '1 - Request Clearance\n'
        #data = [(int('3380',16),len(text)), (int('32FA',16),'h')]
        #fdata = fsuipc.prepare_data(data, False)
        #fsuipc.write(fdata, [text, 100])

        #data = [(int('0x3210',16),224)]
        #rdata = fsuipc.prepare_data(data)
        #call = fsuipc.read(rdata)
        #hotkey(call)

        print time.time() - starttime
    
        time.sleep(1.0/call_frequency - time.time()%(1/call_frequency))

    # Ok, Closing connection
    fsuipc.close()
    
except fsuipc.FSUIPCException as e:  
    print e.errorString
    exit(1)


