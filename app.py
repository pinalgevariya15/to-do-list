from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Now storing dictionaries: {'task': 'Text', 'completed': False}
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task_text = request.form.get('todo')
    if task_text:
        todos.append({'task': task_text, 'completed': False})
    return redirect(url_for('index'))

@app.route('/toggle/<int:index>')
def toggle(index):
    if 0 <= index < len(todos):
        todos[index]['completed'] = not todos[index]['completed']
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['POST'])
def edit(index):
    new_task = request.form.get('new_task')
    if 0 <= index < len(todos) and new_task:
        todos[index]['task'] = new_task
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)