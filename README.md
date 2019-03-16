# ThoughtWorks - Next Steps / Coding Assignment

André de Sousa Araújo

Problem one: Trains

The local commuter railroad services a number of towns in Kiwiland.  Because of monetary concerns, all of the tracks are 'one-way.'  That is, a route from Kaitaia to Invercargill does not imply the existence of a route from Invercargill to Kaitaia.  In fact, even if both of these routes do happen to exist, they are distinct and are not necessarily the same distance!

The purpose of this problem is to help the railroad provide its customers with information about the routes.  In particular, you will compute the distance along a certain route, the number of different routes between two towns, and the shortest route between two towns.

This repo shows some freatures to get information about the train routes.

# Notas (Em português)

Tecnicamente optei por criar uma classe para o grafo com as operações mais importantes: inserir vertices, inserir arestas, obter o vertice X (parametro), obter todos os ciclos e a função que faz uma  busca em largura (Breadth-First Search - BFS).

A **busca em largura** permite achar o menor caminho entre um nó raiz e os outros nós do grafo. **Neste caso, usando a bfs eu armazenei os caminhos e os respectivas distâncias.** A cada novo caminho encontrado, eu sumarizei as distâncias daquele caminho. **Além disto, adicionei uma função na busca em largura para recuperar os ciclos existentes para combinar com rotas básicas com rodas adicionais (de ida e volta)**.

E deixei a parte especializada sobre informações de rotas em outras classe (TrainRoutes):

- Obter todas rotas de uma origem para um destino
- Obter o menor caminho e tamanho de uma origem para um destino
- Calcular a distância de uma determinada rota. A estratégia utilizada foi caminhar no grafo somando as distâncias
- Obter a quantidade de paradas de uma origem para um destino, obter o máximo ou menor que um valor. **A estratégia foi usar a busca em largura para obter os caminhos, e contabilizar as quantidades de paradas destes caminhos. Assim bastou filtrar conforme os parâmetros**. 
- Obter todas os caminhos com uma distância máxima. **A estratégia foi também usar a busca em largura, mas controlar o máximo da distância ao caminhar para as rotas adjacentes. No algoritmo eu vou sumarizando o total da distância para cada caminho, e quando atingo o máximo para-se de caminhar. Isto não ficar indefinidamente caminhando por ciclos em um grafo**.

## Install guide

#### Create the virtualenv
```bash
$ virtualenv -p python3 twenv
$ source twenv/bin/activate
```

#### Install dependencies
```bash
$ pip install -r requirements.txt
```

#### Run the code and infom the INPUT:
``` bash
AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7 
```
If other input, remember to change the run.py with the correct parameters. Eg: In get_number_trips_by_stop('C', 'C', stops=3), the Town C should be exists in yout input.

```bash
$ python run.py
```

#### Test (Automated Tests)
```bash
$ make test
```

### PS: Formatação, estilo, comentários e documentação.

Usei o sublime text e formatei conforme o PEP8 Autoformat. Nome de classes não costumo user MixedCase, mas segui o PEP8. Já as demais regras eu segui normalmente, mas procuro seguir o estilo básico do time ou da empresa. Como também a opção de documentar classes, funções, pode variar optei por não fazê-lo, apenas coloquei nas classes de forma a demonstar a capacidade de fazer. Além disto, eu considero importante quando as classes ou funções serão expostas, mas não é caso, pois é um exercício.
