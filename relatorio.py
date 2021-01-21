f = open("pDOWNLOAD_20190505113000_1005_1.avi.txt", "r")
relatorio = open('resultados.txt', 'w')

frame = 0
ave = 0
per = ""
for x in f:
    if "Objects:" in x:
      frame = frame + 1
    if "Ave:" in x:
      ave = ave + 1
      aux = x.replace("Ave:","")
      per = aux.rstrip() + "," + per
    if "FPS:" in x:
        linha = str(frame) +","+ str(ave)+","+ per[:-1]
        print(linha[:-1])
        relatorio.write(linha[:-1]+'\n')
        ave = 0
        per = " "

relatorio.close()

