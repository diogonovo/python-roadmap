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


1. Funções de Ordenação (Sorting)
sorted():
A função sorted() é usada para ordenar qualquer coleção iterável e retorna uma nova lista com os elementos ordenados. Ela não altera a lista original.

Exemplo:
a = [5, 1, 4, 3]
print(sorted(a))  # Saída: [1, 3, 4, 5]
print(a)          # Saída: [5, 1, 4, 3]

Argumentos opcionais:
reverse=True: para ordenar em ordem decrescente.
strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs, reverse=True))  # Saída: ['zz', 'aa', 'CC', 'BB']
key=: permite personalizar a forma como os elementos são comparados, passando uma função como argumento. A função key transforma cada elemento antes da comparação.
Exemplo: Ordenar uma lista de strings pelo comprimento das strings.
strs = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(strs, key=len))  # Saída: ['d', 'bb', 'ccc', 'aaaa']
Exemplo: Ignorar a diferenciação entre maiúsculas e minúsculas na ordenação.
print(sorted(strs, key=str.lower))  # Saída: ['aa', 'BB', 'CC', 'zz']

Você também pode criar suas próprias funções key. Por exemplo, para ordenar por última letra de cada string:
strs = ['xc', 'zb', 'yd', 'wa']
def MyFn(s):
    return s[-1]
print(sorted(strs, key=MyFn))  # Saída: ['wa', 'zb', 'xc', 'yd']
list.sort():
list.sort() é um método que modifica a lista original em vez de retornar uma nova lista. Ele classifica a lista "no lugar".

Exemplo:
alist = [3, 1, 2]
alist.sort()
print(alist)  # Saída: [1, 2, 3]
Diferença entre sorted() e list.sort():
sorted(): retorna uma nova lista, funciona com qualquer coleção iterável.
list.sort(): modifica a lista original e funciona apenas com listas.

2. Tuplas
Uma tupla é semelhante a uma lista, mas é imutável (seus elementos não podem ser modificados depois de criados). São definidas usando parênteses ( ).
Exemplo:
tuple = (1, 2, 'hi')
print(tuple[2])  # Saída: 'hi'

Tuplas de um único elemento precisam de uma vírgula após o elemento para serem corretamente identificadas como tuplas:
single_element_tuple = ('hi',)

Tuplas podem ser usadas como uma maneira conveniente de armazenar vários valores e retorná-los de uma função. Por exemplo, uma função pode retornar várias coordenadas:
(x, y, z) = (42, 13, "hike")
print(z)  # Saída: 'hike'

Atribuição múltipla:
Quando uma tupla é atribuída a outra com o mesmo número de elementos, cada valor correspondente é atribuído às variáveis respectivas:
(first_name, last_name) = ("John", "Doe")
print(first_name)  # Saída: 'John'

3. Compreensão de Listas (List Comprehension)
Compreensão de lista é uma maneira concisa de criar listas com base em outra lista ou iterável. A sintaxe básica é:
[expr for var in iterable]

Exemplo básico:
nums = [1, 2, 3, 4]
squares = [n * n for n in nums]
print(squares)  # Saída: [1, 4, 9, 16]

Compreensão de listas com condições:
Você pode adicionar condições para filtrar os elementos:
nums = [2, 8, 1, 6]
small_nums = [n for n in nums if n <= 2]
print(small_nums)  # Saída: [2, 1]

Exemplo com strings:
Criar uma nova lista com strings maiúsculas e adicionar "!!!" a cada uma:
strs = ['hello', 'and', 'goodbye']
shouting = [s.upper() + '!!!' for s in strs]
print(shouting)  # Saída: ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']

Compreensão de listas com if:
Você pode adicionar um filtro condicional na compreensão de lista:
fruits = ['apple', 'banana', 'cherry', 'lemon']
afruits = [f.upper() for f in fruits if 'a' in f]
print(afruits)  # Saída: ['APPLE', 'BANANA']



1. Dicionários (Dict)
Os dicionários são uma das estruturas de dados mais eficientes do Python para armazenar pares chave-valor. São implementados usando tabelas de hash, o que significa que a busca, inserção e exclusão de itens é rápida.

Criação de Dicionários:
Um dicionário vazio é criado com {}.
Para adicionar pares chave-valor:
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'
print(dict)  # Saída: {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

Acessando e Modificando Valores:
Para acessar um valor, usa-se a chave entre colchetes:
print(dict['a'])  # Saída: 'alpha'
dict['a'] = 6  # Modifica o valor associado à chave 'a'
Verificar se uma chave existe:
'a' in dict  # Retorna True se a chave 'a' estiver presente

Para evitar um erro KeyError ao acessar uma chave inexistente, pode-se usar get():
print(dict.get('z'))  # Retorna None se a chave 'z' não existir
print(dict.get('z', 'default'))  # Retorna 'default' se não encontrar

Iteração sobre Dicionários:
Iterar sobre um dicionário retorna as chaves por padrão:
for key in dict:
    print(key)  # Itera sobre as chaves

