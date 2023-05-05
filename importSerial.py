import serial

#variaveis que podem ser alteradas
porta = "COM7"
baud = 115200
amostra = 3000
arquivo = "logger.csv"

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


