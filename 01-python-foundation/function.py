# Function
def greet():
    print("Hello")
greet()

def greeting(name):
    print(f"Hello, {name}")
greeting("Dhanush")

# Default parameters
def search_document(query, limit=5):
    print(f"Searching for {query} with limit {limit}")
search_document("motor")
search_document("motor", 10)

# Keyword Arguments
def task(title, priority):
    print(title, priority)
task(priority="high", title="Replace")

# Exercise 1
def calculate_square(num):
    return num * num
result = calculate_square(7)
print(result)

# Exercise 2
def calculate_total(price, quantity):
    return price * quantity
total = calculate_total(250, 3)
print(total)

# Exercise 3
def is_relevant(score, threshold):
    return score >= threshold
print(is_relevant(0.87, 0.8))

# Exercise 4
def get_equipment(page, limit=10):
    return f"Fetching page {page} with limit {limit}"
print(get_equipment(2))
print(get_equipment(3, 25))

# Exercise 5
def create_task(title, priority="medium"):
    return f"Title: {title} - Priority: {priority}"
print(create_task("Inspect motor"))
print(create_task("Replace motor", "high"))

# Exercise 6
def connect(port, host="localhost"):
    print(host, port)
connect(3000)

# Exercise 7
def fetch_equipment(page, limit=10, status="active"):
    return f"{page} {limit} {status}"
print(fetch_equipment(status="maintenance", page=2, limit=20))

# Exercise 8
def retrieve_documents(query, top_k=5, threshold=0.7):
    return f"{query} {top_k} {threshold}"
print(retrieve_documents("Motor", top_k=10))

# Exercise 9
def create_task(title, priority="medium", assigned_to="unassigned"):
    return f"{title} {priority} {assigned_to}"
print(create_task("Inspect pump", "medium", "Dhanush"))
print(create_task(assigned_to="Dhanush", title="Inspect pump", priority="high"))


# *args - The * means collect all remaining positional arguments into a tuple.
def process(*args):
    print(type(args))
    print(args)
process("Motor", "Pump", "Generator")

def log_event(event_type, *messages):
    for message in messages:
        print(f"[{event_type}] {message}")
log_event("ERROR", "Database failed", "Retrying connection")

# *args with normal parameters
def process_equipment(category, *equipment):
    print(f"Category: {category}")

    for item in equipment:
        print(f"Processing {item}")
process_equipment("Critical", "Motor", "Pump", "Compressor")

# Exercise 1
def process_equipment(*equipment):
    for equip in equipment:
        print(f"Processing {equip}")
process_equipment("Motor", "Pump", "Compressor")

# Exercise 2
def calculate_total(*prices):
    total = 0
    for price in prices:
        total += price
    print(total)
calculate_total(10, 20)

# Exercise 3
def build_context(*documents):
    return "\n".join(documents) #\n is new line character in python
context = build_context("Motor maintenance guide", "Pump inspection guide", "Compressor safety guide")
print(context)

# Exercise 4
def log_messages(level, *messages):
    for message in messages:
        print(f"[{level}] {message}")
log_messages("ERROR", "Database connection failed", "Retrying connection", "Connection restored")


# **kwargs is keyword arguments. It becomes dictionary
def create_equipment(**kwargs):
    print(kwargs)
create_equipment(name="Motor", status="active", location="Plant A")

def show_equipment(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
show_equipment(name="Motor", status="active", location="Plant A")

# Exercise 1
def equipment_detail(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
equipment_detail(name="Motor", status="active", location="Plant A", department="Production")

# Exercise 2
def configure_model(**config):
    for key, value in config.items():
        print(f"{key}: {value}")
configure_model(model="gpt", temperature=0.2, max_tokens=500)

# Exercise 3
def create_user(username, **details):
    print(f"Username: {username}")

    for key, value in details.items():
        print(f"{key}: {value}")
create_user("Dhanush", role="developer", experience=2, location="Trichy")

# All in one example
def example(name, *args, **kwargs):
    print(f"Username: {name}")
    print(f"Skills {args}")
    print(f"experience {kwargs}")
example("Dhanush", "React", "Python", role="Developer", experience=2)