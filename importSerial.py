import serial
porta = "COM7"
baud = 115200
arquivo = "logger.csv"
amostra = 3000
linha = 0

try:
    ser = serial.Serial(porta,baud)
    ser.flushInput()
    print("Abrindo Serial")

    while linha <= amostra:
         data = str(ser.readline().decode("utf-8"))
         print(data)
         file = open(arquivo,"a")
         file.write(data)
         linha = linha+1
    print("Final de leituras")
    file.close()
    ser.close()

except:
    print("ERRO: Porta Nao Encontrada ou Ocupada")


