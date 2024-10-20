import sqlite3


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