Você pode usar métodos como keys(), values(), e items() para iterar sobre as chaves, valores, ou pares chave-valor:
for key, value in dict.items():
    print(key, '>', value)  # Saída: a > alpha, o > omega, g > gamma
    
Para ordenar as chaves:
for key in sorted(dict.keys()):
    print(key, dict[key])

Métodos Úteis:
del: Remove uma chave do dicionário:
del dict['a']
print(dict)  # Saída: {'o': 'omega', 'g': 'gamma'}

2. Manipulação de Arquivos
Em Python, o método open() é usado para abrir arquivos. Ele retorna um file handler que pode ser usado para ler ou escrever dados.

Leitura de Arquivos:
Abrir um arquivo para leitura:
f = open('foo.txt', 'r', encoding='utf-8')
for line in f:
    print(line, end='')  # Itera sobre as linhas do arquivo
f.close()
Ao usar o modo r (leitura), você pode iterar pelas linhas do arquivo diretamente. Isso é útil para grandes arquivos, pois não carrega tudo na memória de uma vez.

Para ler todo o conteúdo do arquivo de uma vez:
content = f.read()  # Lê o arquivo inteiro como uma string

Escrita de Arquivos:
Para abrir um arquivo para escrita:
f = open('output.txt', 'w', encoding='utf-8')
f.write("This is a test.\n")
f.close()

Alternativamente, você pode usar print() com o argumento file para escrever:
print("This is a test.", file=f)

