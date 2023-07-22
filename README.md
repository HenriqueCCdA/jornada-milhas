# Jornada Milhas
[![Python application](https://github.com/HenriqueCCdA/jornada-milhas/actions/workflows/CI.yml/badge.svg)](https://github.com/HenriqueCCdA/jornada-milhas/actions/workflows/CI.yml)
[![codecov](https://codecov.io/gh/HenriqueCCdA/jornada-milhas/branch/main/graph/badge.svg?token=DGE83HA807)](https://codecov.io/gh/HenriqueCCdA/jornada-milhas)

| :placard: Vitrine.Dev |     |
| -------------         | --- |
| :sparkles: Nome       | `Jornada milhas`
| :label: Tecnologias   | `Django Rest Framework`, `Python`, `Postgres`, `Pytest`, `Docker`, `Poetry`, `Ruff`, 'codecov', 'swagger'
| :rocket: URL          |


## Instalando as dependencias.

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
