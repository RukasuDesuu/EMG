import serial

#variaveis que podem ser alteradas
porta = "COM4"
baud = 115200
amostra = 3000
arquivo = "semAtiv.csv"



try:
    ser = serial.Serial(porta,baud)
    ser.flushInput()
    print("Abrindo Serial")
    linha = 0
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


