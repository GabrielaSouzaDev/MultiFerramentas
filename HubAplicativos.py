# Autor: Gabriela Souza
# Projeto - Ferramentas Essenciais

import customtkinter as ctk
import requests

# configuração visual
ctk.set_appearance_mode('light')

# palheta de cores (claro / escuro)
COR_FUNDO = ("#F7F5F0", "#1C1A17")       # Off-white terroso / Areia escuro
COR_SIDEBAR = ("#EADBC8", "#2C2621")     # Bege suave / Marrom argila profundo
COR_BOTAO_NAV = ("#DAC0A3", "#3E362E")   # Camurça / Marrom médio
COR_BOTAO_HOVER = ("#B0927A", "#54473E") # Terra queimada clara / Tom outonal
COR_TEXTO = ("#4A3E3D", "#F5EFE6")       # Marrom escuro para contraste / Areia claro

# janela principal
app = ctk.CTk()
app.geometry('900x600')
app.title('Hub De Aplicativos - Ferramentas Essenciais')
app.iconbitmap('./assets/ico/tools.ico')
app.configure(fg_color=COR_FUNDO)

# frame esquerda/menu
frame_menu = ctk.CTkFrame(app,
                          width=200,
                          height=600,
                          fg_color= COR_SIDEBAR)
frame_menu.pack(side='left',fill='y')


# frame direita/conteúdo
frame_conteudo = ctk.CTkFrame(app,
                              fg_color=COR_FUNDO)
frame_conteudo.pack(side='right', fill='both', expand='True')

# botões
ctk.CTkButton(frame_menu,
              fg_color=COR_BOTAO_NAV,
              text_color=('#0F0F0F'),
              hover_color=COR_BOTAO_HOVER,
              corner_radius=12,
              text='Juros Simples').pack(pady=10, padx=10)


# loop
app.mainloop()