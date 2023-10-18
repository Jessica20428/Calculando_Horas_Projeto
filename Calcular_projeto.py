#Construa um programa que calcule: Quanto devemos cobrar em um projeto de programação
#se trabalhamos 8h por dia, demoramos 15 dias para fazer o projeto e cobramos R$100/h?

horas_por_dia = 8
dias_totais = 15
custo_hora = 100

horas_trabalho = horas_por_dia * dias_totais
custo_total = horas_trabalho * custo_hora
print(f'O valor que tem que ser cobrado pelo Projeto de Programação é: R${custo_total}')