# ======================================================= #
# INÍCIO DA CLASSE BASE
# ======================================================= #

# Importando TODO conteúdo do módulo de interfaces
# gráficas 'tkinter'
from tkinter import *
from tkinter import messagebox
import numpy as np
from math import *

class JanelaBase():
    'Classe geradora da janela gráfica'    

    # Importando um pacote interno do python
    import sys

    # Listando todos os atributos e método públicos
    __all__ = [
        'expressao', 'conteudoCaixa', 'rodarJanela'
    ]

    def __init__(
        self       : object,
        comprimento: [int,float] = 425,
        altura     : [int,float] = 445,
        titulo     : str         = '𝓒𝓐𝓛𝓒𝓤𝓛𝓐𝓓𝓞𝓡𝓐',
        corFundo   : str         = 'light blue',

##=============================================================================================================
        #Arquivo que será usado para guardar os erros
        #durante execução do prorama
        arquivoErros     : 'file'      = sys.stderr, # sys.stderr: Texto no Shell Vermelho
                                                     # sys.stdout: Texto no Shell Azul
                                                     # yourFile  : Texto no Arquivo '.txt' dado
        #Arquivo que será usado para montar um histórico
        #com todas as operações realizadas 
        arquivoHistorico     : 'file'      = sys.stderr # sys.stderr: Texto no Shell Vermelho
                                                        # sys.stdout: Texto no Shell Azul
                                                        # yourFile  : Texto no Arquivo '.txt' dado
        ):

        #Printando um título para os arquivos txt
        print('\nHISTÓRICO DE EXPRESSÕES:', file= arquivoHistorico)
        print('\nHISTÓRICO DE ERROS:', file=arquivoErros)
        self.arquivoErros = arquivoErros

        #Tornando variáveis 'visíveis' fora do método construtor
        #serão úteis para mudar certas características da janela
        #durante a mudança do frame normal para o frame científica
        #Os argumentos default serão adotados no frame científica
        #No frame normal faremos certas alterações
        self.comprimentoPadrao = comprimento
        self.alturaPadrao = altura
        self.titulo = titulo
        self.corFundo= corFundo
##===========================================================================================================


        'Construindo estrutura da janela base'
        self.lista=[]
        # Instanciando uma janela do Tkinter
        self.janela = Tk()


       # Definindo as configurações da janela gráfica
        self.__configurarJanela(
            comprimento, altura, titulo, corFundo
        )
        
        # Criando os atributos necessários
        self.__criarAtributos()

        # Criando e posicionando os widgets na janela
        self.__criarWidgets()

        # Definindo ações de teclado
        self.__definirAcoesTeclado()

        return None

    def __criarAtributos(
        self: object
        ):
        'Criando os atributos necessarios'

        # Criando o atributo 'expressao' para armazenar
        # o conteúdo a ser resolvido pelo python
        self.expressao = ''
        self.lista = []

        # Criando um atributo com uma variável de janela
        # gráfica, do tipo str, para armazenar o conteúdo
        # a ser digitado/exibido na caixa de textoCaixa = StringVar()
        self.conteudoCaixa = StringVar(self.janela)
        
        
        return None


    # Método Privado
    def __configurarJanela(
        self       : object,
        comprimento: [int,float],
        altura     : [int,float],
        titulo     : str,
        corFundo   : str,
        ):
        'Configurando alguns parâmetros da janela'

        # Definindo a cor de fundo da janela gráfica
        self.janela.configure(background=corFundo)

        # Definindo o título da janela gráfica
        self.janela.title(titulo)

        # Definindo o tamanho da janela gráfica
        self.janela.geometry(f'{comprimento}x{altura}')

        return None    

    # Método Privado
    def __criarWidgets(
        self: object
        ):
        'Criando e posicionando os widgets na janela'
        # Criando caixa para digitação de textos na janela
        # gráfica e direcionando seu conteúdo ao atributo
        # 'equação'
        self.caixaDaEquacao = Entry(
            self.janela,
            textvariable=self.conteudoCaixa,
            borderwidth=10,
            fg="navy blue",
            justify="center",
            font="Helvetica 27 bold"
        )

        # Posicionando a caixa de texto considerando a
        # mescalgem de 5 colunas de espaço, tendo 70 px
        # de distância entre a borda desse espaço e a caixa
        self.caixaDaEquacao.grid(
            columnspan=1,
            ipadx=0,
            ipady=0
        )
    
        self.caixaDaEquacao.configure(font="Helvetica 27 bold")

        # Definindo um valor inicial/padrão para a caixa
        # de texto
        self.conteudoCaixa.set('𝓑𝓞𝓡𝓐 𝓕𝓐𝓩𝓔𝓡 𝓒𝓞𝓝𝓣𝓐')



        # Gerando uma barra de menu para janela
        self.barraMenu = Menu(
            self.janela
        )

        # Gerando a estrutura para receber o conteudo
        # do futuro menu 'Constantes' e associando
        # à barra de menu
        self.menuConstantes = Menu(
            self.barraMenu,
            tearoff=False # Limpando a estrutura
        )
        # Adicionando o conteúdo 'e' com a ação
        # atribuida no 'command'
        self.menuConstantes.add_command(
            label='e',
            command=lambda:self._JanelaBase__adicionaValor(e)
        )
        # Adicionando o conteúdo 'pi' com sua
        # respectiva ação
        self.menuConstantes.add_command(
            label='𝝿',
            command=lambda:self._JanelaBase__adicionaValor(pi)
        )
        
        # Posicionando o menu "Constantes" na barra
        # de Menu
        self.barraMenu.add_cascade(
            label='𝓒𝓸𝓷𝓼𝓽𝓪𝓷𝓽𝓮𝓼',
            menu=self.menuConstantes
        )

        # Adicionando um separador à barra de menu
        self.barraMenu.add_command(
            label="★",
            activebackground=self.barraMenu.cget(
                "background"
            )
        )

        # Adicionando um botao de escolha chamado
        # 'Normal', usado para ativar o modo 'normal'
        # da calculadora
        self.barraMenu.add_radiobutton(
            label='𝓝𝓸𝓻𝓶𝓪𝓵',
            indicator=True,
            command=lambda:self.__mudarJanela('normal')
        )


