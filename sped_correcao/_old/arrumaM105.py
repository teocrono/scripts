## Campo obrigatório para Natureza do Crédito igual a Outras Operações com Direito a Crédito.
def exec(conexao):    
    cursor = conexao.cursor()

    update = '''
        UPDATE principal SET
            r10 = "Outras Operações com Direito a Crédito"
        WHERE r1 = "M105" AND r2 = "13"
    '''
    cursor.execute(update)
    conexao.commit()
    print('REGISTROS M105 arrumados')