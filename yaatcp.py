import pyuipc as fsuipc

fsuipc.open(fsuipc.SIM_FSX)

#text = 'Ciao cazzone...\n1 - Contact ground'
#data = [(13184,len(text)), (13050,'h')]
#fdata = fsuipc.prepare_data(data, False)
#fsuipc.write(fdata, [text, 100])

data = [(12816,224)]
rdata = fsuipc.prepare_data(data)
val = fsuipc.read(rdata)
bda=[val[0][i:(i+4)] for i in range(0,len(val[0]),4)]

fsuipc.close()
