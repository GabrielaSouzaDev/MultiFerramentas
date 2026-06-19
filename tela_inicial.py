import customtkinter as ctk
from tela_base import limpar_conteudo
from config.colors import (
    COR_FUNDO,
    COR_SIDEBAR,
    COR_BOTAO_NAV,
    COR_BOTAO_HOVER,
    COR_TEXTO
)


def tela_inicial(frame):
    limpar_conteudo(frame)
    ctk.CTkLabel(frame,
                 text='Bem-vinda ao Hub de Aplicativos',
                 justify='center',
                 text_color= COR_TEXTO,
                 font=('Arial', 24, 'bold')).pack(pady=(30, 10))
    
    ctk.CTkLabel(frame,
                 text='Escolha uma ferramenta no menu à direita para começar.',
                 justify='center',
                 text_color=COR_TEXTO,
                 font=('Arial', 14)).pack(pady=10)
    
