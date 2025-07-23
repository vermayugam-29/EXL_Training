from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        course = request.form['course']
        feedback = request.form['feedback']

        print(f'Name : {name}')
        print(f'Course : {course}')
        print(f'Feedback : {feedback}')

        return f"Thank you, {name}. Your feedback for the course {course} has been received: {feedback}."
    return render_template('feedback_form.html')

if __name__ == '__main__':
    app.run(debug=True)