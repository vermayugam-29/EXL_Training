from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', METHOD=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']
        salary = request.form['salary']

        # Print employee data to console
        print(name)
        print(department)
        print(salary)

        return f"Name = {name}, Department = {department}, Salary = {salary}"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
