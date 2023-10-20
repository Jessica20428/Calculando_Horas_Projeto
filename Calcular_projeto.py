#Construa um programa que calcule: Quanto devemos cobrar em um projeto de programação
#se trabalhamos 8h por dia, demoramos 15 dias para fazer o projeto e cobramos R$100/h?

#Declarando a constante horas_por_dia recebendo o valor 8  OBS: As constantes não podem ser alteradas
horas_por_dia = 8
#Declarando a constante dias_totais recebendo o valor 15
dias_totais = 15
#Declarando a constante custo_hora recebendo o valor de 100
custo_hora = 100

#Descobrindo as horas de trabalho, multiplicando as horas por dia * os dias que foram trabalhados
horas_trabalho = horas_por_dia * dias_totais
#Descobrindo o custo total do projeto a ser cobrado, multiplicando as horas totais trabalhadas * o custo das horas 
custo_total = horas_trabalho * custo_hora
#Exibindo o resultado do valor de quanto deve ser cobrado no projeto
print(f'O valor que tem que ser cobrado pelo Projeto de Programação é: R${custo_total}')