## Para operações de saída, o CST deve ser preenchido com os valores de 01 a 49 ou 99.

def exec(conexao):    
    cursor = conexao.cursor()

    update = '''
        UPDATE principal SET 
            r2 = "49"
        WHERE 1=1
            and r1 = "C181" 
            and r2 in ("00","99")
            and r3 in ("5152","5102")
    '''
    cursor.execute(update)
    conexao.commit()
    print('REGISTROS C181 CFOP 5152 arrumado CST de 00 para 49')

    update = '''
        UPDATE principal SET
            r2 = "49"
        WHERE 1=1
            and r1 = "C185" 
            and r2 in ("00","99")
            and r3 in ("5152","5102")
    '''
    cursor.execute(update)
    conexao.commit()
    print('REGISTROS C185 CFOP 5152 arrumado CST de 00 para 49')