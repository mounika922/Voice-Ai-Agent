# Real-Time Multilingual Voice AI Agent

## Clinical Appointment Booking System

---

# Project Overview

This project implements a **Real-Time Multilingual Voice AI Agent** that manages clinical appointments through voice or text conversations.

The system can:

* Understand **spoken language**
* Convert **speech to text**
* Detect **user language**
* Interpret user **intent**
* Perform appointment operations such as:

  * Booking appointments
  * Cancelling appointments
  * Checking doctor availability
* Respond to the user with structured responses.

The system supports multiple languages including:

* English
* Hindi
* Tamil

The project demonstrates key concepts such as:

* Real-time voice processing
* AI agent architecture
* Tool orchestration
* Memory management
* Backend API development
* Low latency communication pipelines

---

# Installation and Setup

## 1. Clone the Repository

```
git clone <repository-url>
cd voice-ai-agent
```

---

## 2. Create Virtual Environment

```
python -m venv venv
```

Activate the environment:

```
venv\Scripts\activate
```

---

## 3. Install Dependencies

```
pip install fastapi uvicorn openai-whisper langdetect python-multipart
```

---

# Running the Application

Start the FastAPI server:

```
uvicorn backend.main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

# API Endpoints

| Endpoint        | Method | Description                       |
| --------------- | ------ | --------------------------------- |
| `/`             | GET    | Health check endpoint             |
| `/process-text` | POST   | Process text appointment requests |
| `/voice`        | POST   | Process voice input (audio file)  |

---

# Example API Request

Text input example:

```
book cardiologist appointment tomorrow
```

Response example:

```
Appointment with cardiologist booked at 10:00 AM
```

---

# Voice Interaction

The `/voice` endpoint accepts an **audio file**.

Example speech command:

```
Book cardiologist appointment tomorrow
```

The system processes:

```
Audio → Text → Intent → Scheduler → Response
```

---

# Appointment Scheduler Logic

The scheduler performs:

* Doctor availability checking
* Slot selection
* Conflict detection
* Appointment cancellation

Example available slots:

```
Cardiologist
- 10:00 AM
- 2:00 PM
- 4:30 PM
```

---

# Session Memory Design

The system stores conversation context using **session memory**.

Example stored context:

```
{
 "intent": "book",
 "doctor": "cardiologist"
}
```

Session memory allows the AI agent to track conversation state.

---

# Latency Measurement

The system measures request processing latency.

Example output:

```
Latency: 120 ms
```

Target latency requirement:

```
< 450 ms
```

---

# Known Limitations

* Basic rule-based intent detection
* No persistent database storage
* Voice input requires pre-recorded audio file
* Real-time streaming voice not implemented

---

# Future Improvements

* Redis-based session memory
* Real-time WebSocket voice streaming
* PostgreSQL appointment database
* Advanced AI agent reasoning using LLMs
* Cloud deployment

---

# Demo Instructions

1. Run the backend server
2. Open API documentation

```
http://127.0.0.1:8000/docs
```

3. Test `/process-text` endpoint

Example:

```
book cardiologist appointment tomorrow
```

4. Test `/voice` endpoint by uploading a `.wav` audio file.

---

# Author

Real-Time Voice AI Agent Implementation for Clinical Appointment Automation.

---
