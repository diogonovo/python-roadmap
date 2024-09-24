python:

Linguagem dinamica e interpretada (compilada por bytescode). Não há declarações de variaveis, parametros, funções ou métodos no código fonte, o que torna o código mais curto e simples, mas ao mesmo tempo não ha essa verificação no momento da compilação e é apenas verificado no momento de execução.

A variavel "a" é diferente da variavel "A". Existe diferenciação entre minusculas e maiusculas.

O fim de cada linha marca o fim de uma instrução, que ao contrario do que existe com outras linguagens em que utilizamos o ";" ou "." para terminar, aqui deixamos sem marcação.
Comentários: "#" no inicio da linha

A extensão dos arquivos é ".py" e são chamados de "módulos".
Módulo: "hello_world.py" 
CMD: "python hello_world.py Diogo" #executa o modulo e passa o argumento Diogo

EX:
    #!/usr/bin/python3

    # import modules used here -- sys is a very standard one
    import sys

    # Gather our code in a main() function
    def main():
        print('Hello there', sys.argv[1])
        # Command line args are in sys.argv[1], sys.argv[2] ...
        # sys.argv[0] is the script name itself and can be ignored

    # Standard boilerplate to call the main() function to begin
    # the program.
    if __name__ == '__main__':
        main()

Os tabs também delimitam as funções. Usar espaços em vez de tabs por segurança e evitando erros.
Configurar o editor para substituir o tab por espaços para seguir recomendações do PEP 8


Quando o módulo é executado diretamente a variavel __name__ é definida como __main__ para garantir que apenas é executado diretamente e não como importado.
if __name__ == "__main__":
    main()

É permitido também passar argumentos na linha de comandos através da lista sys.arg que pertence ao módulo sys.
sys.argv[0] sempre contém o nome do script ou programa que está a ser executado.
sys.argv[1], sys.argv[2], etc., contêm os argumentos fornecidos na linha de comando.

A função len() devolve o tamanho de objetos, pode ser o numero de itens de uma lista, tupla, string ou pares key-value de um dicionario.
len(sys.argv) devolve o numero de argumentos passados para o script incluindo o nome do proprio script.

As funções sao definidas pela palavra "def" que indicia a criação de uma nova função, seguido do nome da função e dos parametros entre parentises.
def repeat(s, exclaim):
    pass

Boa prática adicionar docstrings a seguir as funções para adicionar uma descriçao da função. docstring são triplas aspas. Exemplo:
"""
Returns the string 's' repeated 3 times.
If exclaim is true, add exclamation marks.
"""

Identar a função com 4 espaços para identificar o que faz parte da função.

as funções podem retornar valores com a instrução "return"
return result

Os operadores + e * podem ser usados de maneiras diferentes para diferentes tipos de dados.
O operador + pode ser usado para concatenar strings.
O operador * pode ser usado para repetir strings.


Variaveis dentro de uma função são locais à funçao e nao podem ser acedidas fora dela.

Uma pratica comum é usar a função main para organizar a execução de outras funções.
definir uma função main() e chamá-la condicionalmente quando o script é executado diretamente, mas não quando o módulo é importado.
as funções devem ser definidas antes de serem chamadas no codigo, daí a função main normalmente ficar no fim para depois organizar consoante as funções que foram definidas em cima.
isto garante que a função main é execuada quando o módulo é executado diretamente e não quando é importado por outro módulo.


python3 adicionou tipagem na definição de variaveis e argumentos, permitindo assim alguma ajuda de editores ao programar e garantir que os tipos estão em concordancia.
Caso contrario o python só irá dar erro quando estiver a executar e a usar essa variavel, em tempo de execução.
Neste caso, NameError.

ao importar módulos, podemos chamar as funções que tiverem dentro desse módulo como no seguinte exemplo:
Chamamos a função exit que está dentro do módulo sys, com sys.exit(0)

import sys

  # Now can refer to sys.xxx facilities
  sys.exit(0)



Python oferece uma classe embutida "str" em vez da classe antiga string, que oferece muitos recursos uteis.
Podemos definir strings com '' "" ou triplas aspas para quando tem mais que uma linha

