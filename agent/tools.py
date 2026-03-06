from scheduler.appointment_engine import (
    check_availability,
    book_appointment,
    cancel_appointment,
)

def handle_tools(intent_data):

    if "book" in intent_data:

        slots = check_availability()

        if slots:
            return book_appointment(slots[0])

    if "cancel" in intent_data:

        return cancel_appointment()

    return "I couldn't understand the request"