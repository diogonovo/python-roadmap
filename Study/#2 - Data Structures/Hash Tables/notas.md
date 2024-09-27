estruturas de dados que implentam key-value de maneira altamente eficiente
Convertem uma key num indice de array

pode haver colisoes, onde duas chaves podem ter o mesmo indice.
Chaining e open addressing
open addressing usa linear probing ou quadratic probing

Inserção:
o indice do array é determinado, se houver colisao entra em ação a estrategia de colisao

Busca:
se houver colisao é necessário verificar a lista ligada(chaining) ou tentar as proximas posiçoes (open addressing)
remoção: semelhante à busca

são operações extremamente rapidas 
Usados em maps, contagem de frequencia, indexação de bases de dados.

Mas o seu desempenho depende da função de hash, se for mal feita vai demorar mais.
Se houver dados ordenados, nao sera vantajoso.

Usado em contagem de elementos
Lookup rápidos
dict é a hash table de python oimizada