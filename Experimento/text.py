import sqlite3

class TaskManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_tenants_table()

    def create_tenants_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tenants (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL UNIQUE
                        )''')
        self.conn.commit()

    def create_tenant_schema(self, tenant_name):
        cursor = self.conn.cursor()
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {tenant_name}_tasks (id INTEGER PRIMARY KEY, task TEXT NOT NULL)')
        self.conn.commit()

    def add_task(self, tenant_name, task):
        cursor = self.conn.cursor()
        cursor.execute(f'INSERT INTO {tenant_name}_tasks (task) VALUES (?)', (task,))
        self.conn.commit()

    def get_tasks(self, tenant_name):
        cursor = self.conn.cursor()
        cursor.execute(f'SELECT * FROM {tenant_name}_tasks')
        tasks = cursor.fetchall()
        return tasks

# Exemplo de uso
task_manager = TaskManager("task_manager.db")
task_manager.create_tenant_schema("tenant1")
task_manager.create_tenant_schema("tenant2")

task_manager.add_task("tenant1", "Lavar a louça")
task_manager.add_task("tenant2", "Passear com o cachorro")

print(task_manager.get_tasks("tenant1"))
print(task_manager.get_tasks("tenant2"))