#=====================================================================================

        # Adicionando mais um separador à barra de menu
        self.barraMenu.add_command(
            label="★",
            activebackground=self.barraMenu.cget(
                "background"
            )
        )
#=====================================================================================
        # Adicionando um botao de escolha chamado
        # 'Cientifica', usado para ativar o modo
        # 'cientifica' da calculadora
        self.barraMenu.add_radiobutton(
            label='𝓒𝓲𝓮𝓷𝓽𝓲𝓯𝓲𝓬𝓪',
            indicator=True,
            command=lambda:self.__mudarJanela('cientifica')
        )
        self.janela.config( bg='light blue')
        #Ativando o modo 'normal' de início
        self.barraMenu.invoke(3)
        # O valor é 3, pois foi o quarto elemento
        # a ser inserido no menu.

        # Configurando/habilitando menu na janela
        self.janela.config(
            menu=self.barraMenu,
        )
        
        return None

    def __mudarJanela(
        self: object,
        tipo: str = 'normal'
        ):
        'Mudando configuração da janela'

        # Verificando se tem algum frame aberto
        try:
            # Fechando o frame atual
            self.__frame.destroy()

        except: pass

        # Atualizando frame
        if   (tipo == 'normal'):
            self.__frame = FrameNormal(self).frame
##=================================================================================================================
            # Definindo as configurações da janela gráfica quando entrar no frame 'normal'
            self.__configurarJanela(
                337,
                325,
                self.titulo,
                self.corFundo
            )
            self.caixaDaEquacao.configure(font="Helvetica 22 bold")


        #Definindo as configurações da janela gráfica quando entrar no frame 'cientifica'
        #todas as variáveis de configurarJanela já foram definidas anteriormente
        #como argumento default
        elif (tipo == 'cientifica'):
            self.__frame = FrameCientifica(self).frame
            self.__configurarJanela(
                self.comprimentoPadrao,
                self.alturaPadrao,
                self.titulo,
                self.corFundo
            )
            self.caixaDaEquacao.configure(font="Helvetica 27 bold")
            
        # Posicioanando frame
        self.__frame.grid()        

        return None

    # Método Privado
    def __adicionaValor(
        self : object,
        valor: [int,str]
        ):
        'Adicionando valor à expressão'

        # Adicionando o valor à expressao
        self.expressao += str(valor)
        
##===============================================================================================================================
        #Adiciona o valor à lista
        #Lista criada para guardar as expressoes e seus resultados na forma de itens de uma lista
        #Lista esta que será usada para criar o botão que apagará o útilo item dessa lista
        #botao 'apagar'
        self.lista.append(str(valor))
#===============================================================================================================================

        # Atualizando expressão na caixa
        self.conteudoCaixa.set(self.expressao)

        return None

    # Método Privado
    def __fecharJanela(
        self: object
        ):
        'Fechando janela'

        # Excutando fechamento
        self.janela.destroy()

        return None

    # Método Privado
    def __limpar(
        self : object,
        event: 'Event' = None
        ):
        "Limpando entrada de texto e variavel 'expressao'"

        # Limpando expressao
        self.expressao = ''
##===================================================================================================================
        #Atualiza a lista, esvaziando-a
        self.lista=[]

        #Printa no arquivo o uso do botão clear
        #Indicando que a operação anterior foi excluida
        print("Clear", file= arquivoHistorico)

        # Limpando caixa de texto
        self.conteudoCaixa.set('')
        return None

     #Método Privado
     #Desfaz o último item da expressão.
     #A lista que que criamos anteriormente e
     #guardamos as operações realizadas paralelamente
     #agora será usada para excluir o último item desta lista
     #alterando a expressão inicial
    def __Apaga(
        self : object
        ):
        'Adicionando valor à expressão'

        # Adicionando o valor à expressao
        if(self.lista):
            #remove o último item da lista
            self.lista.pop()
            #converte a lista em string
            #juntando cada item da lista em uma string só
            self.expressao = ''.join(self.lista)

        # Atualizando expressão na caixa
        self.conteudoCaixa.set(self.expressao)

        return None
##================================================================================================================================
    # Método Privado
    def __perguntarPraSair(
        self : object,
        event: 'Event' = None
        ):
        'Exibe uma janela perguntando se deseja fechar a janela'

        # Abrindo janela com o diálogo
        decisao = messagebox.askyesno(
            'Fechar',
            'Deseja realmente fechar?'
        )

        # Verificando decisão
        if decisao == True:
            # Fechando a janela
            self.__fecharJanela()

        else:
            # Faça nada
            pass

        return None

    # Método Privado
    def __resolveExpressao(
        self : object,
        event: 'Event' = None
        ):
        'Avaliando a expressao e exibindo seu resultado'

        # Definindo uma variavel para verificar
        # se houve erro ou nao
        houveErro = True
        

        # Tratando possíveis erros
        try:
            # Ajustando os simbolos de multiplicação e divisão
            expressao = self.conteudoCaixa.get().replace('x','*').replace('÷','/').replace(',','.').replace('log','log10').replace('ln','log').replace('%','/100')
                                                
            # Avaliando a expressão
            resultado = eval(expressao)
            
            # Redefinindo a expressão pelo resultado
            self.expressao = str(resultado)
            self.lista= [self.expressao]
            
            # Exibindo resultado na caixa
            self.conteudoCaixa.set(str(resultado))

            # Informando que houve erro
            houveErro = False

        except SyntaxError as erroInfo:
            # Obtendo conteudo do erro
            conteudoErro = erroInfo.args[0].title()
            
            # Traduzindo o erro
            erroTraduzido = self.__traduzirTexto(conteudoErro)

            # Reportando erro no shell e no arquivoErros
            print(f'\nErroDeSintaxe: {erroTraduzido}\n', file=sys.stderr)
            print(f'\nErroDeSintaxe: {erroTraduzido}\n', file=self.arquivoErros)
            

        except NameError as erroInfo:
            # Obtendo conteudo do erro
            conteudoErro = erroInfo.args[0].title()
            
            # Traduzindo o erro
            erroTraduzido = self.__traduzirTexto(conteudoErro)

            # Reportando erro no shell e no arquivoErros
            print(f'\nErroDeNome: {erroTraduzido}\n', file=sys.stderr)
            print(f'\nErroDeNome: {erroTraduzido}\n', file=self.arquivoErros)

