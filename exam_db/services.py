import psycopg2
from psycopg2.extensions import (cursor as Cursor, connection as Connection, ISOLATION_LEVEL_AUTOCOMMIT)
from psycopg2 import Error
from typing import Any

from config import (USER, PASSWORD, HOST, PORT)


class Connection:
    def __init__(self) -> None:
        try:
            self.connection = psycopg2.connect(
                user=USER,
                password=PASSWORD,
                host=HOST,
                port=PORT,
            )
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = self.connection.cursor()
            print('соединено')
            cursor.execute('CREATE DATABASE football_matchess;')
            print('создано')
        except (Exception, Error) as e:
            print(f'Error {e}')

    def __new__(cls: type[Any]):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Connection, cls).__new__(cls)

        return cls.instance

    def connect_db(self):
        try:
            self.connection = psycopg2.connect(
                user=USER,
                password=PASSWORD,
                host=HOST,
                port=PORT,
                database='football_matchess',
            )
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            print('соединено')
        except (Exception, Error) as e:
            print(f'Error {e}')

    def create_tables(self):
        with self.connection.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS teams(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(70) UNIQUE
                );

                CREATE TABLE IF NOT EXISTS matches(
                    id SERIAL PRIMARY KEY,
                    rounds VARCHAR(20) NOT NULL,
                    date TIMESTAMP NOT NULL,
                    team_one_id INTEGER REFERENCES teams(id),
                    team_two_id INTEGER REFERENCES teams(id),
                    score VARCHAR(40) NOT NULL DEFAULT('матч еще не начался')
                );
            """)
        self.connection.commit()
        print("таблицы созданы)))")

    def match_info(self):
        data = []
        with self.connection.cursor() as cur:
            cur.execute('SELECT * FROM matches')
            data = cur.fetchall()
        self.connection.commit()
        return data

    def teams(self):
        data = []
        with self.connection.cursor() as cur:
            cur.execute('SELECT * FROM teams')
            data = cur.fetchall()
        self.connection.commit()
        return data

    def info_score(self, score):
        data = []
        with self.connection.cursor() as cur:
            cur.execute(f"SELECT * FROM matches WHERE (score = '{score}')")
            data = cur.fetchall()
        self.connection.commit()
        return data


    def data(self , data) -> None:
        if self.match_info() == []:
            matches = []
            teams = []
            for i in data:
                team1 = i['team1']
                if team1 not in teams:
                    teams.append(team1)

            with self.connection.cursor() as cur:
                cur.execute(f"""
                    INSERT INTO teams (name)
                    VALUES {', '.join(teams)}
                """)
            for i in data:
                game_round = i['round']
                data = i['date']
                team_one_id = teams.index(i['team1'])
                team_two_id = teams.index(i['team2'])
                if len(i)>4:
                    score = i['score']['ft']
                    score = str(score[0], '-', score[1])
                
                score = ''
                matches.append(game_round, data, team_one_id, team_two_id, score)
            with self.connection.cursor() as cur:
                cur.execute(f"""
                    INSERT INTO matches (rounds , date , team_one_id , team_two_id ,score)
                    VALUES {', '.join(matches)}
                """)
        self.connection.commit()
    def close_connection(self) -> None:
        self.connection.close()
        print('и все')
