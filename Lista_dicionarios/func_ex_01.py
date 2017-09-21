def euclides(m,n):
    anterior = n
    atual = m
    resto = anterior % atual

    while resto != 0:
        anterior = atual
        atual = resto
        resto = anterior % atual

    print('MDC(%d,%d)=%d' % (n, m, atual))
    return atual

def contagemvogal(text):
    contvogal = 0
    for c in text:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u"  :
            contvogal = contvogal + 1
    return contvogal

def notaaluno(aluno, nt1, nt2 ):

    if not aluno == None:
        classe = {
            'aluno': [nt1,nt2]
        }
        return


def entrada_produtos(nome_produto, qtd):
    produtos = {
        'tomate': [100, 2.3],
        'alface': [500, 0.45],
        'laranja': [300, 1.3],
        'cenoura': [130, 2.1],
        'manga': [75, 3.45],

    }
    tupla_produtos = tuple(produtos.keys())
    #nome_produto = input('digite o nome do produto: ')
    if nome_produto == 'fim':
        return -1
    elif not nome_produto in tupla_produtos:
        return None
    else:
     #   qtd = input('quantidade: ')
        produto = produtos[nome_produto]
        dic_retorno = {nome_produto: [qtd, produto[1]]}
        return dic_retorno

def notas():
    nomes = []
    nt1 = []
    nt2 = []
    alunos = { }

    while 1:
        nome = input("Qual o nome do aluno?")
        if nome == ' ':
            break;
        nt1.append(int(input("Qual a primeira nota?")))
        nt2.append(int(input("Qual a segunda nota?")))
        nomes.append(nome.lower())

    i = 0
    while i < len(nomes):
        alunos[nomes[i]] = [nt1[i], nt2[i]]
        i+=1

    return alunos

def med_aluno(nome, notas):
    for i in notas:
        if i == nome:
            notas = notas[i]
            break
    media = (notas[0]+notas[1])/2
    return media

# alunos = notas()
# nome = input("Qual o nome do aluno que voce deseja saber a media?")
# print(media_aluno(nome, alunos))

