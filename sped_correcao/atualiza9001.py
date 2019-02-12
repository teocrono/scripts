## rotina para atualizar o total no 9900 e no 9999
def exec(conexao):
    cursor = conexao.cursor()

    update = ""
    update = update + " UPDATE principal SET "
    update = update + " r3 = (select count(*) from principal p WHERE p.r1 = principal.r2)"
    update = update + " WHERE r1 = \"9900\""
    cursor.execute(update)
    conexao.commit()
    print("Atualizado os registros 9900")

    update = ""
    update = update + " UPDATE principal SET "
    update = update + " r2 = (select count(*) from principal WHERE r1 like \"99%\") + 1 "
    update = update + " where r1 = \"9990\""
    cursor.execute(update)
    conexao.commit()
    print("Atualizado o registro 9990")

    update = ""
    update = update + " UPDATE principal SET "
    update = update + " r2 = (select count(*) from principal)"
    update = update + " where r1 = \"9999\""
    cursor.execute(update)
    conexao.commit()
    print("Atualizado o registro 9999")

    ## atualiza o total bloco C
    update = ""
    update = update + " UPDATE principal SET "
    update = update + " r2 = (select count(*) from principal WHERE r1 like \"C%\")"
    update = update + " where r1 = \"C990\""
    cursor.execute(update)
    conexao.commit()
    print("Atualizado o registro C990")

    ## atualiza o total bloco M
    update = ""
    update = update + " UPDATE principal SET "
    update = update + " r2 = (select count(*) from principal WHERE r1 like \"M%\")"
    update = update + " where r1 = \"M990\""
    cursor.execute(update)
    conexao.commit()
    print("Atualizado o registro M990")
    