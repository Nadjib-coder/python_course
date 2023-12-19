from sqlalchemy import create_engine, Metadata, Tabel

host = "localhost"
user = "user_name"
password = "user_password"
database = "db_name"

engine = create_engine(f"mysql://{user}:{password}@{host}/{database}", echo=True)

connection = engine.connect()

metadata = Metadata()

our_tabel = Tbale('table_name', metadata, autoload_with=engine)

query = our_tabel.select()

result = connection.excute(query)

for row in result:
    print(row)

connection.close()