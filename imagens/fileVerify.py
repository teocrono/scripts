#solução rápida para verificar se certos códigos existiam a sua imagem correspondente

import os.path

a = [159,266,287] #varios números, apaguei o restante

c = 0
for i in a:
    #verifica se existe o arquivo dentro da pasta
    r = os.path.exists('//192.168.0.214/FOTOS/WINTHOR/' + str(i) + '/' + str(i) + '.JPG')
    #se não existe o arquivo, incrementa c e imprime o código
    if r == False:
        c = c + 1
        print(i,end = ',')
print(c)