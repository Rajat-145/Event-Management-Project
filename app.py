from flask import Flask, render_template, request, redirect, url_for
from db_connection import create_connection
from crud_operations import insert_event, insert_attendee, insert_ticket, insert_payment, get_all_events, get_all_payments

app = Flask(__name__)

# Route for the homepage (Dashboard)
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Route for the registration form
@app.route('/register_event', methods=['GET', 'POST'])
def register_event():
    if request.method == 'POST':
        # Get form data from the HTML form
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        location_id = request.form['location_id']
        total_tickets = request.form['total_tickets']
        description = request.form['description']
        
        # Create connection and insert event data into the database
        connection = create_connection()
        if connection:
            insert_event(connection, event_name, event_date, location_id, total_tickets, description)
            connection.close()  # Close the connection after the operation is done
            return redirect(url_for('success'))  # Redirect to a success page or show a message
        else:
            return "Error connecting to the database"
    return render_template('register_event.html')

# Route for registering attendees
@app.route('/register_attendee', methods=['GET', 'POST'])
def register_attendee():
    if request.method == 'POST':
        # Get form data from the HTML form
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        
        # Create connection and insert attendee data into the database
        connection = create_connection()
        if connection:
            insert_attendee(connection, name, email, phone_number)
            connection.close()
            return redirect(url_for('success'))  # Redirect to success page
        else:
            return "Error connecting to the database"
    return render_template('register_attendee.html')

# Route for ticket management
@app.route('/register_ticket', methods=['GET', 'POST'])
def register_ticket():
    if request.method == 'POST':
        # Get form data from the HTML form
        event_id = request.form['event_id']
        attendee_id = request.form['attendee_id']
        ticket_status = request.form['ticket_status']
        
        # Create connection and insert ticket data into the database
        connection = create_connection()
        if connection:
            insert_ticket(connection, event_id, attendee_id, ticket_status)
            connection.close()
            return redirect(url_for('success'))  # Redirect to success page
        else:
            return "Error connecting to the database"
    return render_template('register_ticket.html')

# Route for payment management
@app.route('/register_payment', methods=['GET', 'POST'])
def register_payment():
    if request.method == 'POST':
        # Get form data from the HTML form
        ticket_id = request.form['ticket_id']
        payment_amount = request.form['payment_amount']
        
        # Create connection and insert payment data into the database
        connection = create_connection()
        if connection:
            insert_payment(connection, ticket_id, payment_amount)
            connection.close()
            return redirect(url_for('success'))  # Redirect to success page
        else:
            return "Error connecting to the database"
    return render_template('register_payment.html')

# Route to view all registered events
@app.route('/view_events')
def view_events():
    connection = create_connection()
    events = []
    if connection:
        events = get_all_events(connection)
        connection.close()
    return render_template('view_events.html', events=events)

# Route to view all payments
@app.route('/view_payments')
def view_payments():
    connection = create_connection()
    payments = []
    if connection:
        payments = get_all_payments(connection)
        connection.close()
    return render_template('view_payments.html', payments=payments)

# Success route (to show after form submission)
@app.route('/success')
def success():
    return "Operation successful!"

if __name__ == '__main__':
    app.run(debug=True)
