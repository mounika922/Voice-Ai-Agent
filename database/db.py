appointments = []

def save_appointment(patient, slot):
    appointments.append({
        "patient": patient,
        "slot": slot
    })

def get_appointments():
    return appointments