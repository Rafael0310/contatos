import os

from comands import (
    checar_banco,
    novo_contato,
    editar_contato,
    meu_contato
)

os.system('cls' if os.name=='nt' else 'clear')

checar_banco()

while True:
    opt = int(input('\nO que deseja?\n1 - Novo contato\n2 - Editar contato\n3 - Consultar contatos\n4 - Consultar meu número\n5 - Editar meu número\n0 - Sair\n'))

    match opt:
        case 1:
            os.system('cls' if os.name=='nt' else 'clear')
            novo_contato()

        case 2:
            os.system('cls' if os.name=='nt' else 'clear')
            editar_contato()

        case 3:
            os.system('cls' if os.name=='nt' else 'clear')
            pass

        case 4:
            os.system('cls' if os.name=='nt' else 'clear')
            meu_contato()
        case 5:
            os.system('cls' if os.name=='nt' else 'clear')
            pass


        case 0:
            print('Encerrando...')
            exit()