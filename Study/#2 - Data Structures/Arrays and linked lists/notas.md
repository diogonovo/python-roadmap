Diferenciar Arrays de linked lists
Como o NumPy otimiza arrays em relação aos arrays normais
como os views do numpy economizam memoria, porque nao cria copias mas views do array
Ver VLists
Lock-Free linked lists
Skip Lists
Linked Arrays
CuPy
Dask


NumPy Arrays:
Alinhamento de Memória e SIMD para execução de múltiplas operações em uma única instrução.
Evitar cópias desnecessárias com views em vez de copies.
Uso de GPUs com bibliotecas como CuPy para paralelizar cálculos.
Evitar operações sequenciais; sempre que possível, utilizar vetorização.

Linked Lists:
Minimizar o impacto de cache misses usando variações como VLists ou skip lists.
Para ambientes concorrentes, utilizar listas ligadas sem bloqueios (lock-free linked lists).
Considerar estruturas híbridas como linked arrays para melhorar localidade de cache e flexibilidade.