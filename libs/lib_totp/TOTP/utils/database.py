import mysql.connector
from mysql.connector import errorcode
from .user import User
from typing import Sequence, Dict, Optional
import os

class Database:

    def __init__(self):
        self.connection = mysql.connector.connect(user='root', password='secret',host='127.0.0.1', database='test')
        self.cursor = self.connection.cursor()

        self.queries: Dict[str, str] = dict()
        queries_path = "sql_queries"
        queries = os.listdir(os.path.join("utils", queries_path))
        for query in queries:
            if query.endswith(".sql"):
                with open(os.path.join("utils", queries_path, query)) as f:
                    fileWithoutExt = os.path.splitext(query)[0]
                    self.queries[fileWithoutExt] = f.read()

    def reset(self):
        self.cursor.execute("DROP TABLE IF EXISTS users")
        self.cursor.execute(self.queries["table_users"])

    def close(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def addUser(self, user: User) -> bool:
        sql = self.queries.get("add_user", None)
        # assert sql is None, "Couldn't load add_user query"

        values = (user.email, user.name, user.surname, user.city, user.dateOfBitrh, user.income, user.secretKey)
        try:
            self.cursor.execute(sql, values)
        except mysql.connector.errors.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("User exists")
            return False

        return True

    def addUsers(self, users: Sequence[User]) -> bool:
        sql = self.queries.get("add_user", None)
        # assert sql is None, "Couldn't load add_user query"
        try:
            self.cursor.executemany(sql, [(user.name, user.password, user.secretKey) for user in users])
        except:
            return False
        
        return True

    def getUser(self, email: str) -> Optional[User]:
        sql = self.queries.get("get_user", None)
        # assert sql is None, "Couldn't load get_user query"

        values = (email, )
        
        try:
            self.cursor.execute(sql, values)
        except:
            return None

        return User(*self.cursor.fetchone())

    def getUsers(self) -> Optional[Sequence[User]]:
        sql = self.queries.get("get_users", None)
        # assert sql is not None, "Couldn't load get_users query"

        try:
            self.cursor.execute(sql)
        except:
            return None

        return [User(*user) for user in self.cursor.fetchall()]
    

db = Database()



db.close()


