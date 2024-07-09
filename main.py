# Importando bibliotecas
import os

# Importando classes
from agenda import Agenda

agenda = Agenda()

while True:
    opcao = int(input('''
_______________________________________________\n
                    Agenda
_______________________________________________\n
          1 - Adicionar contato
          2 - Remover contato
          3 - Listar contatos
          4 - Sair
_______________________________________________\n '''))
    
    match opcao:
        case 1:
            agenda.novo_contato()
        case 2:
            pass

        case 3:
            pass

        case 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Encerrando...')
            quit()
        
        case _:
            print('Opção inválida! Tente novamente.')