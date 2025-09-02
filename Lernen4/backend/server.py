from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sqlite3
from urllib.parse import parse_qs

# Datenbank erstellen


def init_database():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN DEFAULT FALSE
        )
    ''')
    conn.commit()
    conn.close()


init_database()


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/tasks':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            conn = sqlite3.connect('tasks.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tasks')
            tasks = []
            for row in cursor.fetchall():
                tasks.append(
                    {'id': row[0], 'title': row[1], 'completed': bool(row[2])})
            conn.close()

            self.wfile.write(json.dumps(tasks).encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 - Not Found')

    def do_POST(self):
        if self.path == '/api/tasks':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode())

            conn = sqlite3.connect('tasks.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)',
                           (data['title'], data.get('completed', False)))
            conn.commit()
            task_id = cursor.lastrowid
            conn.close()

            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(
                {'id': task_id, 'title': data['title'], 'completed': False}).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()


def run_server():
    server = HTTPServer(('localhost', 8000), SimpleHandler)
    print('✅ Server läuft auf http://localhost:8000')
    print('✅ GET: http://localhost:8000/api/tasks')
    print('✅ POST: http://localhost:8000/api/tasks')
    print('✅ Datenbank: tasks.db (wird automatisch erstellt)')
    print('Drücke STRG+C zum Stoppen')
    server.serve_forever()


if __name__ == '__main__':
    run_server()
