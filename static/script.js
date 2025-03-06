// Wait for the DOM content to be loaded
document.addEventListener("DOMContentLoaded", function() {
    // Get the form element
    const form = document.querySelector("form");

    // Event listener to validate form before submission
    form.addEventListener("submit", function(event) {
        let isValid = true;

        // Validate event name
        const eventName = document.getElementById("event_name").value;
        if (eventName === "") {
            alert("Event name is required.");
            isValid = false;
        }

        // Validate event date
        const eventDate = document.getElementById("event_date").value;
        if (eventDate === "") {
            alert("Event date is required.");
            isValid = false;
        }

        // Validate total tickets
        const totalTickets = document.getElementById("total_tickets").value;
        if (totalTickets === "" || totalTickets <= 0) {
            alert("Please enter a valid number of tickets.");
            isValid = false;
        }

        // Validate description
        const description = document.getElementById("description").value;
        if (description === "") {
            alert("Description is required.");
            isValid = false;
        }

        // If validation fails, prevent form submission
        if (!isValid) {
            event.preventDefault();
        }
    });
});
