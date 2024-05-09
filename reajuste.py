salario = float(input('Digite o salário do colaborador: '))
#reajuste = float(input('Digite o reajuste: '))


if salario <= 280:
    reajuste = 0.2
    
elif salario <= 700:
    reajuste = 0.15
    
elif salario < 1500:
    reajuste = 0.1

else:
    reajuste = 0.05
    

aumento = salario*reajuste
novo_salario = salario + aumento
    
print(f'O salário antes do reajuste: {salario}')
print(f'O percentual de aumento aplicado foi de {reajuste}%')
print(f'O valor do aumento foi de {aumento}')
print(f'O novo salário, após o aumento é de {novo_salario}')