##======================================================================================================================
        except ZeroDivisionError as erroInfo:
            # Reportando erro no shell e no arquivoErros
            print(f'\n Não é possível realizar divisão por zero\n', file=sys.stderr)        
            print(f'\n Não é possível realizar divisão por zero!\n', file=self.arquivoErros)  

        except ValueError as erroInfo:
            # Reportando erro no shell e no arquivoErros
            print(f'\n Resultado indefinido.\n', file=sys.stderr)        
            print(f'\n Resultado indefinido!\n', file=self.arquivoErros)

        except TypeError as erroInfo:
            # Reportando erro no shell e no arquivoErros
            print(f'\n Erro de tipo.\n', file=sys.stderr)        
            print(f'\n Erro de tipo!\n', file=self.arquivoErros) 
##======================================================================================================================            

        except:
            # Reportando erro no shell e no arquivoErros
            print(f'\nDeuRuim: Problema desconhecido\n', file=sys.stderr)        
            print(f'\nDeuRuim: Problema desconhecido\n', file=self.arquivoErros)        

        finally:
            # Verificando se houve erro
            if houveErro:
                # Informando erro na caixa
                self.conteudoCaixa.set(' error')

                # Limpando a expressao na memória
                self.expressao = ''
                self.lista= []

            else:
                
##================================================================================================================
                #printando no aquivoHistorico a expressao
                #e seu resultado exibido após pressionar o botao '='
                print(expressao, file= arquivoHistorico)
                print('=', file= arquivoHistorico)
                print(resultado,file=arquivoHistorico)
##================================================================================================================
                # Faça nada
                pass                    

        return None

    def __traduzirTexto(self, texto):
        '''Traduz o erro de ingles para portugues
           pelo Google Tradutor'''

        # Obtendo acesso à instância externa 'tradutor'
        global tradutor

        # Tentando traduzir texto de erro pela Web
        try:
            # Traduzindo texto
            textoTraduzido = tradutor.translate(texto,dest='pt')

            # Obtendo texto da tradução
            textoTraduzido = textoTraduzido.text

        # Tradutor nao definido pois modulo 'googletrans'
        # não está instalado
        except NameError:
            # Reportando erro de conexão no shell
            #print("\nModuloNãoInstalado: 'googletrans'", file=sys.stderr)
            print("\nModuloNãoInstalado: 'googletrans'", file=self.arquivoErros)

        # Sem conexão
        except:            
            # Reportando erro de conexão no shell
            print(f'\nSemConexão: Não foi possível traduzir o erro', file=sys.stderr)
            print(f'\nSemConexão: Não foi possível traduzir o erro', file=self.arquivoErros)

        # Clausula de proteção
        finally:
            # Verificando se 'textoTraduzido' não foi definido
            # internamente
            if 'textoTraduzido' not in locals():
                # Definindo a tradução do texto como ele mesmo
                textoTraduzido = texto

            # Nada faça, o 'try' funcionou
            else: pass
            

        return textoTraduzido

    def __definirAcoesTeclado(
        self: object
        ):
        'Definindo as ações de teclado'

        # Habilitando ENTER para resolver a equação
        self.janela.bind('<Return>', self._JanelaBase__resolveExpressao)

        # Habilitando ESC para fechar a janela
        self.janela.bind('<Escape>', self._JanelaBase__perguntarPraSair)

        # Habilitando BACKSPACE para limpar caixa de texto
        self.janela.bind('<BackSpace>', self._JanelaBase__limpar)

        return None

    # Método Público
    def rodarJanela(
        self       : object,
#=====================================================================================================================
        arquivoErros          : 'file'      = sys.stderr, # sys.stderr: Texto no Shell Vermelho
                                                   # sys.stdout: Texto no Shell Azul
                                                   # yourFile  : Texto no Arquivo '.txt' dado

        arquivoHistorico      : 'file'      = sys.stderr # sys.stderr: Texto no Shell Vermelho
                                                   # sys.stdout: Texto no Shell Azul
                                                   # yourFile  : Texto no Arquivo '.txt' dado
        ):
    
        'Executando janela'        

        # Rodando aplicação
        self.janela.mainloop()


        # Fechando os arquivos '.txt'
        if 'idlelib' not in str(type(arquivoErros)):
            arquivoErros.close()

        if 'idlelib' not in str(type(arquivoHistorico)):
            arquivoHistorico.close()

        return None

      # Método Privado
      #Será usado no botão 'inverso' do frame cientifica
    def __inverte(
        self : object
        ):
        'Adicionando valor à expressão'

        # Adicionando o valor à expressao
        self.lista = ['(','1','/']+self.lista+[')']
        self.expressao= ''.join(self.lista)
        
        # Atualizando expressão na caixa
        self.conteudoCaixa.set(self.expressao)

        return None

    # Método Privado
    #Será usado no botão 'elevado' do frame cientifica
    def __elevado(
        self : object
        ):
        'Adicionando valor à expressão'

        # Adicionando o valor à expressao
        self.lista = self.lista+ ['**', '(']
        self.expressao= ''.join(self.lista)

        # Atualizando expressão na caixa
        self.conteudoCaixa.set(self.expressao)

        return None

    # Método Privado
    #Será usado no botão 'fatorial' do frame cientifica
    def __fatora(
        self : object
        ):
        'Adicionando valor à expressão'

        # Adicionando o valor à expressao
        self.lista = ['factorial(']+self.lista+[')']
        self.expressao = ''.join(self.lista)
        # Atualizando expressão na caixa
        self.conteudoCaixa.set(self.expressao)

        return None
    
##===================================================================================================================


