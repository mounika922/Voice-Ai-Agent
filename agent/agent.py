def interpret_request(text):

    text = text.lower()

    doctor = "cardiologist"

    if "dermatologist" in text:
        doctor = "dermatologist"

    if "book" in text:
        return {"intent": "book", "doctor": doctor}

    if "cancel" in text:
        return {"intent": "cancel"}

    if "reschedule" in text:
        return {"intent": "reschedule"}

    return {"intent": "unknown"}