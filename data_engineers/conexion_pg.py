# Configura tus credenciales de la base de datos
database_config = {
    'username': 'base_qa6d_user',
    'password': 'HSqnH1m5ipLbeTkaDUKPTciAbSztBwh0',
    'host': 'dpg-cn5pn90l5elc73e8k72g-a.oregon-postgres.render.com',
    'port': '5432',
    'database': 'base_qa6d'
}

# Construye la URL de conexión
db_url = f'postgresql+psycopg2://{database_config["username"]}:{database_config["password"]}@{database_config["host"]}:{database_config["port"]}/{database_config["database"]}'