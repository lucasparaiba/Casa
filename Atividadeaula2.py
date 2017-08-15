"""
1) Composição
2) Descrição, data inicio, data fim, propriedade
3) Uma tarefa é solicitada por uma pessoa juridica e é execultada por uma pessoa fisica
"""

class tarefa():
	descricao = ''
	data_inicio = ''
	data_fim = ''
	propriedade = ''
	def __init__(self, descricao, data_inicio, data_fim, propriedade, nome, codigo):
		self.descricao = descricao
		self.data_inicio = data_inicio
		self.data_fim = data_fim
		self.propriedade = propriedade
		self.projeto = projeto(nome, codigo)

	def __str__(self):
		return self.descricao, self.data_inicio, self.data_fim, self.propriedade, self.projeto.__str__()


class Pessoa():
    nome = ''
    data_nascimento= None

    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, data_nascimento):
    	Pessoa.__init__(self, nome, data_nascimento)
    	self.cpf = cpf

class PessoaJuridica(Pessoa):
    def __init__(self, CNPJ, nome, data_nascimento):
    	Pessoa.__init__(self, nome, data_nascimento)
    	self.CNPJ = CNPJ

class projeto(object):
	codigo = None
	nomePro = ''
	def __init__(self, codigo, nomePro):
		self.codigo = codigo
		self.nomePro = nomePro

	def __str__(self):
		return self.codigo, self.nomePro

class Solicitacao():
	codigo = None
	def __init__(self, codigo, tarefa, pessoaJuridica):
		self.codigo = codigo
		self.tarefa = tarefa
		self.pessoaJuridica = pessoaJuridica

class Ex():
	codigo = None
	def __init__(self, codigo,tarefa, PessoaFisica):
		self.codigo = codigo
		self.tarefa = tarefa
		self.PessoaFisica



t =Tarefa()
p =`PessoaJuridica()

Solicitacao(13, t, p)


t = tarefa("Cont","Hoje","Amanha","Minha","Ceulp", 4356456345643);
print(t.__str__())