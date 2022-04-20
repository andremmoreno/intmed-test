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
