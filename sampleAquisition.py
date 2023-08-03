import sys
from time import sleep
import serial

#variaveis que podem ser alteradas
porta = "COM7"
baud = 9600
amostra = 1000
pesos = [0,1]

def ImportSerial(arquivo:str): 
        ser.flushInput()
        print("Abrindo Serial")
        linha = 0
        while linha <= amostra:
            data = str(ser.readline())
            data = data.replace("b","")
            data = data.replace("'","")
            data = data.replace("\\n","")
            data = data.replace("\\r","")
            print(data)
            file = open(arquivo,"a")
            file.write(data+"\n")
            linha = linha+1
        print("Final de leituras")
        file.close()

try:
    ser = serial.Serial(porta,baud)
except:
    print("ERRO: Porta Nao Encontrada ou Ocupada")
    sys.exit(-1)
for i in pesos:
    for x in range(4):
        print(str(x+1)+"º amostra de "+str(i)+"kg")
        sleep(10)
        print("LENDO")
        sleep(1)
        ImportSerial("amostra"+str(i)+"_"+str(x)+".csv")
