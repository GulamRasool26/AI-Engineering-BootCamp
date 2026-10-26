import json
import sqlite3

# Program 01: Cinema Ticket Calculator
age = int(input("Enter age: "))
tickets = int(input("Enter number of tickets: "))
price = 300 if age >= 12 else 180
print("Ticket price: Rs.", price)
print("Total bill: Rs.", price * tickets)

# Program 02: Name Tag Generator
first = input("First name: ").strip()
last = input("Last name: ").strip()
full_name = first.title() + " " + last.title()
initials = first[0].upper() + "." + last[0].upper() + "."
print("Full name:", full_name)
print("Initials:", initials)
print("Letters:", len(first) + len(last))

# Program 03: Five-Day Step Tracker
steps = []
for day in range(5):
    steps.append(int(input(f"Steps on day {day + 1}: ")))
print("Total:", sum(steps))
print("Highest:", max(steps))
print("Average:", sum(steps) / len(steps))
print("Days with 6000+ steps:", len([step for step in steps if step >= 6000]))

# Program 04: Stationery Price Manager
prices = {"pen": 20, "notebook": 150, "eraser": 10}
item = input("Which item to update? ").strip().lower()
if item in prices:
    prices[item] = float(input("New price: "))
else:
    print("Item not found.")
for name, price in prices.items():
    print(name, price)
print("Sum of prices:", sum(prices.values()))

# Program 05: Three-Subject Result Checker
def average_marks(a: int, b: int, c: int) -> float:
    """Return the average of three marks."""
    return (a + b + c) / 3

assert average_marks(60, 70, 80) == 70.0

m1 = int(input("Mark 1: "))
m2 = int(input("Mark 2: "))
m3 = int(input("Mark 3: "))
avg = average_marks(m1, m2, m3)
print("Average:", avg)
print("Result:", "Pass" if avg >= 50 else "Needs improvement")

# Program 06: Visitor Register
name1 = input("First visitor: ")
name2 = input("Second visitor: ")

with open("visitors.txt", "w") as f:
    f.write(name1 + "\n")
with open("visitors.txt", "a") as f:
    f.write(name2 + "\n")
with open("visitors.txt", "r") as f:
    print(f.read())
    
# Program 07: Movie Watchlist with JSON
movies = [
    {"title": "Inception", "watched": True},
    {"title": "The Matrix", "watched": False},
    {"title": "Interstellar", "watched": False},
]
with open("watchlist.json", "w") as f:
    json.dump(movies, f)
with open("watchlist.json", "r") as f:
    loaded = json.load(f)
print("Second movie:", loaded[1]["title"])
print("Not watched:")
for movie in loaded:
    if not movie["watched"]:
        print(movie["title"])

# Program 08: Shared-Bill Calculator
try:
    bill = float(input("Total bill: "))
    friends = int(input("Number of friends: "))
    if friends <= 0:
        print("Number of friends must be at least 1.")
    else:
        print(f"Each person pays: {bill / friends:.2f}")
except ValueError:
    print("Please enter numbers only.")

# Program 09: Parcel Delivery Classes
class Parcel:
    def __init__(self, item, weight):
        self.item = item
        self.weight = weight

    def delivery_fee(self):
        return self.weight * 50

class ExpressParcel(Parcel):
    def delivery_fee(self):
        return self.weight * 80

normal = Parcel("Book", 2)
express = ExpressParcel("Laptop", 2)
print("Normal fee:", normal.delivery_fee())
print("Express fee:", express.delivery_fee())

# Program 10: Book Club Database
conn = sqlite3.connect("book_club.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("INSERT INTO members (name) VALUES (?)", ("Ayesha",))
cur.execute("INSERT INTO members (name) VALUES (?)", ("Bilal",))
conn.commit()
cur.execute("SELECT name FROM members")
rows = cur.fetchall()
for row in rows:
    print(row[0])
assert len(rows) >= 2
conn.close()