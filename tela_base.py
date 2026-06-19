import customtkinter as ctk
from config.colors import (
    COR_FUNDO,
    COR_SIDEBAR,
    COR_BOTAO_NAV,
    COR_BOTAO_HOVER,
    COR_TEXTO
)

def limpar_conteudo(frame):
    for widget in frame.winfo_children():
        widget.destroy()
