import sqlite3
# Insert car (and enigne if needed) data into the car table 
def add():
        conn = sqlite3.connect('cars.db')
        c = conn.cursor()
        print("select make acquardingly")
        c.execute("SELECT * FROM make")
        for row in c.fetchall():
             print(row)
        make = input("Make: ")
        model = input("Model: ")
        while True:
            print("Is Your Engine On The Below List")
            c.execute("SELECT * FROM engine")
            for row in c.fetchall():
                 print(row)
            answer = input("(y) or (n)")
            if answer == "y":
                 engine = input("Engine: ")
                 break
            if answer == "n":
                name = input("name")
                c.execute("INSERT INTO engine (engine_name ) VALUES (?)", (name,))

        stockhp = input("Stock Horse Power: ")
        stocktorque = input("Stock Torque: ")
        image = input("Image(leave null):")
        print("select drive acquardingly")
        c.execute("SELECT * FROM drive")
        for row in c.fetchall():
             print(row)
        drive = input(":")
        c.execute("INSERT INTO car (make, model, engine, stockhp, stocktorque, image, drive) VALUES (?, ?, ?, ?, ?, ?, ?)", (make, model, engine, stockhp, stocktorque, image, drive))
        conn.commit()
        conn.close()

# Insert engine data into the car table 
def add_engine():
        conn = sqlite3.connect('cars.db')
        c = conn.cursor()
        name = input("name")
        c.execute("INSERT INTO engine (engine_name ) VALUES (?)", (name,))
        conn.close()

# Commit changes
def save_changes():
        conn = sqlite3.connect('cars.db')
        c = conn.cursor()
        conn.commit()
        print("saved")
        conn.close()
        
# Fetch and print car table
def veiw_cars():
        conn = sqlite3.connect('cars.db')
        c = conn.cursor()
        c.execute("select make.whatmake, car.model, car.engine, car.stockhp, car.stocktorque from car join make on car.make = make.id")
        print("All car:")
        for row in c.fetchall():
            print(row)
        conn.close()

# Fetch and print all engines
def veiw_engines():
        conn = sqlite3.connect('cars.db')
        c = conn.cursor()
        c.execute("SELECT * FROM engine")
        print("All engines:")
        for row in c.fetchall():
            print(row)
        conn.close()

# Delete data from the table
def delete():
        conn = sqlite3.connect('cars.db')
        c = conn.cursor()
        table = input("what would you like to delete (car=1) (engine=2)")
        if table == "1":
            c.execute("SELECT * FROM car")
            for row in c.fetchall():
                print(row)
            what = input()
            c.execute("DELETE FROM car WHERE car_id = ?", (what,))
            conn.commit()
            conn.close()
        if table == "2":
            c.execute("SELECT * FROM engine")
            for row in c.fetchall():
                print(row)
            what = input()
            c.execute("DELETE FROM engine WHERE engine_id = ?", (what,))
            conn.commit()
            conn.close()

def test():
      print("hello")