class ToolTip():
    'Classe para texto explicativo'

    def __init__(self, widget):
        'Construtor'

        # Tornando, o respectivo widget, um atributo
        self.widget = widget

        # Predefinindo que caixa de dica nao existe        
        self.tipwindow = None

        # Numero de identificação da caixa de dica
        self.id = None

        # Predefinindo as posições da caixa de dica
        self.x = self.y = 0

        return None

    def exibirDica(self, text):
        "Display text in tooltip window"

        # Definindo texto como atributo
        self.text = text

        # Verificando se caixa de dica não existe
        # ou se a mensagem é vazia
        if self.tipwindow or not self.text:
            return None
        
        # Criando e obtendo a posicao da caixa
        # de dica
        x, y, cx, cy = self.widget.bbox("insert")

        # Ajustando posicao
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27

        # Habilitando a caixa de dica
        self.tipwindow = tw = Toplevel(self.widget)

        # Redimensionando
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        # Preenchendo com a mensagem
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))

        # Posicionando texto na caixa de dica
        label.pack(ipadx=1)

        return None

    def esconderDica(self):
        'Hide the tooltip'

        # Verificando se caixa de dica está ativa
        if self.tipwindow:
            # Redefinindo e fechando
            self.tipwindow, _ = None, self.tipwindow.destroy()

        return None
    
class FrameNormal(JanelaBase):
    '''Classe referente às configuracoes de
       botoes do modo normal'''

    def __init__(
        self            : object,
        base            : 'Tk_object',
        corFundoBotao   : str         = 'navy blue',
        corTextoBotao   : str         = 'white',
        alturaBotao     : [int,float] = 2,
        comprimentoBotao: [int,float] = 8,
##========================================================================================================
        fonte           : str         = ("mathjax_ams","10","bold"),
        espessuraBorda  : int         = 7,
        relevo          : str         = 'groove'
##========================================================================================================        
        ):
        'Construindo a estrutura do frame'
        
        # Criando o atributo base
        self.base = base

        # Associando frame à base dada
        self.frame = Frame(
            base.janela,
            background='light blue',
            )

        # Configurando botoes
        self.__configurarBotao(
            corTextoBotao,  
            corFundoBotao,    
            alturaBotao,     
            comprimentoBotao,
            fonte,
            relevo,
            espessuraBorda,
        )

        # Criando os widgets
        self.__criarWidgets()

        # Habilitando acoes do teclado/mouse
        self.__definirAcoesBotoes()
        
        return None


    # Método Privado
    def __configurarBotao(
        self           : object,
        corTexto       : str,
        corFundo       : str,
        altura         : [int,float],
        comprimento    : [int,float],
        fonte          : str,
        relevo         : [int,float],
        espessuraBorda : [int,float]
        ):
        'Configurando alguns parâmetros dos botoes'

        # Criando atributos privados com os parametros
        self.corBotaoTexto    = corTexto
        self.corBotaoBg       = corFundo
        self.alturaBotao      = altura
        self.comprimentoBotao = comprimento
        self.fonte            = fonte
        self.relevo           = relevo
        self.espessuraBorda   = espessuraBorda

        return None

    def limparDica(
        self : object,
        event: 'Event_object'
        ):
        'Limpar caixa de dica'

        # Escondendo dica
        self.caixaDica.esconderDica()

        return None

    def mostrarDica(
        self    : object,
        elemento: [int,str],
        widget  : 'Widget_object'
        ):
        'Exibindo respectiva dica'

        # Estrutura com as dicas
        respectivaDica = {
            1  : 'Número 1',
            2  : 'Número 2',
            3  : 'Número 3',
            4  : 'Número 4',
            5  : 'Número 5',
            6  : 'Número 6',
            7  : 'Número 7',
            8  : 'Número 8',
            9  : 'Número 9',
            0  : 'Número 0',
            'C': 'Limpar',
            '/': 'Divisão',
            '*': 'Multiplicação',
            '-': 'Subtração',
            '+': 'Soma',
            '.': 'Decimal',
            '=': 'Resolver equação',
##=====================================================================================================
            '%': 'porcentagem',
            '⌫': 'Apaga o útimo item da expressão'
##=====================================================================================================            
        }[elemento]


        # Criando uma caixa de dicas para o
        # respectivo widget
        self.caixaDica = ToolTip(widget)

        # Exibindo dica
        self.caixaDica.exibirDica(respectivaDica)

        return None

    def __definirAcoesBotoes(
        self: object
        ):
        'Definindo as ações de teclado/mouse'

        # Habilitando a dica referente ao botao        
        self.botao1.bind       ("<Enter>",lambda event: self.mostrarDica(1,self.botao1))
        self.botao2.bind       ("<Enter>",lambda event: self.mostrarDica(2,self.botao2))
        self.botao3.bind       ("<Enter>",lambda event: self.mostrarDica(3,self.botao3))
        self.botao4.bind       ("<Enter>",lambda event: self.mostrarDica(4,self.botao4))
        self.botao5.bind       ("<Enter>",lambda event: self.mostrarDica(5,self.botao5))
        self.botao6.bind       ("<Enter>",lambda event: self.mostrarDica(6,self.botao6))
        self.botao7.bind       ("<Enter>",lambda event: self.mostrarDica(7,self.botao7))
        self.botao8.bind       ("<Enter>",lambda event: self.mostrarDica(8,self.botao8))
        self.botao9.bind       ("<Enter>",lambda event: self.mostrarDica(9,self.botao9))
        self.botao0.bind       ("<Enter>",lambda event: self.mostrarDica(0,self.botao0))
        self.botaoPlus.bind    ("<Enter>",lambda event: self.mostrarDica('+',self.botaoPlus))
        self.botaoMinus.bind   ("<Enter>",lambda event: self.mostrarDica('-',self.botaoMinus))
        self.botaoMultiply.bind("<Enter>",lambda event: self.mostrarDica('*',self.botaoMultiply))
        self.botaoDivide.bind  ("<Enter>",lambda event: self.mostrarDica('/',self.botaoDivide))
        self.botaoClear.bind   ("<Enter>",lambda event: self.mostrarDica('C',self.botaoClear))
        self.botaoDecimal.bind ("<Enter>",lambda event: self.mostrarDica('.',self.botaoDecimal))
        self.botaoEqual.bind   ("<Enter>",lambda event: self.mostrarDica('=',self.botaoEqual))
