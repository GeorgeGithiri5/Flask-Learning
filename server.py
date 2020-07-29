from flask import Flask,render_template,url_for,flash,redirect
from form import RegistrationForm,LoginForm

posts = [
    {
        'author':'George Post',
        'title': 'The growth of random trees Algorithms',
        'content': 'First Post content',
        'date_posted':'April 20,2018'
    },
    {
        'author':'Post On TensorFlow',
        'title': 'The growth of neural networks',
        'content': 'second Post content',
        'date_posted':'April 20,2018'
    }
]

app = Flask(__name__)

app.config['SECRET_KEY'] = '6f82a2d15dc30bd5462f2ebf526e765e'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data=='password':
            flash('You have been logged In','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html',title='login',form=form)


if __name__ == "__main__":
    app.run(debug=True)