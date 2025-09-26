import pymysql as connector
db = connector.connect(host = 'localhost',user = 'root',password = 'password',database = 'chemwallah')
c = db.cursor()
c.executemany('''CREATE TABLE pr101 (
            id SERIAL PRIMARY KEY,
            user VARCHAR(255),
            phone VARCHAR(20)
            );
CREATE TABLE pr101_2 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);
CREATE TABLE pr101_offline (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);
CREATE TABLE ar101 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE ar101_2 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE ar101_offline (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE aj101 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE aj101_2 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE aj101_offline (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE an101 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE an101_2 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE an101_offline (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE lj101 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE lj101_2 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE lj101_offline (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE ln101 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE ln101_2 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE ln101_offline (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE mj101 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE mj101_2 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE mj101_offline (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE mn101 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE mn101_2 (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE mn101_offline (
    id SERIAL PRIMARY KEY,
    user VARCHAR(255),
    phone VARCHAR(20)
);
''')
db.commit()
c.execute('Create table record(user varchar(20) primary key, name varchar(20), phone varchar(10), guardians varchar(20), course varchar(20), batch varchar(30), class int, subjects char(3)')
db.commit()
c.execute("Create table users(user varchar(20), password varchar(20))")
db.commit()
c.execute('Create table feedback(user varchar(20), feedback varchar(10000)')
db.commit()