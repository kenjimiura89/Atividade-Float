#Um freelancer está com dificuldade para calcular qual o valor cobrar por um projeto que está estimado em 80 horas.
#Após pensar e revisitar o preço de alguns projetos que cobrou no passado ele montou a seguinte fórmula:
#valor inicial + quantidade de horas estimadas * valor da hora + 15% do valor calculado.
#Sua tarefa é criar um programa que faça essa conta para o freelancer.
#Considere que o valor inicial sempre será 1000,00 R$ e o valor da hora cobrada é de 20,45 R$.
#A aplicação deve imprimir o valor calculado pelo projeto considerando duas casas decimais na formatação do valor.
#Dica: Olhar a ordem como as operações da fórmula devem ser realizadas.

valor_inicial = float(1000.00)
valor_trabalhadas = float(input('informe o valor de horas'))
valor_horas = float(20.45)
porcentagem = float(0.15)

Valor_final = valor_inicial +(valor_trabalhadas*valor_horas)+porcentagem
print("o valor do projeto é de R$", Valor_final)