appointments = []

doctor_slots = {
    "cardiologist": ["10:00 AM", "2:00 PM", "4:30 PM"],
    "dermatologist": ["11:00 AM", "3:00 PM"]
}


def check_availability(doctor):
    return doctor_slots.get(doctor, [])


def book_appointment(doctor="cardiologist"):

    slots = check_availability(doctor)

    if not slots:
        return "Doctor not available"

    # check booked slots
    booked_slots = [a["time"] for a in appointments if a["doctor"] == doctor]

    # find first available slot
    for slot in slots:
        if slot not in booked_slots:

            appointments.append({
                "doctor": doctor,
                "time": slot
            })

            return f"Appointment with {doctor} booked at {slot}"

    # if all slots taken
    return f"No slots available for {doctor}. Please try another time."


def cancel_appointment():

    if appointments:
        appointment = appointments.pop()

        return f"Appointment with {appointment['doctor']} at {appointment['time']} cancelled"

    return "No appointment found"