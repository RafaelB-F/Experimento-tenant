# Experimento-tenant

A estratégia de Schema-Based Multi Tenancy é uma abordagem eficaz para isolar os dados de diferentes inquilinos em um sistema. Neste exemplo simples, cada inquilino possui seu próprio esquema no banco de dados SQLite, garantindo que suas tarefas sejam armazenadas de forma isolada. Isso permite escalabilidade, segurança e eficiência no acesso aos dados.



Classe TaskManager:

Esta classe é responsável por gerenciar as tarefas e a interação com o banco de dados.

No método __init__, estabelecemos uma conexão com o banco de dados SQLite e chamamos o método create_tenants_table para criar a tabela de inquilinos (tenants) se ela não existir.

O método create_tenant_schema é utilizado para criar um novo esquema (tabela) para um inquilino específico.

add_task adiciona uma nova tarefa para um inquilino especificado.

get_tasks retorna todas as tarefas de um inquilino.





Implementação do Banco de Dados:

Utilizamos SQLite para simplicidade. Cada inquilino terá uma tabela própria, nomeada de acordo com seu nome (por exemplo, "tenant1_tasks", "tenant2_tasks").




Exemplo de Uso:

Criamos uma instância de TaskManager e chamamos create_tenant_schema para criar esquemas para dois inquilinos diferentes: "tenant1" e "tenant2".

Em seguida, adicionamos algumas tarefas para cada inquilino usando add_task.

Finalmente, usamos get_tasks para recuperar as tarefas de cada inquilino e imprimi-las.

