from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

ADMIN_PASSWORD = 'admin123'

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        password = request.form.get('password')
        if password == ADMIN_PASSWORD:
            return redirect(url_for('admin_dashboard'))
        else:
            error = "Incorrect Password"
    return render_template('admin_login.html', error=error)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        file = request.files.get('file')
        copies = request.form.get('copies')
        page_range = request.form.get('page_range')
        custom_range = request.form.get('custom_range') if page_range == 'custom' else None
        colour = request.form.get('colour')
        print_type = request.form.get('print_type')
        message = request.form.get('message')

        # Do whatever you want with the form data
        return "Form submitted!"  # You can redirect or show total cost here

    return render_template('order.html')









if __name__ == '__main__': 
    app.run(debug=True,host='0.0.0.0') 
# host='0.0.0.0'