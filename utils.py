from models import Pessoas, Usuarios

# Inseri dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Gabrielzito', idade=48)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)

    #pessoa = Pessoas.query.filter_by(nome='Perivaldo')
    #for p in pessoa:
    #    print(p)

    pessoa = Pessoas.query.filter_by(nome='Souza').first()
    print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Pedrolino').first()
    #pessoa.idade = 11
    pessoa.nome = 'Pedrolandio'
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Pedrolandio').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('perivaldo', '1234')
    insere_usuario('souza', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()
