import sqlite3

class TicketManager:
    def __init__(self):
        self.conn = sqlite3.connect('tickets.db')
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS tickets (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    project_type TEXT NOT NULL,
                    description TEXT NOT NULL,
                    priority TEXT NOT NULL,
                    status TEXT NOT NULL
                )
            ''')

    def create_ticket(self, title, project_type, description, priority, status):
        with self.conn:
            self.conn.execute('''
                INSERT INTO tickets (title, project_type, description, priority, status)
                VALUES (?, ?, ?, ?, ?)
            ''', (title, project_type, description, priority, status))

    def update_ticket(self, ticket_id, title, project_type, description, priority, status):
        with self.conn:
            self.conn.execute('''
                UPDATE tickets
                SET title = ?, project_type = ?, description = ?, priority = ?, status = ?
                WHERE id = ?
            ''', (title, project_type, description, priority, status, ticket_id))

    def fetch_tickets(self):
        with self.conn:
            cursor = self.conn.execute('SELECT * FROM tickets')
            return cursor.fetchall()
