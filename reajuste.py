#Programa realizado para calcular reajuste dos salários dos funcionários

salario = float(input('Digite o salário do colaborador: '))



if salario >= 1500:
    reajuste = 0.05
    aumento = salario*reajuste
    novo_salario = salario + aumento

    print(f'O salário antes do reajuste: {salario}')
    print(f'O percentual de aumento aplicado foi de {reajuste}')
    print(f'O valor do aumento foi de {aumento}')
    print(f'O novo salário, após o aumento é de {novo_salario}')

elif salario < 1500 and salario > 700:
    reajuste = 0.1
    aumento = salario*0.1
    novo_salario = salario + aumento

    print(f'O salário antes do reajuste: {salario}')
    print(f'O percentual de aumento aplicado foi de {reajuste}')
    print(f'O valor do aumento foi de {aumento}')
    print(f'O novo salário, após o aumento é de {novo_salario}')

elif salario < 700 and salario > 280:
    reajuste = 0.15
    aumento = salario*0.15
    novo_salario = salario + aumento
    
    print(f'O salário antes do reajuste: {salario}')
    print(f'O percentual de aumento aplicado foi de {reajuste}')
    print(f'O valor do aumento foi de {aumento}')
    print(f'O novo salário, após o aumento é de {novo_salario}')   

else:
    aumento = salario*0.20
    reajuste = 0.2
    novo_salario = salario + aumento
    
    print(f'O salário antes do reajuste: {salario}')
    print(f'O percentual de aumento aplicado foi de {reajuste}')
    print(f'O valor do aumento foi de {aumento}')
    print(f'O novo salário, após o aumento é de {novo_salario}')