from fastapi import FastAPI
from services.language_detection import detect_language

from services.response_formatter import format_response
from agent.agent import interpret_request
from scheduler.appointment_engine import book_appointment, cancel_appointment
from memory.session_memory import save_session, get_session, clear_session

import time
import os

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Voice AI Agent Running"}


@app.post("/process-text")
def process_text(text: str):

    start = time.time()
    session_id = "user1"

    context = get_session(session_id)

    language = detect_language(text)
    intent = interpret_request(text)

    if intent["intent"] == "book":

        save_session(session_id, {"intent": "book"})
        doctor = intent.get("doctor", "cardiologist")

        response = book_appointment(doctor)

        clear_session(session_id)

    elif intent["intent"] == "cancel":

        response = cancel_appointment()

    else:
        response = "I didn't understand"

    response = format_response(response, language)

    latency = (time.time() - start) * 1000

    return {
        "language": language,
        "response": response,
        "latency_ms": latency
    }




  