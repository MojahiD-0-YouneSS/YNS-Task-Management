from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class TaskList:
    def __init__(self):
        self.tasks = []
        self.task_id = 1

    def add_task(self, task_name, description, due_date, level):
        self.tasks.append({
            "priority level": level,
            "id": self.task_id,
            "name": task_name,
            "Date": due_date,
            "description": description,
            "completion status": 'not completed'
        })
        self.task_id += 1

    def mark_task_as_complete(self, task_id):
        for task in self.tasks:
            if task["id"] == int(task_id):
                task["completion status"] = 'completed'
                return True
        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == int(task_id):
                self.tasks.remove(task)
                return True
        return False

    def edit_task(self, task_id, task_name, description, due_date, level):
        for task in self.tasks:
            if task["id"] == int(task_id):
                task["name"] = task_name
                task["description"] = description
                task["Date"] = due_date
                task["priority level"] = level
                return True
        return False

task_list = TaskList()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view_tasks')
def view_tasks():
    return render_template('view_tasks.html', tasks=task_list.tasks)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        description = request.form['description']
        due_date = request.form['due_date']
        level = request.form['level']
        task_list.add_task(task_name, description, due_date, level)
        return redirect(url_for('view_tasks'))
    return render_template('add_task.html')

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    task_list.mark_task_as_complete(task_id)
    return redirect(url_for('view_tasks'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    task_list.delete_task(task_id)
    return redirect(url_for('view_tasks'))

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = next((task for task in task_list.tasks if task["id"] == task_id), None)
    if request.method == 'POST':
        task_name = request.form['task_name']
        description = request.form['description']
        due_date = request.form['due_date']
        level = request.form['level']
        task_list.edit_task(task_id, task_name, description, due_date, level)
        return redirect(url_for('view_tasks'))
    return render_template('edit_task.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)