##============================================================================================================================
        self.botaoPorcentagem.bind("<Enter>",lambda event: self.mostrarDica('%',self.botaoPorcentagem))
        self.botaoApagar.bind     ("<Enter>",lambda event: self.mostrarDica('⌫',self.botaoApagar))
        
##============================================================================================================================
        # Desabilitando dz
        self.botao1.bind       ("<Leave>",self.limparDica)
        self.botao2.bind       ("<Leave>",self.limparDica)
        self.botao3.bind       ("<Leave>",self.limparDica)
        self.botao4.bind       ("<Leave>",self.limparDica)
        self.botao5.bind       ("<Leave>",self.limparDica)
        self.botao6.bind       ("<Leave>",self.limparDica)
        self.botao7.bind       ("<Leave>",self.limparDica)
        self.botao8.bind       ("<Leave>",self.limparDica)
        self.botao9.bind       ("<Leave>",self.limparDica)
        self.botao0.bind       ("<Leave>",self.limparDica)
        self.botaoPlus.bind    ("<Leave>",self.limparDica)
        self.botaoMinus.bind   ("<Leave>",self.limparDica)
        self.botaoMultiply.bind("<Leave>",self.limparDica)
        self.botaoDivide.bind  ("<Leave>",self.limparDica)
        self.botaoClear.bind   ("<Leave>",self.limparDica)
        self.botaoDecimal.bind ("<Leave>",self.limparDica)
        self.botaoEqual.bind   ("<Leave>",self.limparDica)
##================================================================================================================================
        self.botaoPorcentagem.bind  ("<Leave>",self.limparDica)
        self.botaoApagar.bind       ("<Leave>",self.limparDica)
##================================================================================================================================
        return None


    def __criarWidgets(self):
        'Criando os widgets deste frame'
        
        # Criando um botão funcional com o texto '1'
        self.botao1 = Button(
            self.frame,                    # Onde será colocado o botão
            text='１',                     # Texto a ser exibido no botão
            fg=self.corBotaoTexto,         # Cor do texto
            bg=self.corBotaoBg,            # Cor de fundo do botão
            height=self.alturaBotao,       # Altura do botão
            width=self.comprimentoBotao,   # Comprimento do botão
##=====================================================================================================
            relief=self.relevo,            # Estilo de relevo
            font=self.fonte,               # Fonte do texto
            bd=self.espessuraBorda,        # Espessura da boda
            command=lambda:JanelaBase._JanelaBase__adicionaValor(
                self.base,1
                )                          # Função a ser executada ao clicar no botão
##======================================================================================================          
        )        

        # Criando um botão funcional com o texto '2'
        self.botao2 = Button(
            self.frame,
            text='２',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,2)
            
            
        )

        # Criando um botão funcional com o texto '3'
        self.botao3 = Button(
            self.frame,
            text='３',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,3)
        
        )

        # Criando um botão funcional com o texto '4'
        self.botao4 = Button(
            self.frame,
            text='4',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,4)    
        )

        # Criando um botão funcional com o texto '5'
        self.botao5 = Button(
            self.frame,
            text='５',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,5)
        )

        # Criando um botão funcional com o texto '6'
        self.botao6 = Button(
            self.frame,
            text='６',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,6)
        )

        # Criando um botão funcional com o texto '7'
        self.botao7 = Button(
            self.frame,
            text='7',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,7)
        )

        # Criando um botão funcional com o texto '8'
        self.botao8 = Button(
            self.frame,
            text='８',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,8)
        )

        # Criando um botão funcional com o texto '9'
        self.botao9 = Button(
            self.frame,
            text='９',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,9)
        )

        # Criando um botão funcional com o texto '0'
        self.botao0 = Button(
            self.frame,
            text='0',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,0)
        )

        # Criando um botão funcional com o texto '+'
        self.botaoPlus = Button(
            self.frame,
            text='✚',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'+')
        )

        # Criando um botão funcional com o texto '-'
        self.botaoMinus = Button(
            self.frame,
            text='➖',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'-')
        )

        # Criando um botão funcional com o texto '*'
        self.botaoMultiply = Button(
            self.frame,
            text='X',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'x')
        )

        # Criando um botão funcional com o texto '/'
        self.botaoDivide = Button(
            self.frame,
            text='➗',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'÷')
        )

        # Criando um botão funcional com o texto '.'
        self.botaoDecimal= Button(
            self.frame,
            text='•',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'.')
            
        )

        # Criando um botão funcional com o texto '='
        self.botaoEqual = Button(
            self.frame,
            text='＝',
            font=self.fonte,
            fg='white',
            bd=self.espessuraBorda,
            bg='red',
            height=self.alturaBotao,
            width=19,
            relief= self.relevo,
            command=lambda:JanelaBase._JanelaBase__resolveExpressao(self.base)   
        )

        # Criando um botão funcional com o texto 'C'
        self.botaoClear = Button(
            self.frame,
            text='CLEAR',
            font=self.fonte,
            bd=self.espessuraBorda,
            fg='white',
            bg='orange',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief= self.relevo,
            command=lambda:JanelaBase._JanelaBase__limpar(self.base)  
        )

        ##===========================================================================================================================
        # Criando um botão funcional com o texto '%'

        self.botaoPorcentagem = Button(
            self.frame,
            text='%',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'%')
            
        )

        # Criando um botão funcional com o texto 'del'

        self.botaoApagar = Button(
            self.frame,
            text='⌫',
            font=self.fonte,
            fg="white",
            bg="orange",
            bd=self.espessuraBorda,
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            command=lambda:JanelaBase._JanelaBase__Apaga(self.base)
            
        )
        
##===========================================================================================================================

        # Posicionando os botões considerando um grid
        # com 6 linhas e 4 colunas
        self.botao1           .grid(row=2, column=0) 
        self.botao2           .grid(row=2, column=1) 
        self.botao3           .grid(row=2, column=2) 
        self.botao4           .grid(row=3, column=0) 
        self.botao5           .grid(row=3, column=1)
        self.botao6           .grid(row=3, column=2)
        self.botao7           .grid(row=4, column=0)
        self.botao8           .grid(row=4, column=1)
        self.botao9           .grid(row=4, column=2)
        self.botao0           .grid(row=5, column=0)
        self.botaoPlus        .grid(row=2, column=3)
        self.botaoMinus       .grid(row=3, column=3)
        self.botaoMultiply    .grid(row=4, column=3)
        self.botaoDivide      .grid(row=5, column=3)
        self.botaoEqual       .grid(row=6, column=0, rowspan=2, columnspan=6)
        self.botaoClear       .grid(row=5, column=1)
        self.botaoDecimal     .grid(row=6, column=0)
