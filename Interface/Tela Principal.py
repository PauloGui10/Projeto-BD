from tkinter import *
from CRUD import *

class novo:	
	def init(self, janela):
		self.jan = janela
		self.caixa=Frame(janela)
		self.caixa.grid()
		self.buttonCreate = Button( text="Create", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.buttonCreate.place(x=350, y=20)
		self.buttonRead = Button(root, text="Read", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janRead)#, command = TelaRead
		self.buttonRead.place(x=350, y=100)
		self.buttonUpdate = Button(root, text="Update", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janUpdate)#, command = TelaUpdate
		self.buttonUpdate.place(x=350, y=180)
		self.buttonDelete = Button(root, text="Delete", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janDelete)#, command = TelaDelete
		self.buttonDelete.place(x=350, y=260)

	def retornar(self):
		self.bCliente.destroy()
		self.bAtendimento.destroy()
		self.bFuncionario.destroy()
		self.bFornece.destroy()
		self.bCompra.destroy()
		self.bNota.destroy()
		self.bServico.destroy()
		self.bProduto.destroy()
		self.bFornecedor.destroy()
		self.bVoltar.destroy()
		self.init(self.jan)

	def retornarDeCliente(self):
		self.lValores.destroy()
		self.cValores.destroy()
		self.bVoltar.destroy()
		self.bSubmit.destroy()
		self.init(self.jan)

	def janCreate(self):
		self.buttonDelete.destroy()
		self.buttonRead.destroy()
		self.buttonCreate.destroy()
		self.buttonUpdate.destroy()
		#----------------------------------------
		self.bCliente = Button( text="Cliente", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.iCliente)
		self.bCliente.place(x=10, y=10)
		self.bAtendimento = Button( text="Atendimento", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.iAtendimento)
		self.bAtendimento.place(x=10, y=70)
		self.bFuncionario = Button( text="Funcionario", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bFuncionario.place(x=10, y=130)
		self.bProduto = Button( text="Produto", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bProduto.place(x=200, y=10)
		self.bFornecedor = Button( text="Fornecedor", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bFornecedor.place(x=200, y=70)
		self.bFornece = Button( text="Fornece", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bFornece.place(x=200, y=130)
		self.bServico = Button( text="Serviço", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bServico.place(x=400, y=10)
		self.bNota = Button( text="Nota", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bNota.place(x=400, y=70)
		self.bCompra = Button( text="Compra", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bCompra.place(x=400, y=130)

		self.bVoltar = Button( text="Voltar", font ="arial", bg ="red", activebackground = "green", activeforeground= "yellow", width = 10, command = self.retornar)
		self.bVoltar.place(x=200, y=180)
		
	def iCliente(self):
		self.bCliente.destroy()
		self.bAtendimento.destroy()
		self.bFuncionario.destroy()
		self.bFornece.destroy()
		self.bCompra.destroy()
		self.bNota.destroy()
		self.bServico.destroy()
		self.bProduto.destroy()
		self.bFornecedor.destroy()
		self.bVoltar.destroy()

		self.lValores = Label(text="Digite os valores a serem inseridos(entre aspas e separados por vírgula):")
		self.lValores.place(x=200, y=100)
		self.cValores = Entry(text="'valor1', 'valor2', ...", width = 70)
		self.cValores.place(x=190, y=120)
		self.bSubmit = Button( text="Inserir", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.inserirCliente)
		self.bSubmit.place(x=350, y=150)

		self.bVoltar = Button( text="Voltar", font ="arial", bg ="red", activebackground = "green", activeforeground= "yellow", width = 10, command = self.retornarDeCliente)
		self.bVoltar.place(x=200, y=180)

	def iAtendimento(self):
		self.bCliente.destroy()
		self.bAtendimento.destroy()
		self.bFuncionario.destroy()
		self.bFornece.destroy()
		self.bCompra.destroy()
		self.bNota.destroy()
		self.bServico.destroy()
		self.bProduto.destroy()
		self.bFornecedor.destroy()
		self.bVoltar.destroy()

		self.lValores = Label(text="Digite os valores a serem inseridos(entre aspas e separados por vírgula):")
		self.lValores.place(x=200, y=100)
		self.cValores = Entry(text="'valor1', 'valor2', ...", width = 70)
		self.cValores.place(x=190, y=120)
		self.bSubmit = Button( text="Inserir", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.inserirAtendimento)
		self.bSubmit.place(x=350, y=150)

		self.bVoltar = Button( text="Voltar", font ="arial", bg ="red", activebackground = "green", activeforeground= "yellow", width = 10, command = self.retornarDeCliente)
		self.bVoltar.place(x=200, y=180)

	def inserirCliente(self):
		values = []
		values.append(self.cValores.get())
		insert(values, "cliente")
		self.lValores.destroy()
		self.cValores.destroy()
		self.bSubmit.destroy()
		self.janCreate()

	def inserirAtendimento(self):
		values = []
		values.append(self.cValores.get())
		insert(values, "atendimento")
		self.lValores.destroy()
		self.cValores.destroy()
		self.bSubmit.destroy()
		self.janCreate()


	






	def janRead(self):
		self.buttonDelete.destroy()
		self.buttonRead.destroy()
		self.buttonCreate.destroy()
		self.buttonUpdate.destroy()
		#----------------------------------------
		self.bCliente = Button( text="Cliente", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.rCliente)
		self.bCliente.place(x=10, y=10)
		self.bAtendimento = Button( text="Atendimento", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.iAtendimento)
		self.bAtendimento.place(x=10, y=70)
		self.bFuncionario = Button( text="Funcionario", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bFuncionario.place(x=10, y=130)
		self.bProduto = Button( text="Produto", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bProduto.place(x=200, y=10)
		self.bFornecedor = Button( text="Fornecedor", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bFornecedor.place(x=200, y=70)
		self.bFornece = Button( text="Fornece", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bFornece.place(x=200, y=130)
		self.bServico = Button( text="Serviço", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bServico.place(x=400, y=10)
		self.bNota = Button( text="Nota", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bNota.place(x=400, y=70)
		self.bCompra = Button( text="Compra", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bCompra.place(x=400, y=130)

		self.bVoltar = Button( text="Voltar", font ="arial", bg ="red", activebackground = "green", activeforeground= "yellow", width = 10, command = self.retornar)
		self.bVoltar.place(x=200, y=180)

	def rCliente(self):
		self.bCliente.destroy()
		self.bAtendimento.destroy()
		self.bFuncionario.destroy()
		self.bFornece.destroy()
		self.bCompra.destroy()
		self.bNota.destroy()
		self.bServico.destroy()
		self.bProduto.destroy()
		self.bFornecedor.destroy()
		self.bVoltar.destroy()

		self.lCampos = Label(text="Digite os campos a serem exibidos:")
		self.lCampos.place(x=200, y=50)
		self.cCampos = Entry(width = 70)
		self.cCampos.place(x=190, y=70)
		self.lWhere = Label(text="Digite as condições:")
		self.lWhere.place(x=200, y=100)
		self.cWhere = Entry(width = 70)
		self.cWhere.place(x=190, y=120)
		self.bSubmit = Button( text="Selecionar", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.readCliente)
		self.bSubmit.place(x=350, y=150)

		self.bVoltar = Button( text="Voltar", font ="arial", bg ="red", activebackground = "green", activeforeground= "yellow", width = 10, command = self.retornarDeRead)
		self.bVoltar.place(x=200, y=180)

	def readCliente(self):
		campos = self.cCampos.get()
		where = self.cWhere.get()
		self.consulta = select(campos, "cliente", where)
		aux = 210
		for i in self.consulta:
			self.select = Label(text = i)
			self.select.place(x=200, y=aux)
			aux += 30


		'''
		self.lCampos.destroy()
		self.cCampos.destroy()
		self.lWhere.destroy()
		self.cWhere.destroy()
		self.bVoltar.destroy()
		self.bSubmit.destroy()
		self.janRead()
		'''

	def retornarDeRead(self):
		self.lCampos.destroy()
		self.cCampos.destroy()
		self.lWhere.destroy()
		self.cWhere.destroy()
		self.bVoltar.destroy()
		self.bSubmit.destroy()
		
		if self.select:
			for i in self.consulta:
				self.select.destroy()

		self.init(self.jan)

	def janUpdate(self):
		self.buttonDelete.destroy()
		self.buttonRead.destroy()
		self.buttonCreate.destroy()
		self.buttonUpdate.destroy()

		self.bCliente = Button( text="Cliente", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.uCliente)
		self.bCliente.place(x=10, y=10)
		self.bAtendimento = Button( text="Atendimento", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.iAtendimento)
		self.bAtendimento.place(x=10, y=70)
		self.bFuncionario = Button( text="Funcionario", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bFuncionario.place(x=10, y=130)
		self.bProduto = Button( text="Produto", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bProduto.place(x=200, y=10)
		self.bFornecedor = Button( text="Fornecedor", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bFornecedor.place(x=200, y=70)
		self.bFornece = Button( text="Fornece", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bFornece.place(x=200, y=130)
		self.bServico = Button( text="Serviço", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bServico.place(x=400, y=10)
		self.bNota = Button( text="Nota", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bNota.place(x=400, y=70)
		self.bCompra = Button( text="Compra", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bCompra.place(x=400, y=130)

		self.bVoltar = Button( text="Voltar", font ="arial", bg ="red", activebackground = "green", activeforeground= "yellow", width = 10, command = self.retornar)
		self.bVoltar.place(x=200, y=180)

	def uCliente(self):
		self.bCliente.destroy()
		self.bAtendimento.destroy()
		self.bFuncionario.destroy()
		self.bFornece.destroy()
		self.bCompra.destroy()
		self.bNota.destroy()
		self.bServico.destroy()
		self.bProduto.destroy()
		self.bFornecedor.destroy()
		self.bVoltar.destroy()

		self.lValores = Label(text="Digite os novos valores:(NOME, TELEFONE)")
		self.lValores.place(x=200, y=50)
		self.cValores = Entry(width = 70)
		self.cValores.place(x=190, y=70)
		self.lWhere = Label(text="Digite a condição do registro a ser alterado:")
		self.lWhere.place(x=200, y=100)
		self.cWhere = Entry(width = 70)
		self.cWhere.place(x=190, y=120)
		self.bSubmit = Button( text="Update", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.updateCliente)
		self.bSubmit.place(x=350, y=150)

		self.bVoltar = Button( text="Voltar", font ="arial", bg ="red", activebackground = "green", activeforeground= "yellow", width = 10, command = self.retornarDeUpdate)
		self.bVoltar.place(x=200, y=180)

	def updateCliente(self):
		valoresStr = self.cValores.get()
		valoresList = valoresStr.split(",") 
		valores = {"nome": valoresList[0], "telefone": valoresList[1]} #valores novos
		where = self.cWhere.get()
		update(valores, "cliente", where)

	def retornarDeUpdate(self):
		self.lValores.destroy()
		self.cValores.destroy()
		self.lWhere.destroy()
		self.cWhere.destroy()
		self.bVoltar.destroy()
		self.bSubmit.destroy()
		self.init(self.jan)

	def janDelete(self):
		self.buttonDelete.destroy()
		self.buttonRead.destroy()
		self.buttonCreate.destroy()
		self.buttonUpdate.destroy()
		
		self.bCliente = Button( text="Cliente", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.dCliente)
		self.bCliente.place(x=10, y=10)
		self.bAtendimento = Button( text="Atendimento", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.iAtendimento)
		self.bAtendimento.place(x=10, y=70)
		self.bFuncionario = Button( text="Funcionario", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bFuncionario.place(x=10, y=130)
		self.bProduto = Button( text="Produto", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bProduto.place(x=200, y=10)
		self.bFornecedor = Button( text="Fornecedor", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bFornecedor.place(x=200, y=70)
		self.bFornece = Button( text="Fornece", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bFornece.place(x=200, y=130)
		self.bServico = Button( text="Serviço", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bServico.place(x=400, y=10)
		self.bNota = Button( text="Nota", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bNota.place(x=400, y=70)
		self.bCompra = Button( text="Compra", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.janCreate)
		self.bCompra.place(x=400, y=130)

		self.bVoltar = Button( text="Voltar", font ="arial", bg ="red", activebackground = "green", activeforeground= "yellow", width = 10, command = self.retornar)
		self.bVoltar.place(x=200, y=180)

	def dCliente(self):
		self.bCliente.destroy()
		self.bAtendimento.destroy()
		self.bFuncionario.destroy()
		self.bFornece.destroy()
		self.bCompra.destroy()
		self.bNota.destroy()
		self.bServico.destroy()
		self.bProduto.destroy()
		self.bFornecedor.destroy()
		self.bVoltar.destroy()

		self.lDelete = Label(text="Digite a condição do registro que será deletado")
		self.lDelete.place(x=200, y=50)
		self.cDelete = Entry(width = 70)
		self.cDelete.place(x=190, y=70)
		self.bSubmit = Button( text="Delete", font ="arial", bg ="grey", activebackground = "green", activeforeground= "white", width = 10, command = self.deleteCliente)
		self.bSubmit.place(x=350, y=150)

		self.bVoltar = Button( text="Voltar", font ="arial", bg ="red", activebackground = "green", activeforeground= "yellow", width = 10, command = self.retornarDeDelete)
		self.bVoltar.place(x=200, y=180)

	def deleteCliente(self):
		where = self.cDelete.get()
		delete("cliente", where)

	def retornarDeDelete(self):
		self.lDelete.destroy()
		self.cDelete.destroy()
		self.bSubmit.destroy()
		self.bVoltar.destroy()
		self.init(self.jan)

root = Tk()
a = novo()
a.init(root)
root.geometry("800x400")
photo = PhotoImage(file="C:\\Users\\Paulo\\Documents\\Estudos\\Python e MySQL\\CRUD.png")
label = Label(root, image=photo)

root.title("CRUD")
root.mainloop()