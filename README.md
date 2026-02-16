# HBnB - Evolution

HBnB is a simplified AirBnB-like application designed to demonstrate software architecture, object-oriented design, and full-stack development principles.  

The project is structured in multiple phases, progressively moving from system design and modeling to implementation and persistence. It emphasizes clean architecture, separation of concerns, and maintainable code organization.

---

## Part 1 – UML Design

Part 1 focuses on the architectural and conceptual design of the system using UML diagrams.

This phase includes:
- A **High-Level Package Diagram** describing the layered architecture.
- A **Detailed Class Diagram** defining the core business entities.
- **Sequence Diagrams** illustrating how API calls interact across system layers.

The purpose of this phase is to establish a clear technical blueprint that will guide the implementation stages of the HBnB project.

---

## 🏗️ 1. Global Architecture (Package Diagram)

The application follows a **3-tier architecture**. This structure ensures that each part of the code has a unique responsibility, facilitating long-term maintenance and scalability.



* **Presentation Layer (API)**: Handles the input interfaces, receives HTTP requests, and returns formatted responses.
* **Business Logic Layer (Facade)**: The "brain" of the application. It validates data and applies business rules through domain models (User, Place, etc.).
* **Persistence Layer (Database)**: Responsible for permanent data storage and retrieval.

---

## 🗂️ 2. Data Model (Class Diagram)

The Class Diagram defines the business entities that make up the system:

* **BaseModel**: The parent class providing common attributes (Unique ID, creation and update timestamps) to avoid redundancy (DRY principle).
* **User**: Represents the application users (clients or owners).
* **Place**: Represents the accommodations available for rent, including geographical and pricing details.
* **Review**: Manages user feedback and ratings.
* **Amenity**: Lists available services (Wifi, Pool, etc.).

**Key Relations:** A user can own multiple places (1:*), and places share a "many-to-many" (*:*) relationship with Amenities.

---

## 🔄 3. Data Flow (Sequence Diagrams)

The Sequence Diagrams illustrate the system's dynamics by detailing interactions between layers during critical scenarios:

1.  **User Registration**: Process of email validation, password hashing, and persistence.
2.  **Place Creation**: Systematic verification of the owner's existence before any creation.
3.  **Review Submission**: Double-check of the existence of both the author and the target place being rated.
4.  **Fetching Places**: Read flow including object serialization for final display.

---

## 🛠️ Applied Key Concepts

* **Separation of Concerns**: Strict isolation between the user interface and the database.
* **Facade Pattern**: Use of a single entry point for the business logic to simplify API calls.
* **Inheritance**: Use of base classes to centralize common technical logic.
