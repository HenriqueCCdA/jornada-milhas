# Jornada Milhas

[![Python application](https://github.com/HenriqueCCdA/jornada-milhas/actions/workflows/CI.yml/badge.svg)](https://github.com/HenriqueCCdA/jornada-milhas/actions/workflows/CI.yml)
[![codecov](https://codecov.io/gh/HenriqueCCdA/jornada-milhas/branch/main/graph/badge.svg?token=DGE83HA807)](https://codecov.io/gh/HenriqueCCdA/jornada-milhas)

| :placard: Vitrine.Dev |     |
| -------------         | --- |
| :sparkles: Nome       | `Jornada milhas`
| :label: Tecnologias   | `Django Rest Framework`, `Python`, `Postgres`, `Pytest`, `Docker`, `Poetry`, `Ruff`, `codecov`, `swagger`
| :rocket: URL          |


![](doc/assets/swagger.png)

## Instalando as dependencias

```bash
poetry install
```

## Usando o servidor local

Subindo a imagem com o banco de dados

```bash
task docker_db_up
```

Rodando o servidor local

```bash
poetry run python manage.py runserver
```

As variáveis de ambiente de configurações ser encontras no arquivo `.env.sample`

```bash
DEBUG=True
DOC_API=True
SECRET_KEY=Sua_chave_secreta_aqui!
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgres://jornada_milhas:123456@localhost:5432/jornada_milhas
CORS_ALLOWED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
```

## Desenvolvimento

Formatador do codigo com `black` e `ruff`:

```bash
task fmt
```

Linter com `ruff`

```bash
task linter
```

Rodando testes

```bash
task test
```