Unicode em Arquivos:
Para ler ou escrever arquivos Unicode, use o modo 't' (texto) e especifique a codificação:
with open('foo.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        print(line)

with open('output.txt', 'wt', encoding='utf-8') as f:
    f.write("Texto em Unicode.\n")

3. Melhores Práticas: Desenvolvimento Incremental
Ao desenvolver em Python (ou em qualquer linguagem), é uma boa prática seguir o desenvolvimento incremental, ou seja, criar o código em pequenos passos que podem ser testados imediatamente.

Primeiros Marcos:
Em vez de tentar escrever todo o programa de uma vez, comece com pequenos objetivos. Por exemplo, comece extraindo e processando um conjunto de dados simples. Teste esse passo, e depois siga para o próximo.

Saídas de Depuração:
Durante o desenvolvimento, use print() ou outras técnicas para exibir as variáveis e verificar o comportamento do programa antes de continuar.

Pequenas Alterações:
Pequenas modificações seguidas de testes rápidos são uma maneira eficiente de garantir que cada parte do código esteja funcionando corretamente antes de integrar mais funcionalidades.

Expressões regulares:
python usar o "re." 
match = re.search(pat, str)
procura o padrao pat na string str
usar normalmente um if para validar que existe

import re

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
  print('found', match.group()) ## 'found word:cat'
else:
  print('did not find')

padrões basicos:
a, X, 9, < -- caracteres comuns apenas correspondem exatamente a si mesmos. Os metacaracteres que não correspondem entre si porque possuem significados especiais são: . ^ $ * + ? { [ ] \ | ( ) (detalhes abaixo)
. (um ponto) -- corresponde a qualquer caractere único, exceto a nova linha "\n"
\w -- (w minúsculo) corresponde a uma "palavra" caractere: uma letra, dígito ou barra inferior [a-zA-Z0-9_]. Embora a palavra "word" é a mnemônica disso, ela corresponde somente a uma única palavra, não a uma palavra inteira. \W (W maiúsculo) corresponde a qualquer caractere que não seja uma palavra.
\b: limite entre palavras e não palavras
\s -- (s minúsculos) corresponde a um único caractere de espaço em branco -- espaço, nova linha, retorno, tabulação, formulário [ \n\r\t\f]. \S (S maiúsculo) corresponde a qualquer caractere que não seja um espaço em branco.
\t, \n, \r -- tab, nova linha, retornar
\d: dígito decimal [0-9] (alguns utilitários de regex mais antigos não são compatíveis com \d, mas todos são compatíveis com \w e \s)
^ = início, $ = fim: corresponde ao início ou ao fim da string
\ -- inibir a "especialidade" de um personagem. Por exemplo, use \. para corresponder a um ponto ou \\ para corresponder a uma barra. Se você não tiver certeza se um caractere tem um significado especial, como "@", tente colocar uma barra na frente dele, \@. Se não for uma sequência de escape válida, como \c, seu programa em Python será interrompido com um erro.

a pesquisa é feita pela string de inicio ao fim, todos os padroes tem que ser correspondentes mas nao a string toda, se for bem sucedido o match.group() devolve o texto correspondente.

+ -- uma ou mais ocorrências do padrão à esquerda, por exemplo, "i+" = um ou mais "i"
* -- 0 ou mais ocorrências do padrão à esquerda
? -- corresponde a 0 ou 1 ocorrência do padrão à esquerda

match = re.search(r'i+', 'piigiiii') # found, match.group() == "ii"

podemos usar o [] para indicar um conjunto de caracteres
e usar () para agrupar

  str = 'purple alice-b@google.com monkey dishwasher'
  match = re.search(r'([\w.-]+)@([\w.-]+)', str)
  if match:
    print(match.group())   ## 'alice-b@google.com' (the whole match)
    print(match.group(1))  ## 'alice-b' (the username, group 1)
    print(match.group(2))  ## 'google.com' (the host, group 2)


    findall() procura todas as correspondencias

    por exemplo usar o findall para pesquisar em todo o arquivo, em vez de iterar linha a linha
    usando findall com os () podemos fazer uma lista de tuplas key value com as correspondencias

IGNORECASE -- ignorar diferenças em maiúsculas/minúsculas para correspondência, de modo que "a" corresponde a "a" e "A".
DOTALL: permite que o ponto (.) corresponda a "newline" -- normalmente corresponde a qualquer coisa, exceto "newline". Isso pode confundir você, já que acha que .* corresponde a tudo, mas, por padrão, não vai além do fim de uma linha. Observe que \s (espaço em branco) inclui novas linhas. Portanto, se você quiser fazer a correspondência com um espaço em branco que possa incluir uma nova linha, basta usar \s*
MULTILINE -- Dentro de uma string composta por muitas linhas, permita que ^ e $ correspondam ao início e ao final de cada linha. Normalmente, ^/$ corresponde ao início e ao fim de toda a string.

Greedy vs Non-Greedy
o uso de ? no final das expressões

Substituiçao
re.sub(pat, replace, str)



Sistema de Arquivos:
documentos do módulo os
files = os.listdir(dir) -- lista de nomes de arquivos no caminho do diretório (não incluindo . e ..). Os nomes dos arquivos são apenas os nomes no diretório, não os caminhos absolutos.
os.path.join(dir, filename) -- considerando um nome de arquivo da lista acima, use-o para juntar o diretório e o nome de arquivo para criar um caminho
os.path.abspath(path): determinado caminho, retorna uma forma absoluta, por exemplo, /home/nick/foo/bar.html
os.path.dirname(path), os.path.basename(path) -- considerando dir/foo/bar.html, retorne o dirname "dir/foo" e basename "bar.html"
os.path.exists(path): verdadeiro se existir
os.mkdir(dir_path) -- cria um diretório, os.makedirs(dir_path) cria todos os diretórios necessários nesse caminho.
launchil.copy(source-path, dest-path) -- copia um arquivo (os diretórios de caminho de destino devem existir)

O módulo *subprocess* é uma forma simples de executar um comando externo e capturar a saída dele.

documentos do módulo subprocess
output = subprocess.check_output(cmd, stderr=subprocess.STDOUT) – executa o comando, aguarda a saída dele e retorna o texto de saída. O comando é executado com a saída e o erro padrão combinados em um texto de saída. Em caso de falha, ele lança um CalledProcessError.
Se você quiser ter mais controle sobre a execução do subprocesso, consulte a classe subprocess.popen.
Existe também um subprocess.call(cmd) simples que executa o comando, despeja a saída na saída e retorna o código de erro. Isso funciona se você quiser executar o comando, mas não precisar capturar a saída nas estruturas de dados do Python.

Exceções:
try:
    ## Either of these two lines could throw an IOError, say
    ## if the file does not exist or the read() encounters a low level error.
    f = open(filename, 'rb')
    data = f.read()
    f.close()
  except IOError:
    ## Control jumps directly to here if any of the above lines throws IOError.
    sys.stderr.write('problem reading:' + filename)
  ## In any case, the code then continues with the line after the try/except


HTTP -- urllib e urlparse
O módulo *urllib.request* fornece busca de URL, fazendo com que o URL pareça um arquivo que você pode ler. O módulo *urlparse* pode separar e reunir URLs.

Documentação do módulo urllib.request
ufile = urllib.request.urlopen(url) -- retorna um arquivo como um objeto para esse URL
text = ufile.read() -- pode ler a partir dele, como um arquivo (readlines() etc. também funciona)
info = ufile.info() -- a metainformação da solicitação. info.gettype() é o tipo MIME, por exemplo, "text/html"
baseurl = ufile.geturl() -- obtém a "base" URL para a solicitação, que pode ser diferente do original devido aos redirecionamentos
urllib.request.urlretrieve(url, nome de arquivo) -- faz o download dos dados de URL para o caminho de arquivo fornecido
urllib.parse.urljoin(baseurl, url): com base em um URL que pode ou não estar completo e o baseurl da página de origem, retorna um URL completo. Use geturl() acima para fornecer o URL base.
Todas as exceções estão em urllib.error.
-------
## Version that uses try/except to print an error message if the
## urlopen() fails.
def wget2(url):
  try:
    ufile = urlopen(url)
    if ufile.info().get_content_type() == 'text/html':
      print(ufile.read())
  except IOError:
    print('problem reading url:', url)