##=====================================================================================================================================
        self.botaoPorcentagem .grid(row=6, column=3)
        self.botaoApagar      .grid(row=5, column=2)
        
##=====================================================================================================================================
        return None

class FrameCientifica(FrameNormal):
    '''Classe referente às configuracoes de
       botoes do modo cientifico'''

    def __init__(self, base):
        'Construtor'

        # Agregando os metodos e atributos
        # da classe "FrameNormal"
        FrameNormal.__init__(self, base)

        # Cirando e posicionando os botoes
        self.__criarWidgets()

        # Habilitando acoes do teclado/mouse
        self.__definirAcoesBotoesCientifica()
        # Habilitando acoes do teclado/mouse
        self._FrameNormal__definirAcoesBotoes()
        
##=============================================================================================================
    #redefinindo o metodo de dicas para o frame científica
    def limparDicaCien(
        self : object,
        event: 'Event_object'
        ):
        'Limpar caixa de dica'

        # Escondendo dica
        self.caixaDica.esconderDica()

        return None

    def mostrarDicaCien(
        self    : object,
        elemento: [int,str],
        widget  : 'Widget_object'
        ):
        'Exibindo respectiva dica'

        # Estrutura com as dicas
        respectivaDica = {
            'cos': 'Cosseno- Não esquecer de fechar o parenteses-(argumento em radiano)',
            'sen': 'Seno- Não esquecer de fechar o parenteses-(argumento em radiano)',
            'tan': 'Tangente- Não esquecer de fechar o parenteses-(aqgumento em radiano)',
            'log': 'Logaritmo na base 10- Não esquecer de fechar o parenteses',
            'ln' : 'Logaritmo natural- Não esquecer de fechar o parenteses',
            '√'  : 'Raiz quadrada',
            'x²' : 'Quadrado',
            'xʸ' : 'Eleva a "y"',
            '1/x': 'Inverso',
            'n!' : 'Fatorial',
            'exp': 'Exponecial',
            '|x|': 'Módulo',
            '10ⁿ': 'potencia na base 10',
            '2ⁿ' : 'potencia na base 2',
            'ⁿ√' : 'Raíz n-ésima. Não esquecer de fechar o parêntese',
            '⌫' : 'Apaga o último item da expressão'
        }[elemento]


        # Criando uma caixa de dicas para o
        # respectivo widget
        self.caixaDica = ToolTip(widget)

        # Exibindo dica
        self.caixaDica.exibirDica(respectivaDica)

        return None

    def __definirAcoesBotoesCientifica(
        self: object
        ):
        'Definindo as ações de teclado/mouse'

        # Habilitando a dica referente ao botao 
        self.botaoCosseno.bind      ("<Enter>",lambda event: self.mostrarDicaCien('cos',self.botaoCosseno))
        self.botaoSeno.bind         ("<Enter>",lambda event: self.mostrarDicaCien('sen',self.botaoSeno))
        self.botaoTangente.bind     ("<Enter>",lambda event: self.mostrarDicaCien('tan',self.botaoTangente))
        self.botaoLogaritmo.bind    ("<Enter>",lambda event: self.mostrarDicaCien('log',self.botaoLogaritmo))
        self.botaoLogNatural.bind   ("<Enter>",lambda event: self.mostrarDicaCien('ln',self.botaoLogNatural))
        self.botaoRaiz.bind         ("<Enter>",lambda event: self.mostrarDicaCien('√',self.botaoRaiz))
        self.botaoQuadrado.bind     ("<Enter>",lambda event: self.mostrarDicaCien('x²',self.botaoQuadrado))
        self.botaoElevado.bind      ("<Enter>",lambda event: self.mostrarDicaCien('xʸ',self.botaoElevado))
        self.botaoInverte.bind      ("<Enter>",lambda event: self.mostrarDicaCien('1/x',self.botaoInverte))
        self.botaoFatorial.bind     ("<Enter>",lambda event: self.mostrarDicaCien('n!',self.botaoFatorial))
        self.botaoExponencial.bind  ("<Enter>",lambda event: self.mostrarDicaCien('exp',self.botaoExponencial))
        self.botaoModulo.bind       ("<Enter>",lambda event: self.mostrarDicaCien('|x|',self.botaoModulo))
        self.botaoPotencia_10.bind  ("<Enter>",lambda event: self.mostrarDicaCien('10ⁿ',self.botaoPotencia_10))
        self.botaoPotencia_2.bind   ("<Enter>",lambda event: self.mostrarDicaCien('2ⁿ',self.botaoPotencia_2))
        self.botaoRaiz_n.bind       ("<Enter>",lambda event: self.mostrarDicaCien('ⁿ√',self.botaoRaiz_n))
        self.botaoApagar.bind       ("<Enter>",lambda event: self.mostrarDicaCien('⌫',self.botaoApagar))

       # Desabilitando dz
        self.botaoCosseno.bind      ("<Leave>",self.limparDicaCien)
        self.botaoSeno.bind         ("<Leave>",self.limparDicaCien)
        self.botaoTangente.bind     ("<Leave>",self.limparDicaCien)
        self.botaoLogaritmo.bind    ("<Leave>",self.limparDicaCien)
        self.botaoLogNatural.bind   ("<Leave>",self.limparDicaCien)
        self.botaoRaiz.bind         ("<Leave>",self.limparDicaCien)
        self.botaoQuadrado.bind     ("<Leave>",self.limparDicaCien)
        self.botaoElevado.bind      ("<Leave>",self.limparDicaCien)
        self.botaoInverte.bind      ("<Leave>",self.limparDicaCien)
        self.botaoFatorial.bind     ("<Leave>",self.limparDicaCien)
        self.botaoExponencial.bind  ("<Leave>",self.limparDicaCien)
        self.botaoModulo.bind       ("<Leave>",self.limparDicaCien)
        self.botaoPotencia_10.bind  ("<Leave>",self.limparDicaCien)
        self.botaoPotencia_2.bind   ("<Leave>",self.limparDicaCien)
        self.botaoRaiz_n.bind       ("<Leave>",self.limparDicaCien)
        self.botaoApagar.bind            ("<Leave>",self.limparDicaCien)
        return None
        #=========================================================================================================================================================



    def __criarWidgets(self):
        'Criando widgets deste frame'
        
        # Criando um botão funcional com o texto '1'
        self.botao1 = Button(
            self.frame,                  # Onde será colocado o botão
            text='1',                    # Texto a ser exibido no botão
            fg=self.corBotaoTexto,       # Cor do texto
            bg=self.corBotaoBg,          # Cor de fundo do botão
            height=self.alturaBotao,     # Altura do botão
            width=self.comprimentoBotao, # Comprimento do botão
            relief= self.relevo,         # Estilo de relevo 
            bd= self.espessuraBorda,     # Espessura da borda do botão
            font= self.fonte,            # Fonte do texto inserido no botão
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,1) # Função a ser executada ao clicar no botão
        )

        # Criando um botão funcional com o texto '2'
        self.botao2 = Button(
            self.frame,
            text='2',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            bd=self.espessuraBorda,
            relief=self.relevo,
            width=self.comprimentoBotao,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,2)
        )

        # Criando um botão funcional com o texto '3'
        self.botao3 = Button(
            self.frame,
            text='3',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            bd=self.espessuraBorda,
            relief=self.relevo,
            width=self.comprimentoBotao,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,3)
        )

        # Criando um botão funcional com o texto '4'
        self.botao4 = Button(
            self.frame,
            text='4',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            bd=self.espessuraBorda,
            relief=self.relevo,
            width=self.comprimentoBotao,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,4)
        )

        # Criando um botão funcional com o texto '5'
        self.botao5 = Button(
            self.frame,
            text='5',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            bd=self.espessuraBorda,
            relief=self.relevo,
            width=self.comprimentoBotao,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,5)
        )

        # Criando um botão funcional com o texto '6'
        self.botao6 = Button(
            self.frame,
            text='6',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            bd=self.espessuraBorda,
            relief=self.relevo,
            width=self.comprimentoBotao,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,6)
        )

        # Criando um botão funcional com o texto '7'
        self.botao7 = Button(
            self.frame,
            text='7',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            bd=self.espessuraBorda,
            relief=self.relevo,
            width=self.comprimentoBotao,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,7)
        )

        # Criando um botão funcional com o texto '8'
        self.botao8 = Button(
            self.frame,
            text='8',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            bd=self.espessuraBorda,
            relief=self.relevo,
            width=self.comprimentoBotao,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,8)
        )

        # Criando um botão funcional com o texto '9'
        self.botao9 = Button(
            self.frame,
            text='9',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            bd=self.espessuraBorda,
            relief=self.relevo,
            width=self.comprimentoBotao,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,9)
        )

        # Criando um botão funcional com o texto '0'
        self.botao0 = Button(
            self.frame,
            text='O',
            font=self.fonte,
            fg=self.corBotaoTexto,
            bg=self.corBotaoBg,
            height=self.alturaBotao,
            bd=self.espessuraBorda,
            relief=self.relevo,
            width=self.comprimentoBotao,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,0)
        )

        # Criando um botão funcional com o texto '+'
        self.botaoPlus = Button(
            self.frame,
            text='➕',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'+')
        )

        # Criando um botão funcional com o texto '-'
        self.botaoMinus = Button(
            self.frame,
            text='➖',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'-')
        )

        # Criando um botão funcional com o texto '*'
        self.botaoMultiply = Button(
            self.frame,
            text='X',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'x')
        )

        # Criando um botão funcional com o texto '/'
        self.botaoDivide = Button(
            self.frame,
            text='➗',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'÷')
        )

        # Criando um botão funcional com o texto '.'
        self.botaoDecimal= Button(
            self.frame,
            text=',',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'.')
        )

        # Criando um botão funcional com o texto '='
        self.botaoEqual = Button(
            self.frame,
            text='=',
            font=self.fonte,
            fg='white',
            bg='red',
            bd=self.espessuraBorda,
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief= self.relevo,
            command=lambda:JanelaBase._JanelaBase__resolveExpressao(self.base)
        )

        # Criando um botão funcional com o texto 'C'
        self.botaoClear = Button(
            self.frame,
            text='CLEAR',
            font=self.fonte,
            fg='white',
            bg='orange',
            bd=self.espessuraBorda,
            relief=self.relevo,
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            command=lambda:JanelaBase._JanelaBase__limpar(self.base)
        )

