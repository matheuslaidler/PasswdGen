'''
Script feito por Matheus Laidler para um artigo ajudando a aprender Python.
* Gerador de palavra-chave aleatória e com regra *
Caso não queira alguma das regras, só colocar o valor 0. 
Ex: Se não quiser cartactere especial, deixe o tamanho de simbolos em 0.
'''

import random
import string
'''
Essas são as bibliotecas importadas. random é usada para gerar números aleatórios e string contém várias constantes de string úteis.
'''

def gerar_senha(qntd_letras, qntd_numeros, qntd_simbolos):
    '''
    Esta é a definição da função gerar_senha. Ela aceita três argumentos: o número de letras, números e símbolos que você deseja em sua senha.
    '''
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = "!@#$%¨'~^`´[]/\+-{}&*()_+?:;.,"
    '''
    Essas são as strings da bibllioteca que contêm todos os possíveis caracteres que podem ser usados na senha.
    '''
    senha = ''.join(random.choice(letras) for _ in range(qntd_letras))
    senha += ''.join(random.choice(numeros) for _ in range(qntd_numeros))
    senha += ''.join(random.choice(simbolos) for _ in range(qntd_simbolos))
    '''
    Aqui, estamos gerando uma string de caracteres aleatórios para cada tipo de caractere (letras, números e símbolos) e adicionando-os à senha.
    '''
    senha = ''.join(random.sample(senha, len(senha)))   
    return senha
    '''
    Aqui, estamos embaralhando todos os caracteres na senha para garantir que eles não estejam na ordem em que foram adicionados. Em seguida, retornamos a senha.
    '''  

def main():
    '''
    Esta é a função principal que será executada quando o script for iniciado.
    '''
    print("="*50)
    print(f"    Gerador de palavra-chave com regra definida")
    print("="*50 + "\n")
    print(f"            Feito por Matheus Laidler")
    print("="*50 + "\n")
    '''
    Printando mensagens na tela com estrutura. 
    O primeiro print é referente a estrutura falada que serve como separador visual.
    Ele é usado para imprimir uma linha de iguais ("=="), hífens (“-”), ou o que quiser colocar na tela. O * é um operador de multiplicação e quando usado com str, ele repete-a um determinado número de vezes. Então, print("="*60) imprime uma linha de 60 iguais. Isso é geralmente feito para melhorar a legibilidade da saída, agindo como uma espécie de separador visual entre diferentes seções de texto.
    O '\n' é uman forma de quebra de linha (pular linha), assim como quando usamos o print vazio, também mostrado mais abaixo.
    O ‘f’ antes das aspas indica uma string formatada. Uma nova maneira de formatar strings introduzida no Python 3.6. Elas são precedidas por ‘f’ e são usadas para incorporar expressões dentro de literais de str.
    '''
    qntd_letras = int(input("Digite uma quantidade de LETRAS: "))
    qntd_numeros = int(input("Digite uma quantidade de NÚMEROS: "))
    qntd_simbolos = int(input("Digite uma quantidade de CARACTERES ESPECIAIS: "))
    '''
    Estas são as instruções que solicitam ao usuário o número de letras, números e símbolos que eles desejam em sua senha.
    '''
    print("")
    print("="*50)
    print("")
    senha = gerar_senha(qntd_letras, qntd_numeros, qntd_simbolos)
    '''
    Aqui, chamamos a função gerar_senha para gerar uma senha com base nas entradas do usuário.
    '''
    print(f"O tamanho da sua senha gerada é: {len(senha)}")
    '''
    Imprimir o tamanho da senha antes de mostrá-la. A função len(senha) retorna o número de caracteres na senha.
    '''
    print("="*50)
    print(f"Palavra-chave: {senha}")
    print("="*50)
    
if __name__ == "__main__":
    main()
    '''
    Esta é uma construção comum em Python. 
    Quando o script é executado, ele define a variável "__name__" para "__main__", então essa condição se torna verdadeira e a função main() é chamada (iniciando o script). 
    Se esse script for importado como um módulo em outro script, "__name__" não será "__main__" e a função 'main()' não será chamada automaticamente. 
    Isso é útil quando você quer que certas coisas aconteçam quando o script é executado diretamente, mas não quando o código é importado como um módulo em outro script.
    '''
