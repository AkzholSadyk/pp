import psycopg2

name = input("Name plaese: ")
phone_number = input("Phone number please: ")
 
conn = psycopg2.connect(host="localhost", dbname="students", user="postgres",
                        password="Akjol006", port=5432)   
 
cur = conn.cursor()
 
conn.set_session(autocommit=True)

# cur.execute('DROP TABLE contacts3 ;')

# conn.commit()

cur.execute("""
    CREATE TABLE if not exists dorm (
    name VARCHAR(255),
    phone_number VARCHAR(30) PRIMARY KEY
    );
""")

cur.execute(f"""
    INSERT INTO dorm (name, phone_number) VALUES ('{name}','{phone_number}')
""")

conn.commit()