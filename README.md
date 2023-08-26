# M5 - Kenzie Buster
## Descrição
Neste projeto, desenvolvi uma api para gerenciar usuários, filmes e compras, com recursos de autenticação e permissões personalizadas para diferentes tipos de usuários. o Projeto foi feito com Python e o framework Django. Configuração do projeto: Configuração inicial do projeto, incluindo o arquivo .gitignore, ambiente virtual ( venv) e lista de dependências ( requirements.txt).
Customização do modelo de usuário: Personalização do modelo de usuário para atender aos requisitos específicos do projeto.
Registro de modelos no Django Admin: Registro dos modelos no Django Admin para facilitar a administração e visualização dos dados.
Implementação de serializadores convencionais: Criação de serializadores para serializar e desserializar objetos relacionados a usuários, filmes e compras.
Validação personalizada: Implementação de validações personalizadas nos serializadores para garantir a integridade dos dados.
Sobrescrita de métodos de serializadores: Personalização de métodos nos serializadores para adaptá-los às necessidades específicas do projeto.
Proteção de rotas com autenticação JWT e permissão customizada: Implementação de autenticação baseada em JWT e permissões personalizadas para controlar o acesso às rotas.
Tabela Pivô customizada: Criação de uma tabela pivô personalizada para lidar com a associação entre usuários, filmes e compras.
Campos de escolha para atributos de modelo: Adição de campos de escolha em certos modelos para limitar as opções disponíveis para determinados atributos.
Paginação com APIView: Implementação da funcionalidade de paginação para dividir os resultados em várias páginas e melhorar a eficiência da navegação pelos dados.
Foi implementado 40 testes e passei em todos
## Instalação dos pacotes de teste

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:
```shell
pip list
```
- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:
```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate

# git bash:
source venv/Scripts/activate
```

3. Instale o pacote `pytest-testdox`:
```shell
pip install pytest-testdox pytest-django
```

5. Vá até o arquivo `pytest.ini` e modifique o nome do projeto `my_project_name.settings` para o nome do **seu_projeto**.settings (onde se encontra o settings.py)

4. Agora é só rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```



## Rodando os testes de cada tarefa isoladamente

Ao fim de cada tarefa será possível executar uma suite de testes direcionada àquela tarefa específica. Lembre-se de sempre estar com o **virtual enviroment (venv) ativado**.

- Rodando testes da Tarefa 1:
```python
pytest --testdox -vvs tests/tarefas/t1/
```

- Rodando testes da Tarefa 2:
```python
pytest --testdox -vvs tests/tarefas/t2/
```

- Rodando testes da Tarefa 3:
```python
pytest --testdox -vvs tests/tarefas/t3/
```

- Rodando testes da Tarefa 4:
```python
pytest --testdox -vvs tests/tarefas/t4/
```
