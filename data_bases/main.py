import sqlite3

with sqlite3.connect("yandex.db") as connection:
    cursor = connection.cursor()

    create_countries = """
        CREATE TABLE IF NOT EXISTS Countries(
        ID integer PRIMARY KEY AUTOINCREMENT,
        name varchar(40) NOT NULL,
        population integer default NULL,
        gdp integer default NULL
        )
        """

    insert_countries = """
        INSERT INTO Countries(name,population,gdp) VALUES 
        ("Россия",14600000,555999444000),
        ("Беларусь",9300000,333444555),
        ("Великобритания",67000000,999888777666)
        """
    # ALTER TABLE Cities (ADD/RENAME/RENAME TO)
    # ADD some_column varchar(100)
    # DROP COLUMN some_column
    # DROP TABLE table_name
    create_cities = """
    CREATE TABLE IF NOT EXISTS Cities(
    ID integer PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(40) NOT NULL,
    population INTEGER DEFAULT NULL,
    founded INTEGER DEFAULT NULL,
    country_id INTEGER,
    FOREIGN KEY(country_id) REFERENCES Countries(ID) ON DELETE RESTRICT ON UPDATE CASCADE 
    );
    """

    insert_cities = """
    INSERT INTO Cities(name, population, founded, country_id) VALUES
    ("Москва",8000000,1110,1),
    ("Минск",3000000,1344,2),
    ("Могилев",400000,1868,2), 
    ("Лондон",7000000,820,3),
    ("Краснодар",1500000,1793,1),
    ("Ливерпуль",1000000,1504,3),
    ("Воронеж",900100,1840,1),
    ("Саратов",560000,1744,1);
    """

    create_companies = """
    CREATE TABLE IF NOT EXISTS Companies(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(40) NOT NULL,
    city_id INTEGER,
    revenue INTEGER NOT NULL,
    labors INTEGER NOT NULL,
    FOREIGN KEY(city_id) REFERENCES Cities(ID)
    );
    """
    insert_companies = """
    INSERT INTO Companies(name,city_id,revenue,labors) VALUES 
    ("Yandex",1,9998880,6600),
    ("Megafon",4,1230000,1001),
    ("Wargaming",2,4445550,2000),
    ("Facebook",5,123000,300),
    ("Beeline",1,9274000,5500),
    ("Mts",4,322000,400),
    ("PayPal",3,62400600,9800)
    """

    # SELECT * FROM Cities LIMIT 10
    # SELECT * FROM Cities LIMIT 10 OFFSET 10
    # SELECT * FROM COMPANIES WHERE name IN ('Yandex','Mts')
    # SELECT * FROM Companies WHERE name LIKE 'M%'
    # SELECT * FROM Companies WHERE labors BETWEEN 2000 AND 6000
    # SELECT * FROM Cities WHERE population IS NOT NULL
    # SELECT * FROM Cities ORDER BY founded DESC
    # SELECT * FROM Companies GROUP BY city_id,name
    # SELECT COUNT(DISTINCT name),city_id FROM Companies GROUP BY city_id  подсчет кол-ва компаний в каждом городе
    # SELECT MIN(labors),MAX(labors) from Companies
    # SELECT AVG(Revenue),AVG(labors) FROM Companies GROUP BY city_id Среднее кол-во работников в каждом из городов
    query = """
    SELECT Countries.name,COUNT(Companies.name)
    FROM Cities
    LEFT JOIN Countries ON Cities.country_id = Countries.ID
    LEFT JOIN Companies ON Cities.id = Companies.city_id
    WHERE Companies.labors>=1000
    GROUP BY Countries.name
    """

    # cursor.execute(create_countries)
    # cursor.execute(insert_countries)
    # cursor.execute(create_cities)
    # cursor.execute(insert_cities)
    # cursor.execute(create_companies)
    # cursor.execute(insert_companies)
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
