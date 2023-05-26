import serial

#variaveis que podem ser alteradas
porta = "COM7"
baud = 9600
amostra = 1000
arquivo = "amostraSemAtividade_0.csv"



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
    ser.close()
    file.close()

except:
    print("ERRO: Porta Nao Encontrada ou Ocupada")


