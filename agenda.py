# Importando bibliotecas
import os
from dataclasses import dataclass

# Importando classes
from contato import Contato

contatos = []

@dataclass
class Agenda:

    @classmethod
    def novo_contato(cls) -> None:
        try:
            print('_______________________________________________')
            nome = input(' Insira o nome do contato que deseja adicionar: ')

            if not cls.verificar_contato(nome):
                tel = int(input('\n Insira o númeto de telefone: '))
                email = input('\n Insira o email: ')

                contatos.append(Contato(nome=nome, tel=tel, email=email))
                print('_______________________________________________')
                print(f' Novo contato adicionado!\n Nome: {contatos[-1].nome}\n Telefone: {contatos[-1].tel}\n Email: {contatos[-1].email}\n')
            
            else:
                print(f' O número de {nome} já foi adicionado!')

        except ValueError:
            print(' Por favor, insira um valor inteiro.')
        except:
            print(' Ops, algo deu errado.')

    def verificar_contato(nome) -> bool:
        if any(contato.nome == nome for contato in contatos):
            return True
        else:
            return False