import mysql.connector


# Insert event data into the database
def insert_event(connection, event_name, event_date, location_id, total_tickets, description):
    cursor = connection.cursor()
    query = "INSERT INTO events (event_name, event_date, location_id, total_tickets, description) VALUES (%s, %s, %s, %s, %s)"
    data = (event_name, event_date, location_id, total_tickets, description)
    cursor.execute(query, data)
    connection.commit()
    print("Event inserted successfully!")

# Insert attendee data into the database
def insert_attendee(connection, name, email, phone_number):
    cursor = connection.cursor()
    query = "INSERT INTO attendees (name, email, phone_number) VALUES (%s, %s, %s)"
    data = (name, email, phone_number)
    cursor.execute(query, data)
    connection.commit()
    print("Attendee inserted successfully!")

# Insert ticket data into the database
def insert_ticket(connection, event_id, attendee_id, ticket_status):
    cursor = connection.cursor()
    query = "INSERT INTO tickets (event_id, attendee_id, status) VALUES (%s, %s, %s)"
    data = (event_id, attendee_id, ticket_status)
    cursor.execute(query, data)
    connection.commit()
    print("Ticket inserted successfully!")

# Insert payment data into the database
def insert_payment(connection, ticket_id, payment_amount):
    cursor = connection.cursor()
    query = "INSERT INTO payments (ticket_id, payment_amount) VALUES (%s, %s)"
    data = (ticket_id, payment_amount)
    cursor.execute(query, data)
    connection.commit()
    print("Payment inserted successfully!")

# Get all events (for display or further operations)
def get_all_events(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM events"
    cursor.execute(query)
    events = cursor.fetchall()
    return events

# Fetch all events from the database
def get_all_events(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM events"
    cursor.execute(query)
    events = cursor.fetchall()
    return events

# Fetch all payments from the database
def get_all_payments(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM payments"
    cursor.execute(query)
    payments = cursor.fetchall()
    return payments
