from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World Manoel Fangmo! I am adding my first code change'

@app.route('/hello')
def hello():
    return render_template('hello.html');

@app.route('/about')
def about():
    return render_template('about.html');

@app.route('/favorite-Course')
def favoriteCourse():
    text = str(request.args.get('schoolName')) + " " + str(request.args.get('courseNumber'));
    return render_template('favorite-course.html',courses=text);

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True);
    else:
        return render_template('contact.html');

if __name__ == '__main__':
    app.run()
