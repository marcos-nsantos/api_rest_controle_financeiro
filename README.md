# API REST de Controle Financeiro

![Django REST Framework logo](https://www.django-rest-framework.org/img/logo.png)

## Recursos

- Cria, editar, ler e deleta despesas
- Cria, editar, ler e deleta receitas

## Tecnologias

- [Django] - O propósito do Django está no desenvolvimento de aplicações web e sites.
- [Django REST framework] - Desenvolvimento de web API'S de forma simples e ágil.

## Instalação

É necessario o [Python] instalado a partir da versão 3.6.

### Crie um ambiente virtual

#### Se você estiver no Windows
---
Criando ambiente virtual

```sh
py -m venv env
```

Ativando ambiente virtual

```sh
.\env\Scripts\activate
```

#### Se você estiver no macOS ou em uma distribuição Linux
---
Criando ambiente virtual

```sh
python3 -m venv env
```

Ativando ambiente virtual

```sh
source env/bin/activate
```

### Instalando dependências
````sh
pip install -r requirements.txt
````

## Configuração
1. Crie uma cópia do arquivo `example.env` localizado na pasta setup e renomeie para `.env`.
2. No seu terminal com o ambiente virtual ativado, execute o comando `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` para gerar uma chave secreta.
3. Substitua a chave secreta no arquivo `.env` com a chave gerada na variável `SECRET_KEY`.
4. Substitua o endereço do banco de dados no arquivo `.env` com o endereço do banco de dados que você deseja utilizar na variável `DATABASE_URL`.
5. Execute o comando `python manage.py migrate` para criar as tabelas do banco de dados.

## Servidor de desenvolvimento

#### Execute o seguinte comando
---

```sh
python manage.py runserver
```

#### Você verá a seguinte saída
---

```sh
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 21, 2022 - 19:25:00
Django version 3.2.11, using settings 'setup.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

O servidor está rodando, visite http://127.0.0.1:8000/ no seu navegador de internet

[Python]: <https://www.python.org/>

[Django REST framework]: <https://www.django-rest-framework.org/>

[Django]: <https://www.djangoproject.com/>
