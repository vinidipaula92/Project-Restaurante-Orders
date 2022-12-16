# Boas-vindas ao repositório do projeto `Restaurant Orders`!

# Seja bem vindo ao projeto Trybers and Dragons!

## Stack utilizada

**Back-end:** Typescript, NodeJs e Arquitetura SOLID

<details>
  <summary><strong>👨‍💻 O que foi desenvolvido</strong></summary>
    
A lanchonete :baguette_bread: :cook: Pão na Chapa :baguette_bread: :cook: possui um sistema de faturamento de pedidos de clientes que salva o nome da pessoa, o pedido realizado e o dia da semana do atendimento. A gerência da lanchonete está aumentando suas vendas e melhorando sua gestão interna e, para isso, implementei um projeto de melhorias, o Projeto `Restaurant Orders`. </br>
    Em um primeiro momento, eu fiz com que o sistema gere relatórios com informações sobre os pedidos e as pessoas clientes que frequentam a lanchonete. Estes dados auxiliam o trabalho de uma agência de marketing com o objetivo de alavancar as vendas e o número de pessoas clientes. </br>
    Em um segundo momento, o foco do projeto foi ter o controle do estoque de ingredientes para garantir que o cardápio digital da :baguette_bread: :cook: Pão na Chapa :baguette_bread: :cook: sempre ofereça produtos que estão disponíveis no estoque, evitando frustrações por parte das pessoas clientes. </br>

<br />
</details>

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />

No diretório `src/` você vai encontrar os arquivos implementados, todas as classes e métodos que pude considerar importantes para resolver cada etapa do projeto.

Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

```
.
├── data
│   ├──🔸 orders_1.csv
│   └──🔸 orders_2.csv
├── src
│   ├──🔸 analyze_log.py
│   ├──🔸 inventory_control.py
│   ├──🔸 main.py
│   └──🔸 track_orders.py
├──tests
│   ├──🔸 test_analyze_log.py
│   ├──🔸 test_inventory_control.py
│   └──🔸 test_track_orders.py
├──🔸 dev-requirements.txt
├──🔸 pyproject.toml
├──🔸 README.md
├──🔸 requirements.txt
├──🔸 setup.cfg
├──🔸 setup.py
└──🔸 trybe.yml

Legenda:
🔸 Arquivos já implementados.
```

</details>

<details>
  <summary><strong>🎛 Linter</strong></summary><br />

Para garantir a qualidade do código, utilizei neste projeto o linter `Flake8`.
Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível
e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comandos abaixo:

```bash
python3 -m flake8
```

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

1. **criar o ambiente virtual**

```bash
$ python3 -m venv .venv
```

2. **ativar o ambiente virtual**

```bash
$ source .venv/bin/activate
```

3. **instalar as dependências no ambiente virtual**

```bash
$ python3 -m pip install -r dev-requirements.txt
```

Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
:eyes: Caso precise desativar o ambiente virtual, execute o comando "deactivate".

O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.

</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

<strong>Executar os testes</strong>

```bash
$ python3 -m pytest
```

O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

```bash
python3 -m pytest -s -vv
```

Caso precise executar apenas um arquivo de testes basta executar o comando:

```bash
python3 -m pytest tests/nomedoarquivo.py
```

Caso precise executar apenas uma função de testes basta executar o comando:

```bash
python3 -m pytest -k nome_da_func_de_tests
```

Se desejar rodar os testes de um arquivo específico, execute com `-x nome_do_arquivo`

```bash
pytest -x tests/test_jobs.py
```

Para executar um teste específico de um arquivo, basta executar o comando:

```bash
pytest -x tests/nomedoarquivo.py::test_nome_do_teste
```

Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

</details>

<h1 style="center">Obrigado pela visita ao meu repositório</h1>

## 🔗 Links

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://vinidipaula.vercel.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vinicius-depaula/)