Para inserir caracteres especiais usamos escape com barra invertida \n nova linha \\ usar a barra \" aspas
Podemos usar também aspas normais dentro de uma string delimitada por pelicas ' teste "aspas" final '

As strings em python sao imutaveis, ou seja, uma vez criada não é alterada, em vez disso é sempre criada uma nova.
Podemos aceder a caracteres de uma string com o seu indice dentro de []
s = "teste" 
s[0] -> letra "t"
Assim como fazer slice
s[0:2] -> "tes" # a primeira posição é indice 0 a segunda posição é indice 1 e assim sucessivamente 
Se tentar aceder a um indice fora do possivel, gera erro.

com a função len() podemos ver o numero de caracteres da string
com o operador + podemos juntar strings

Python suporta os operadores aritméticos comuns: +, -, *, /, mas não tem um operador ++ como em C/C++. 
Porém, pode-se usar operadores como += para fazer a soma e atribuição ao mesmo tempo.

Para dividirmos numeros inteiros usamos o //

uma raw string é prefixada com "r", estas strings sao usadas de forma literal, nao tem escape da barra invertida
raw_string = r'teste de string raw /n nova' # o /n é usado como texto

O comando print() em Python exibe strings no terminal e, por padrão, adiciona uma nova linha no final de cada impressão.
Se você quiser evitar a nova linha, pode definir o parâmetro end="":
print("hello", end="")  # Não adiciona nova linha após "hello"
print(" world")

lower() e upper() transformam tudo em minusculas e maiusculas respetivamente
strip() remove espaços em branco no inicio e fim da string
isalpha(): verifica se todos os caracteres são letras.
isdigit(): verifica se todos os caracteres são dígitos.
isspace(): verifica se todos os caracteres são espaços em branco.
startswith('other') verifica se começa com other
endswith('other') verifica se termina com other
find('other') procura a palavra other e devolve o indice da primeira ocorrencia, caso nao tenha devolve -1
replace('old', 'new') substitui o old pelo new
split() dividie a string em substrings com base num delimitador que passarmos 
join() oposto do split, se passarmos uma lista, junta tudo numa string

quando usamos indices:
podemos fazer sem indice inicial e é assumido o inicio da string e vice versa
podemos usar indices negativos para fazer contagem de tras para frente
fora do limite da erro
combinar indices negativos com positivos


F-Strings:
maneira nova e eficiente de formatar strings
Prefixar com "f" e incluir expressões dentro de {}

value = 2.791514
print(f'approximate value = {value:.2f}')  
    # Saída: "approximate value = 2.79"
--
car = {'tires': 4, 'doors': 2}
print(f'car = {car}')  
    # Saída: "car = {'tires': 4, 'doors': 2}"
--
address_book = [
    {'name': 'N.X.', 'addr': '15 Jones St', 'bonus': 70},
    {'name': 'J.P.', 'addr': '1005 5th St', 'bonus': 400},
    {'name': 'A.A.', 'addr': '200001 Bdwy', 'bonus': 5},
]

for person in address_book:
    print(f'{person["name"]:8} || {person["addr"]:20} || {person["bonus"]:>5}')

    #N.X.     || 15 Jones St          ||    70
    #J.P.     || 1005 5th St          ||   400
    #A.A.     || 200001 Bdwy          ||     5
neste caso, 8 20 e >5 representam largura e alinhamento das colunas

Operador % (antigo printf)
%d: Inteiros.
%s: Strings.
%f / %g: Números de ponto flutuante.

text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house')
print(text)
    # "3 little pigs come out, or I'll huff, and I'll puff, and I'll blow your house down."

Quando uma linha com % fica muito longa podemos usar os parenteses para agrupar e permitir a sua quebra em varias linhas
Ao mesmo tempo tambem permite concatenaçao automatica quando temos aspas adjacentes

str.Format()
Permite substituir os marcadores {} dentro de uma string pelos valores correspondentes passados como argumentos
text = "The value of pi is {:.2f}".format(3.14159)
print(text)  # Saída: "The value of pi is 3.14"

Recomendado usar F-Strings
operador % é mais antigo
format() poderoso e versátil mas quando tem muitas variaveis fica menos legivel


