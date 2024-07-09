import os
from dataclasses import dataclass

@dataclass
class Contato:
    nome: str
    tel: int
    email: str