
class DB:
    def __init__(self):
        host = 
        user = 
        passwd =
        database = 
        self.conn = mysql.connector.connect(host=host,user=user,passwd=passwd,database=database,auth_plugin='mysql_native_password')
        self.cursor = self.conn.cursor()

    def __del__(self): #destructor
        self.conn.close()

    def close(self):
        self.cursor.close()
        self.conn.close()
        
    # Seach database
    def search(self,*args):
        self.cursor.execute(' '.join(args))
        rows = self.cursor.fetchall()
        return rows

    # Insert database
    def insert(self,*args):
        self.cursor.execute(' '.join(args))
        self.conn.commit()

    # Update database
    def update(self,*args):
        self.cursor.execute(' '.join(args))
        self.conn.commit()

    # Delete from database
    def delete(self,*args):
        self.cursor.execute(' '.join(args))
        self.conn.commit()
