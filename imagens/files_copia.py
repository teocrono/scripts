#solução rápia para copiar arquivos de uma pasta para outra com algumas regras

import os

#pasta com imagens de produtos raw
pasta_all = '//192.168.0.214/FOTOS/PRODUTOS/'
pasta_prods = '//192.168.0.214/FOTOS/WINTHOR/'

#pega todas as imagens dentro desta pasta
caminhos = [os.path.join(pasta_all, nome) for nome in os.listdir(pasta_all)]
#filtra para pegar só os arquivos
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
#filtra para pegar só imagem .jpg
jpgs = [arq for arq in arquivos if arq.lower().endswith(".jpg")]
#envia o arquivo para a pasta correta e imprimi o que deu certo e o que já existe
for arq in jpgs:
    try:
        codprod = arq[arq.rfind('/')+1:arq.rfind('.')]
        pasta_atual = pasta_prods + codprod
        os.makedirs(pasta_atual)
        os.link(arq, pasta_prods + '/' + codprod + '/' + codprod + '.jpg')
        print(codprod + ' = arquivo copiado com sucesso')
    except:
        print(codprod + ' = arquivo já existente')

