# Agentic AI Backend

A FastAPI-based backend service for text summarization using OpenAI's GPT-3.5-turbo model.

## Features

- REST API endpoint for text summarization
- Integration with OpenAI's GPT-3.5-turbo
- Containerized with Docker
- Unit tests with pytest

## API Documentation

### POST `/api/summarize`

Summarizes the given text.

## How to run ## 

Re-Open in Dev Container 

 cd agentic2

 pip install -r app/requirements.txt

 uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Open your browser and go to:


http://localhost:8000/docs
Look for the POST /api/summarize endpoint.

Click the "Try it out" button.

You’ll see a box labeled **Request Body:** – paste your JSON there:

{
  "text": "Artificial Intelligence is a branch of computer science focused on building systems that simulate human intelligence."
}

Scroll down and click "Execute".

The server will respond with something like:


{
  "summary": "Artificial Intelligence is a field of computer science."
}
