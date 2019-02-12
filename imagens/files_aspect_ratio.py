#foi verificado que as imagens estavam com um tamanho muito grande
#solução para redimencionar e diminuir seu tamanho

import os
from PIL import Image
from resizeimage import resizeimage

#pasta com imagens de produtos raw
pasta_prods = '//192.168.0.214/FOTOS/WINTHOR/'

caminhos = []
for subdir, dirs, files in os.walk(pasta_prods):
    for file in files:
        #print os.path.join(subdir, file)
        #filepath = subdir + os.sep + file
        filepath = subdir + '/' + file

        if filepath.endswith(".jpg"):
            caminhos.append(filepath)
#caminhos = [os.path.join(pasta_prods, nome) for nome in os.listdir(pasta_prods)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
jpgs = [arq for arq in arquivos if arq.lower().endswith(".jpg")]

for arq in jpgs:
    try:
        image = Image.open(arq)
        if image.size[0] < 400:
            image = resizeimage.resize_width(image,image.size[0])#400
            image.save(arq,image.format,quality=80)
            print('arquivo alterado com sucesso' + arq)
        image.close()
    
    except:
        print('erro: ' + arq)


