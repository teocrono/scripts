## Código inválido. Utilizar código da "Tabela de Códigos Situação Tributária do PIS/PASEP".
## Código inválido. Utilizar código da "Tabela de Códigos Situação Tributária da COFINS".
##
## função para arrumar o código do pis e cofins no grupo M205 e M605 respectiviamente
## o mesmo está informando de forma errada
def exec(conexao):    
    cursor = conexao.cursor()

    update = '''
        UPDATE principal SET
            r3 = "691201"
        WHERE 1=1
            and r1 = "M205" 
            and r3 = "6912"
    '''
    cursor.execute(update)
    conexao.commit()
    print('REGISTROS M205 mudado o valor do pis de 6912 para 691201')

    update = '''
        UPDATE principal SET
            r3 = "585601"
        where 1=1
            and r1 = "M605" 
            and r3 = "5856"
    '''
    cursor.execute(update)
    conexao.commit()
    print('REGISTROS M605 mudado o valor do cofins de 5856 para 585601')
