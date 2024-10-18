from connection import cursor

def checar_banco():
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS contatos(
                    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255),
                    tel VARCHAR(15) NOT NULL);''')
        
        cursor.execute('''INSERT INTO contatos (id, nome, tel) VALUES ('1', 'Rafael Abreu', '71999048364');''')

    except:
        print('Algo não deu certo!')

def novo_contato():
    try:
        tel = int(input('Digite o telefone: '))

        cursor.execute('''SELECT c.tel FROM contatos c WHERE tel = %s''', (tel,))
        exists = cursor.fetchone()

        if exists:
            print('Esse número já foi registrado!')

        else:
            nome = input('Digite o nome: ')
            cursor.execute('''INSERT INTO contatos(nome, tel) VALUES (%s, %s)''', (nome, tel))
            print('Contato salvo com sucesso!')

    except ValueError:
        print('Por favor, digite um valor inteiro!')

def editar_contato():
    
    try:
        tel = int(input('Digite o telefone que deseja editar: '))

        cursor.execute('''SELECT c.tel FROM contatos c WHERE tel = %s''', (tel,))
        exists = cursor.fetchone()

        if exists:
            try:
                novoTel = int(input('Digite o novo telefone: '))
                nome = input('Digite o nome: ')
                cursor.execute('''INSERT INTO contatos(nome, tel) VALUES (%s, %s)''', (nome, novoTel))
                print('Contato editado com sucesso!')
            except ValueError:
                print('Por favor, digite um valor inteiro!')
        
        else:
            print('Telefone não encontrado!')

    except ValueError:
        print('Por favor, digite um valor inteiro!')

def meu_contato():
    cursor.execute('''SELECT c.tel FROM contatos c WHERE id=1''')
    result = cursor.fetchone()
    print(result)

    cursor.close()

def editar_meu_contato():
    pass