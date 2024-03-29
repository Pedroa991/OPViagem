from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror, showinfo
import webbrowser
import os
import OPViagem


version = OPViagem.version 

def main():
    class Window(Frame):

        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master
            master.minsize(width=250, height=150)
            self.pack_propagate(0)
            self.init_window()
            self.PathOP = False
            self.PathBD = False


        def init_window(self):
            self.master.title('OPViagem')
            self.pack(fill=BOTH, expand=1)

            # Botões
            convert = Button(self, text='Executar', command=self.Executar, width= 12)
            OP = Button(self, text='Log de viagens', command=self.PathOP, width= 12)
            bd = Button(self, text='BD Cliente', command=self.PathBD, width= 12)


            # Campo de entrada
            OP.place(relx=0.75, rely=0.35, anchor=CENTER)
            bd.place(relx=0.25, rely=0.35, anchor=CENTER)
            
            
            # Botão de conversão
            convert.place(relx=0.50, rely=0.80, anchor=CENTER)

        def Executar(self):
            global PathBD
            PathBD = self.PathBD
            global PathOP
            PathOP = self.PathOP
            
            
            if not PathOP:
                showerror('Erro: Log de viagens não encontrado!',
                            'Selecione o arquivo')
                
            if not PathBD:
                showerror('Erro: history_output.csv na pasta do cliente não encontrado!',
                            'Selecione uma pasta de cliente que tenha o arquivo')
                              
            
            if PathBD or PathOP:
                checkSucesso = OPViagem.main(PathBD,PathOP)

                if checkSucesso:
                    info = showinfo(
                        'Sucesso!','Modo de operação gerado!')

                else:
                    info = showinfo(
                        'Erro!','Houve um erro! \nVerifique os arquivos e tente novamente!')
            
            else:
                info = showinfo(
                        'Erro!','Houve um erro! \nVerifique os arquivos e tente novamente!')

        def PathBD(self):
            PathBD = askdirectory(parent=root,
                                   title='Selecione a pasta de BD do cliente')
            if PathBD:
                PathBD = PathBD + '/history_output.csv'
                self.PathBD = PathBD
                print('Arquivo do Históricos do cliente: ' + str(PathBD) + '\n')
				
        def PathOP(self):
            PathOP = askopenfilename(parent=root,
                                   title='Selecione o arquivo de log de viagens', filetypes = [("Excel files","*.xlsx")])
            if PathOP:
                self.PathOP = PathOP
                print('Arquivo de log de eventos: ' + str(PathOP) + '\n')


    root = Tk()
    def callback(event):
        webbrowser.open_new('https://www.linkedin.com/in/pedrobvenancio/')

    #logo sotreq
    scriptpath = os.path.dirname(os.path.realpath(__file__))
    TxSobre = r'{} - Julho 2023 - Sobre / Ajuda'.format(version)
    lbl = Label(root, text=TxSobre, fg="blue", cursor="hand2")
    lbl.pack(side='bottom')
    lbl.bind("<Button-1>", callback)

    root.geometry('250x150')
    app = Window(root)
    root.mainloop()

if __name__ == '__main__':
    main()
