from models import Pessoas

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

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
