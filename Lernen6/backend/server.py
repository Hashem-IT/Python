from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sqlite3

DB_FILE = 'tasks.db'


def init_database():
    conn = sqlite3.connect(DB_FILE)
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
    def _send_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._send_headers()

    def do_GET(self):
        if self.path == '/api/tasks':
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tasks')
            tasks = [{'id': row[0], 'title': row[1], 'completed': bool(
                row[2])} for row in cursor.fetchall()]
            conn.close()
            self._send_headers()
            self.wfile.write(json.dumps(tasks).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 - Not Found')

    def do_POST(self):
        if self.path == '/api/tasks':
            length = int(self.headers['Content-Length'])
            data = json.loads(self.rfile.read(length).decode())
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)',
                           (data['title'], data.get('completed', False)))
            conn.commit()
            task_id = cursor.lastrowid
            conn.close()
            self._send_headers(201)
            self.wfile.write(json.dumps(
                {'id': task_id, 'title': data['title'], 'completed': False}).encode())

    def do_PUT(self):
        if self.path.startswith('/api/tasks/'):
            task_id = int(self.path.split('/')[-1])
            length = int(self.headers['Content-Length'])
            data = json.loads(self.rfile.read(length).decode())
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute('UPDATE tasks SET completed=? WHERE id=?',
                           (data['completed'], task_id))
            conn.commit()
            conn.close()
            self._send_headers()
            self.wfile.write(json.dumps(
                {'id': task_id, 'completed': data['completed']}).encode())

    def do_DELETE(self):
        if self.path.startswith('/api/tasks/'):
            task_id = int(self.path.split('/')[-1])
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))
            conn.commit()
            conn.close()
            self._send_headers()
            self.wfile.write(json.dumps({'message': 'Deleted'}).encode())


def run_server():
    server = HTTPServer(('localhost', 8000), SimpleHandler)
    print('✅ Backend läuft auf http://localhost:8000')
    server.serve_forever()


if __name__ == '__main__':
    run_server()
