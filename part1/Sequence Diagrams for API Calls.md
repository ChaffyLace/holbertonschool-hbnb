```mermaid
sequenceDiagram
    autonumber
    title Flux d'Appels API - HBnB Evolution

    actor User
    participant API as Presentation Layer (API)
    participant BL as Business Logic Layer (Facade)
    participant DB as Persistence Layer (Database)

    Note over User, DB: 1. INSCRIPTION UTILISATEUR (User Registration)
    User->>API: POST /users (email, password, etc.)
    API->>BL: create_user(data)
    BL->>DB: get_user_by_email(email)
    DB-->>BL: null (User available)
    BL->>BL: Hash password & Validation
    BL->>DB: save(user_instance)
    DB-->>BL: Success
    BL-->>API: User Object
    API-->>User: 201 Created

    Note over User, DB: 2. CRÉATION D'UN LIEU (Place Creation)
    User->>API: POST /places (title, price, owner_id)
    API->>BL: create_place(data)
    BL->>DB: get_user_by_id(owner_id)
    DB-->>BL: Owner Found
    BL->>BL: Validate latitude/longitude
    BL->>DB: save(place_instance)
    DB-->>BL: Success
    BL-->>API: Place Object
    API-->>User: 201 Created

    Note over User, DB: 3. SOUMISSION D'UN AVIS (Review Submission)
    User->>API: POST /reviews (place_id, user_id, rating)
    API->>BL: create_review(data)
    BL->>DB: get_place_by_id(place_id)
    DB-->>BL: Place exists
    BL->>DB: get_user_by_id(user_id)
    DB-->>BL: User exists
    BL->>DB: save(review_instance)
    DB-->>BL: Success
    BL-->>API: Review Object
    API-->>User: 201 Created

    Note over User, DB: 4. RÉCUPÉRATION DES LIEUX (Fetching Places)
    User->>API: GET /places
    API->>BL: get_all_places()
    BL->>DB: fetch_all("places")
    DB-->>BL: List of records
    BL->>BL: Serialize objects
    BL-->>API: Array of Places
    API-->>User: 200 OK
