from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
task_id = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    global task_id
    if request.method == 'POST':
        task_name = request.form['name']
        description = request.form['description']
        due_date = request.form['due_date']
        level = request.form['level']
        tasks.append({"priority_level": level, "id": task_id, "name": task_name, "date": due_date, "description": description, "completion_status": 'not completed'})
        task_id += 1
        return redirect(url_for('view_tasks'))
    return render_template('add_task.html')

@app.route('/view')
def view_tasks():
    return render_template('view_tasks.html', tasks=tasks)

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if request.method == 'POST':
        task['name'] = request.form['name']
        task['description'] = request.form['description']
        task['date'] = request.form['due_date']
        task['priority_level'] = request.form['level']
        return redirect(url_for('view_tasks'))
    return render_template('edit_task.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for('view_tasks'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        task['completion_status'] = 'completed'
    return redirect(url_for('view_tasks'))

if __name__ == '__main__':
    app.run(debug=True)

