session_store = {}


def save_session(session_id, data):

    if session_id not in session_store:
        session_store[session_id] = {}

    session_store[session_id].update(data)


def get_session(session_id):

    return session_store.get(session_id, {}).copy()


def clear_session(session_id):

    session_store.pop(session_id, None)