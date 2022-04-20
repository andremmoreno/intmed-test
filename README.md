# intmed-test

## Contexto
Implementação de uma interface administrativa na qual gestor da clínica (superusuário) poderá cadastrar um médico e criar a agenda do médico. Utilizando a ferramenta de geração de interface administrativa automática do Django.

## Funcionalidades
1. Admin (superusuário)
- Cadastrar Médicos (com CRMs diferentes)
- Criar agendas dos médicos (uma por dia e sem dias anteriores)

2. Geral
- Lista de consultas marcadas (GET /consultas/)
- Lista de agendas disponíveis (GET /agendas/)
- Marcar consulta (POST /consultas/)
- Desmarcar consulta (DELETE /consultas/)

## Instruções do projeto:

1. Clone o repositório
- `git clone git@github.com:andremmoreno/intmed-test.git`.

2. Entrar na pasta
- `cd intmed-test`

3. Crie o ambiente virtual para o projeto
- `python3 -m venv .venv && source .venv/bin/activate`

4. Instale as dependências
- `python3 -m pip install -r dev-requirements.txt`

4. Inicie o projeto
- `python manage.py runserver` 



