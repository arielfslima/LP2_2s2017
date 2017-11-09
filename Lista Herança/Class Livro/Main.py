from ClassLivro import *

livro = Livro(input('Digite o nome do livro :'),int(input("Digite a quantidade de paginas desse livro :")),input("Digite o autor desse livro :"),int(input("Digite o preco desse livro : ")))

print("O preço do livro é R${}" .format(livro.getPreco()))

livro.setPreco(int(input("Deseja alterar o preco ? Digite o novo preco :")))

print("O novo preço do livro é R${}" .format(livro.getPreco()))