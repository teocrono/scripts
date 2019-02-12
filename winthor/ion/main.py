import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import os

contador = []
s = requests.session()
data = {'Email':'login','Password':'senha'}
r = s.post('https://admin.ionvendas.com.br/', data = data)
while True:

    r1 = s.get('https://admin.ionvendas.com.br/Version/Index')
    b = r1.text
    #s.get('https://admin.ionvendas.com.br/Account/Logoff')


    soup = BeautifulSoup(b, 'html.parser')
    table = soup.find(id="usertable")
    data = []
    for i1 in table.find_all('tr'):
        cont = 0
        datatemp = []   
        for i2 in i1.find_all('td'):
            cont = cont + 1
            if cont == 1:
                datatemp.append(i2.text.split())
            if cont == 2:
                datatemp.append(i2.text.split())
            if cont == 4:
                datatemp.append(i2.text.split())
        data.append(datatemp)
    data = data[2:]

    now = datetime.now()
    day = str(now.day) if len(str(now.day)) == 2 else '0' + str(now.day)
    month = str(now.month) if len(str(now.month)) == 2 else '0' + str(now.month)
    now = day + '/' + month + '/' + str(now.year)

    dataf = []
    for i in data:
        if len(i[2]) > 0:
            if now == i[2][0]:
                dataf.append([i[2][1],i[0][0],' '.join(i[1])])
                if i[0][0] in [z[0] for z in contador]:
                    contador[[z[0] for z in contador].index(i[0][0])][1] = contador[[z[0] for z in contador].index(i[0][0])][1] + 1
                else:
                    contador.append([i[0][0],0])
    dataf = sorted(dataf,reverse=True)







    os.system('cls')
    print(datetime.now(),end=' -- ')
    print(now)
    print('------------------------------------------------------------------')
    print('  Ultima conexão - Cod  - RCA')
    print('------------------------------------------------------------------')
    cont = 0
    for i in dataf:
        cont = cont + 1
        cont1 = str(cont) if len(str(cont)) == 2 else '0' + str(cont)
        print('   ' + cont1,end=' = ')
        print(' - '.join(i))

    cc = 0
    while True:
        cc = cc + 1
        print('-',end='')
        time.sleep(10)
        if cc == 10:
            print('*')
            break