##===================================================================================================================================

        # Criando um botão funcional com o texto 'cosseno'
        self.botaoCosseno = Button(
            self.frame,
            text='cos',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'cos(')
        )

        # Criando um botão funcional com o texto 'Tangente'
        self.botaoTangente = Button(
            self.frame,
            text='tan',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'tan(')
        )


         # Criando um botão funcional com o texto 'Seno'
        self.botaoSeno = Button(
            self.frame,
            text='sin',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'sin(')
        )

         # Criando um botão funcional com o texto '('

        self.botaoParentese1 = Button(
            self.frame,
            text='(',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'(')
        )

        # Criando um botão funcional com o texto ')'

        self.botaoParentese2 = Button(
            self.frame,
            text=')',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,')')
        )

        # Criando um botão funcional com o texto '1/x'

        self.botaoInverte = Button(
            self.frame,
            text="1/x",
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda: JanelaBase._JanelaBase__inverte(self.base)
        )

        # Criando um botão funcional  'raiz'

        self.botaoRaiz = Button(
            self.frame,
            text='√',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'sqrt(')
        )

        # Criando um botão funcional 'quadrado'

        self.botaoQuadrado = Button(
            self.frame,
            text='x²',
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'**2')
        )

        
        # Criando um botão funcional com o texto 'elevado'

        self.botaoElevado = Button(
            self.frame,
            text="xʸ",
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__elevado(self.base)
        )

        # Criando um botão funcional 'fatorial'

        self.botaoFatorial = Button(
            self.frame,
            text="n!",
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__fatora(self.base)
        )

         # Criando um botão funcional 'exponencial'

        self.botaoExponencial = Button(
            self.frame,
            text="exp",
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'e**')
        )

        # Criando um botão funcional 'log'

        self.botaoLogaritmo = Button(
            self.frame,
            text="log",
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'log(')
        )

         # Criando um botão funcional 'ln'

        self.botaoLogNatural = Button(
            self.frame,
            text="ln",
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'ln(')
        )

        # Criando um botão funcional 'potencia de 10'

        self.botaoPotencia_10 = Button(
            self.frame,
            text="10ⁿ",
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'10**')
        )

        # Criando um botão funcional 'potencia de 2 '

        self.botaoPotencia_2 = Button(
            self.frame,
            text="2ⁿ",
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'2**')
        )


        # Criando um botão funcional 'raiz de n'

        self.botaoRaiz_n = Button(
            self.frame,
            text="ⁿ√",
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'**(1/')
        )

         # Criando um botão funcional 'modulo'

        self.botaoModulo = Button(
            self.frame,
            text="|x|",
            font=self.fonte,
            fg='navy blue',
            bg='light blue',
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            bd=self.espessuraBorda,
            command=lambda:JanelaBase._JanelaBase__adicionaValor(self.base,'abs(')
        )

        # Criando um botão funcional 'apagar'

        self.botaoApagar = Button(
            self.frame,
            text='⌫',
            font=self.fonte,
            fg="white",
            bg="orange",
            bd=self.espessuraBorda,
            height=self.alturaBotao,
            width=self.comprimentoBotao,
            relief=self.relevo,
            command=lambda:JanelaBase._JanelaBase__Apaga(self.base)
            
        )

