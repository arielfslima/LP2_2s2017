from ClassFunc import *

funcionario = Funcionario(input("Digite o nome do funcionario : "),int(input("Digite o salario dele :")))

asalario = funcionario.AumentaSalario(int(input('qual sera o aumento dele ?  em % :')))

print(" O novo salario sera de R${}" .format(asalario))

