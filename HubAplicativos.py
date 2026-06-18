# Autor: Gabriela Souza
# Projeto - Ferramentas Essenciais

# Importações necessárias para a aplicação
import customtkinter as ctk
import requests
import json
import os

# Palheta de cores do Projeto (claro / escuro)
COR_FUNDO = ("#F7F5F0", "#1C1A17")       # Off-white terroso / Areia escuro
COR_SIDEBAR = ("#EADBC8", "#2C2621")     # Bege suave / Marrom argila profundo
COR_BOTAO_NAV = ("#DAC0A3", "#3E362E")   # Camurça / Marrom médio
COR_BOTAO_HOVER = ("#B0927A", "#54473E") # Terra queimada clara / Tom outonal
COR_TEXTO = ("#4A3E3D", "#F5EFE6")       # Marrom escuro para contraste / Areia claro

# Preferenças de tema do usuário (claro/escuro) armazenadas em um arquivo JSON
PREFERENCIAS = 'preferencias-usuario.json'

# =========================  FUNÇÕES DE PREFERÊNCIAS E TEMAS =========================
# Função para carregar as preferências do usuário, retornando o tema atual (claro ou escuro)
def carregar_preferencias():
    if not os.path.exists(PREFERENCIAS):
        return 'light'

    try:
        with open(PREFERENCIAS, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados.get('preferencias', {}).get('tema', 'light')
    except Exception:
        return 'light'

# Função para salvar as preferências do usuário, atualizando o tema escolhido (claro ou escuro) no arquivo JSON
def salvar_preferencias(tema):
    dados = {}
    if os.path.exists(PREFERENCIAS):
        try:
            with open(PREFERENCIAS, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
        except Exception:
            dados = {}

    dados['preferencias'] = {'tema': tema}
    with open(PREFERENCIAS, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# Função para alternar entre modos claro e escuro
def tema():
    modo_atual = ctk.get_appearance_mode().lower()
    novo_modo = 'dark' if modo_atual == 'light' else 'light'
    ctk.set_appearance_mode(novo_modo)
    salvar_preferencias(novo_modo)
# =========================  FUNÇÕES DE PREFERÊNCIAS E TEMAS =========================

# =========================  CONFIGURAÇÕES JANELA PRINCIPAL =========================
# Configuração inicial do tema da aplicação com base nas preferências do usuário
current_theme = carregar_preferencias()
ctk.set_appearance_mode(current_theme)

app = ctk.CTk()
app.geometry('900x600')
app.resizable(False, False)
app.title('Hub De Aplicativos - Ferramentas Essenciais')
app.iconbitmap('./assets/ico/tools.ico')
app.configure(fg_color=COR_FUNDO)
# =========================  CONFIGURAÇÕES JANELA PRINCIPAL =========================

# =========================  ESTRUTURA DA INTERFACE GRÁFICA =========================
# Frame direita/menu
frame_menu = ctk.CTkFrame(app,
                          width=200,
                          height=480,
                          fg_color= COR_SIDEBAR,
                          corner_radius=15)
frame_menu.pack(side='right',
                expand=False,
                padx=8,
                pady=10)
frame_menu.pack_propagate(False)


# Frame esquerda/conteúdo
frame_conteudo = ctk.CTkFrame(app,
                              width=600,
                              height=580,
                              fg_color=COR_FUNDO)
frame_conteudo.pack(side='left', 
                    fill='y', 
                    expand=False, 
                    padx=10, 
                    pady=10)


# Título
ctk.CTkLabel(frame_menu,
             text='Menu Hub',
             text_color=COR_TEXTO,
             font=('Arial', 20, 'bold')).pack(pady=10)

# Botões
ctk.CTkButton(frame_menu,
              fg_color=COR_BOTAO_NAV,
              text_color=(COR_TEXTO),
              hover_color=COR_BOTAO_HOVER,
              corner_radius=8,
              width=180,
              height=40,
              border_color=COR_BOTAO_HOVER,
              border_width=1.4,
              font=('Arial', 12, 'bold'),
              text='Bot Telegram').pack(pady=5, padx=10)

ctk.CTkButton(frame_menu,
              fg_color=COR_BOTAO_NAV,
              text_color=(COR_TEXTO),
              hover_color=COR_BOTAO_HOVER,
              corner_radius=8,
              width=180,
              height=40,
              border_color=COR_BOTAO_HOVER,
              border_width=1.4,
              font=('Arial', 12, 'bold'),
              text='Sistema Consulta Brasil').pack(pady=5, padx=10)

ctk.CTkButton(frame_menu,
              fg_color=COR_BOTAO_NAV,
              text_color=(COR_TEXTO),
              hover_color=COR_BOTAO_HOVER,
              corner_radius=8,
              width=180,
              height=40,
              border_color=COR_BOTAO_HOVER,
              border_width=1.4,
              font=('Arial', 12, 'bold'),
              text='Youtube Downloader').pack(pady=5, padx=10)

ctk.CTkButton(frame_menu,
              fg_color=COR_BOTAO_NAV,
              text_color=(COR_TEXTO),
              hover_color=COR_BOTAO_HOVER,
              corner_radius=8,
              width=180,
              height=40,
              border_color=COR_BOTAO_HOVER,
              border_width=1.4,
              font=('Arial', 12, 'bold'),
              text='Conversor de Moedas').pack(pady=5, padx=10)

ctk.CTkButton(frame_menu,
              fg_color=COR_BOTAO_NAV,
              text_color=(COR_TEXTO),
              hover_color=COR_BOTAO_HOVER,
              corner_radius=8,
              width=180,
              height=40,
              border_color=COR_BOTAO_HOVER,
              border_width=1.4,
              font=('Arial', 12, 'bold'),
              text='Calculadora Juros').pack(pady=5, padx=10)

ctk.CTkButton(frame_menu,
              fg_color=COR_BOTAO_NAV,
              text_color=(COR_TEXTO),
              hover_color=COR_BOTAO_HOVER,
              corner_radius=8,
              width=180,
              height=40,
              border_color=COR_BOTAO_HOVER,
              border_width=1.4,
              font=('Arial', 12, 'bold'),
              text='Calculadora de IMC').pack(pady=(5, 20), padx=10)


# Modo claro/escuro
modo_var = ctk.IntVar(value=1 if current_theme == 'dark' else 0)
ctk.CTkSwitch(frame_menu,
           text='Modo Escuro',
           text_color=COR_TEXTO,
           font=('Arial', 12, 'bold'),
           variable=modo_var,
            command=tema).pack(pady=(10, 0), padx=10)

# Versão
ctk.CTkLabel(frame_menu,
             text='V1.0',
             text_color=COR_TEXTO,
             font=('Arial', 10, 'bold')).pack(pady=5, padx=10, side='bottom')
# =========================  ESTRUTURA DA INTERFACE GRÁFICA =========================

# ================================ LOOP DA APLICAÇÃO ================================
app.mainloop()