##===================================================================================================================================

        # Posicionando os botões considerando um grid
        # com 8 linhas e 4 colunas
        self.botao1            .grid(row=3, column=1)
        self.botao2            .grid(row=3, column=2)
        self.botao3            .grid(row=3, column=3)
        self.botao4            .grid(row=4, column=1)
        self.botao5            .grid(row=4, column=2)
        self.botao6            .grid(row=4, column=3)
        self.botao7            .grid(row=5, column=1)
        self.botao8            .grid(row=5, column=2)
        self.botao9            .grid(row=5, column=3)
        self.botao0            .grid(row=6, column=1)
        self.botaoPlus         .grid(row=3, column=0)
        self.botaoMinus        .grid(row=4, column=0)
        self.botaoMultiply     .grid(row=5, column=0)
        self.botaoDivide       .grid(row=6, column=0)
        self.botaoEqual        .grid(row=2, column=4)
        self.botaoClear        .grid(row=6, column=2)
        self.botaoDecimal      .grid(row=2, column=0)
##===================================================================================================================
        self.botaoCosseno      .grid(row=7, column=1)
        self.botaoSeno         .grid(row=7, column=2)
        self.botaoTangente     .grid(row=7, column=3)
        self.botaoParentese1   .grid(row=2, column=1)
        self.botaoParentese2   .grid(row=2, column=2)
        self.botaoRaiz         .grid(row=8, column=2)
        self.botaoInverte      .grid(row=6, column=4)
        self.botaoElevado      .grid(row=3, column=4)
        self.botaoQuadrado     .grid(row=4, column=4)
        self.botaoFatorial     .grid(row=5, column=4)
        self.botaoApagar       .grid(row=6, column=3)
        self.botaoLogaritmo    .grid(row=7, column=4)
        self.botaoLogNatural   .grid(row=8, column=4)
        self.botaoPotencia_10  .grid(row=8, column=0)
        self.botaoExponencial  .grid(row=8, column=1)
        self.botaoRaiz_n       .grid(row=8, column=3)
        self.botaoModulo       .grid(row=2, column=3)
        self.botaoPotencia_2   .grid(row=7, column=0)

        return None

##===================================================================================================================
       



# ======================================================= #
# FIM DA CLASSE BASE
# ======================================================= #

# Função auxiliar
def preparandoTradutor():
    '''Instalando e importando pacote do Google Tradutor
       e instanciando um tradutor'''

    # Verificando se o modulo 'googletrans' já está
    # instalado na máquina
    if 'googletrans' not in sys.modules:
        # Verificando o sistema operacional e instalando
        # uma pacote externo 'googletrans' convenientemente
        if   platform.system() == 'Windows':        
            subprocess.check_call(['py','-3',"-m", "pip", "install", 'googletrans'])

        elif platform.system() == 'Linux':
            subprocess.check_call(['python3',"-m", "pip", "install", 'googletrans'])

        else:
            subprocess.check_call([sys.call_tracing,"-m", "pip", "install", 'googletrans'])

    # Modulo já instalado
    else: pass

    # Importando módulo externo já baixado
    import googletrans # Para traduzir textos

    # Criando uma instancia do Google Tradutor
    tradutor = googletrans.Translator()

    return tradutor

# Como executar a janela
if __name__ == "__main__":
##======================================================================================================
    #Abrindo os arquivos 'txt'
    arquivoErros = open('log.txt','w')
    arquivoHistorico= open('hist.txt','w')
##======================================================================================================
    # Informando início do programa
    print('\nPrograma iniciado\n')

    # Importando módulos internos
    import subprocess  # Para instalar pacotes externos
    import platform    # Para descobrir o sistema operacional

    # Preparando Google Tradutor
    print('\nBuscando acesso ao Google Tradutor',end='...')
    try:
        #tradutor = preparandoTradutor()
        pass

    # Sem conexão
    except:
        print(' NEGADO')

    # Deu certo!
    else:
        print(' OK')
#========================================================================================================
    # Executando janela
    JanelaBase(arquivoErros=arquivoErros, arquivoHistorico=arquivoHistorico).rodarJanela(arquivoErros=arquivoErros, arquivoHistorico=arquivoHistorico)
    
#========================================================================================================
   

    # Informando fim do programa
    print('\n\nPrograma encerrado\n')
