# HBnB Evolution API

This project is a simplified backend for an AirBnB-like application, built with Python, Flask, and Flask-RESTx. It follows a modular architecture.

## Installation and Execution

1. Create a virtual environment: `python3 -m venv venv`
2. Activate it: `source venv/bin/activate` (Mac/Linux) or `.\venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python run.py`

## Business Logic Layer

The `app/models/` directory contains the core domain entities:
- **BaseModel**: Handles UUID generation and audit timestamps (`created_at`, `updated_at`).
- **User**: Manages user profiles and authentication data.
- **Place**: Represents rental properties, validating geographical coordinates and prices.
- **Review**: Captures user feedback for a specific place.
- **Amenity**: Defines features associated with places (e.g., Wi-Fi).

All entities inherit from `BaseModel` and utilize Python `@property` decorators to enforce strict data validation before state changes.