Strings Unicode vs Bytes

Strings Unicode:
Strings padrão em Python são Unicode, o que significa que podem armazenar caracteres de várias línguas e símbolos usando uma representação mais ampla do que simples bytes.
Unicode é o padrão moderno para representar texto em sistemas de informática, pois inclui caracteres de praticamente todos os idiomas e sistemas de escrita.

Strings Bytes:
Python também oferece suporte a strings de bytes, que são literais de string prefixados com um "b". As strings de bytes são úteis quando você está lidando com dados binários, como arquivos ou transmissões de rede, e representam sequências de bytes em vez de caracteres de texto.
Exemplo:
python
Copiar código
byte_string = b'A byte string'
print(byte_string)  # Saída: b'A byte string'
As strings de bytes não são equivalentes a strings Unicode. São tipos diferentes, mas podem ser convertidos entre si.

usamos o encode() para converter unicode em bytes
ustring = 'A unicode \u018e string \xf1'
b = ustring.encode('utf-8')  # Converte para bytes usando codificação UTF-8
print(b)  # Saída: b'A unicode \xc6\x8e string \xc3\xb1'

decode() bytes em unicode
t = b.decode('utf-8')  # Converte de bytes de volta para Unicode
print(t == ustring)  # Saída: True



IF em Python
em python nao se usa () nem {} para agrupar, em vez disso usa-se ":" e espaços para agrupar
Ter atenção aos espaços, devem ser rigorosamente alinhados para nao dar erro

if condition:
    print('This is true')
else:
    print('This is false')

Usar o else ou elif caso queiramos por outra condição
if time_hour >= 0 and time_hour <= 24:
    if mood == 'sleepy' and time_hour < 10:
        print('coffee')
    elif mood == 'thirsty' or time_hour < 2:
        print('lemonade')
    else:
        print('water')

em python qualquer valor pode ser usado no if 
None,0,'',[],{} são avaliados como falso os outros sao verdadeiros
True e False, equivalente a 1 ou 0 
Operadores comuns: == != < <= >= e >
Operadores and or e not em vez de && || ou | (e ou não)



Listas em python -> []
podem ter elementos de qualquer tipo
assim como com as strings, podemos aceder através dos indices
atribuir uma lista a outra variavel nao cria uma copia, mas sim uma referencia para aquela lista na memoria. Se alterarmos a original ou a referencia, afeta as 2.
Podemos concatenar listas com o operador + 

Loops For e In
para percorrer cada elemento de uma lista
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum)  # Saída: 30
tentar usar nomes que descrevam o conteudo da lista, para melhor entender o codigo

Podemos usar também o in para ver se temos um item numa lista
if 't' in ['t','d']

for ch in 'hello':
    print(ch)
loop iterado por caracter

range()
gera uma sequencia de numeros de 0 a n-1
for i in range(100)
    print(i)
isto vai imprimir valores de 0 a 99


Loop While
repete o bloco de codigo até a condição ser verdadeira

i = 0
while i < len(colors):
    print(colors[i])
    i += 1  # Incrementa o índice
podemos usar o break para saltar fora do while e continue para passar para a proxima iteraçao do loop 

Métodos de listas
list.append(elem)
adiciona um elemento ao final da lista, apenas modifica nao retorna uma lista nova
list.insert(index,elem) insere numa posição especifica, movendo os outros para a direita
list.extend(list2) adiciona a list2 ao fim da list, identico ao + ou +=
list.index(elem) retorna o indice da primeira ocorrencia de um elemento na lista
list.remove(elem) remove a primeira instancia do elemento da lista. caso nao seja encontrado lança um ValueError
list.sort() modifica a lista original nao retorna
list.reverse() inverte a ordem 
list.pop(index) retorna o elemento no indice indicado 

da erro por exemplo, fazer print de uma lista com um metodo que nao retorna nada
comum será iniciar uma lista vazia e ir adicionando elementos conforme necessario co append ou extend 

o slice de listas funciona da mesma maneira das strings, com os indices
list[1:-1]
tambem pode ser usado para substituir partes da lista 