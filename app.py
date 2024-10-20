from flask import Flask, render_template, request, redirect
import sqlite3
import os

# Define admin username and password
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'

app = Flask(__name__)
UPLOAD_FOLDER = 'static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# This is the route to the home page/landing page
@app.route('/')
def landing_page():
    '''this shows the landing page'''
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM car')
    results = cur.fetchall()
    print(results)
    return render_template("landing_page.html", title="home", results=results)

# renders cars
@app.route('/car/<int:car_id>')
def car_info(car_id):
    '''this makes the car info display'''
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute(
        'SELECT car.make, car.model, car.engine, car.stockhp, car.stocktorque, '
        'make.whatmake, engine.engine_name, car.image, car.drive, car.image_, car.vidlink '
        'FROM car JOIN make ON car.make = make.make_id JOIN engine ON car.engine = engine.engine_id '
        'WHERE car_id=?',
        (car_id,)
    )
    results = cur.fetchall()
    print(results)
    return render_template("carinfo.html", title="car", results=results)

# Renders make table
@app.route('/make')
def make():
    '''returns and renders make html'''
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM make')
    results = cur.fetchall()
    print(results)
    return render_template('make.html', title="make", results=results)

# renders all makes
@app.route('/make/<int:make_id>')
def makes(make_id):
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM car WHERE make=?', (make_id,))
    results = cur.fetchall()
    print(results)
    return render_template("makes.html", title="makes", results=results)

# Renders admin table
@app.route('/admin')
def admin():
    '''this shows the admin password page'''
    return render_template('adminpasswall.html')

# shows the add car page
@app.route('/add')
def add():
    '''shows the page that adds cars'''
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM make')
    makes = cur.fetchall()
    print(makes)
    cur.execute('SELECT * FROM drive')
    drive = cur.fetchall()
    print(drive)
    cur.execute('SELECT * FROM engine')
    engine = cur.fetchall()
    print(engine)

    return render_template('add.html', makes=makes, drive=drive, engine=engine)

# Renders make table
@app.route('/process', methods=['POST'])
def process():
    '''retrurns the form to py'''
    make = request.form['Make']
    model = request.form['Model']
    engine = request.form['Engine']
    stock_hp = request.form['Stock HP']
    stock_torque = request.form['Stock Torque']
    image = request.form['Image']
    image_ii = request.form['Imageii']
    video = request.form['Video']
    drive = request.form['Drive']

    # Handle file upload
    if 'car_image' not in request.files:
        return "No file part"
    
    file = request.files['car_image']
    if file.filename == '':
        return "No selected file"
    
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        print(f"Image saved at {file_path}")

    # Handle second file upload
    if 'car_image2' not in request.files:
        return "No file part"
    
    file = request.files['car_image2']
    if file.filename == '':
        return "No selected file"
    
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        print(f"Image saved at {file_path}")

    # Save form data and file path to the database
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO car (make, model, engine, stockhp, stocktorque, image, image_, vidlink, drive) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (make, model, engine, stock_hp, stock_torque, image, image_ii, video, drive)
    )
    conn.commit()
    conn.close()

    return render_template("makes.html", title="makes")

# Pulls up engine table
@app.route('/engine')
def engine_view():
    '''shows all engines'''
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM engine')
    results = cur.fetchall()
    print(results)
    return render_template("engine.html", title="engine", results=results)

# creates a login request
@app.route("/login", methods=["GET", "POST"])
def login():
    """Login route"""
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Print for debugging purposes
    print(f"Submitted Username: {username}, Submitted Password: {password}")
    print(f"Expected Username: {ADMIN_USERNAME}, Expected Password: {ADMIN_PASSWORD}")

    if username and password:  # Ensure that both are not None or empty
        if username.strip() == ADMIN_USERNAME and password.strip() == ADMIN_PASSWORD:
            print("Login successful")
            return redirect("/add")
        else:
            print("Login failed")
            return redirect("/admin")
    else:
        print("Empty username or password")
        return redirect("/admin")

if __name__ == "__main__":
    app.run(debug=True)