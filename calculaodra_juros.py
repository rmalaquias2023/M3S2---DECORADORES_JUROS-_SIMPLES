def decorador_imprimir (function):
    def mensagem (*args, **kwargs):
        function (*args, **kwargs)
        print (f'Capital: R${capital}, Taxa: {taxa}, Tempo: {tempo}')
        print (f'Resultado: R$ {function(*args, **kwargs):.2f}')
    return mensagem


@decorador_imprimir
def juros_simples(capital, taxa, tempo):
    juros_simples = capital * (taxa/100) * tempo    
    return juros_simples

capital = int(input('Digite o valor do capital investido: '))
taxa = int(input('Qual a taxa de Juros (em porcentagem)? '))
tempo = int(input('Qual o prazo de pagamaento (em meses)? '))

resultado = juros_simples (capital, taxa, tempo)

print (resultado)
