patients = {}

def save_patient(patient_id, data):

    patients[patient_id] = data


def get_patient(patient_id):

    return patients.get(patient_id, {})