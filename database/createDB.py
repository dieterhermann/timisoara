import sqlite3


def create_db():
    conn = sqlite3.connect('vremea.sqlite')
    db = conn.cursor()

    db.execute('''DROP TABLE IF EXISTS WETTER''')
    db.execute('''DROP TABLE IF EXISTS SOLAR''')

    db.execute('''CREATE TABLE IF NOT EXISTS WETTER
                         (ID INT PRIMARY KEY    NOT NULL,
                         DATUM           TEXT   NOT NULL,
                         TEMPERATUR      INT    NOT NULL,
                         MAXTEMP         INT    NOT NULL,
                         MINTEMP         INT    NOT NULL,
                         HUMIDITY        INT    NOT NULL,
                         WIND            TEXT   NOT NULL);''')

    db.execute('''CREATE TABLE IF NOT EXISTS SOLAR
                             (ID INT PRIMARY   KEY  NOT NULL,
                             DATUM             TEXT NOT NULL,
                             SPANNUNG          REAL NOT NULL,
                             STROM             REAL NOT NULL,
                             WATS              REAL NOT NULL);''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_db()