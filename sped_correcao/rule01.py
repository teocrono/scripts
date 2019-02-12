## Arruma os NCM
## Os registros nos grupos C180 e C190 são populados pelo PCMOV
## inserindo NCM diferente, com isso preciso pegar o ncm do produto
## no 0200 e propagar nos C180 e C190

def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 01 - Inicializando",end=' - ')

    for i in ["C180","C190"]:
        upd = " UPDATE principal SET "
        upd = upd + " r6 = (SELECT distinct p.r8 "
        upd = upd + "         FROM principal as p "
        upd = upd + "         WHERE p.r1 = \"0200\" "
        upd = upd + "               AND p.r2 = principal.r5) "
        upd = upd + " WHERE r1 = \"" + i + "\" "
        print('-',end=' ')
        cursor.execute(upd)
        conexao.commit()

    print("Finalizado")


