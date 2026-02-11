## 📑 Task 2 — Sequence Diagrams for API Calls

### Explanatory Notes

This section provides a detailed breakdown of the interaction between the application layers for four primary API operations. Each entry describes the use case, the technical steps, and the specific role of the **Presentation**, **Business Logic**, and **Persistence** layers.

---

### 1️⃣ API Call: User Registration

**Objective:** To allow a new user to create an account in the system.

**Brief Description:**
When a registration request is received, the system validates the input, enforces business constraints (such as email uniqueness), creates the `User` entity, and persists the data.

**Key Execution Steps:**

1. **Client** sends a `POST /users` request with details such as name, email, and password.
2. **API (Presentation)** validates the JSON structure, including required fields and data types.
3. **API** delegates the task to the `Facade` via a call like `register_user()`.
4. **Facade (Business Logic)** applies business rules, such as checking if the email is already registered and validating field constraints.
5. **Facade** instantiates the `User` object, which inherits from `BaseModel`.
6. **Facade** requests the **Persistence** layer to store the new user.
7. **Persistence** saves the record and returns the saved object or ID.
8. **API** sends a `201 Created` response (or error) back to the **Client**.

**Role of Layers:**

* **Presentation**: Handles HTTP communication, initial form validation, and response formatting.
* **Business Logic**: Centralizes rules like email uniqueness, orchestrates entity creation, and prevents direct API access to models.
* **Persistence**: Executes the physical data storage operation.

---

### 2️⃣ API Call: Place Creation

**Objective:** To allow a user to list a property (Place) associated with an owner and specific amenities.

**Brief Description:**
The system receives property details, ensures the owner exists, links any provided amenities, and saves the new listing.

**Key Execution Steps:**

1. **Client** sends `POST /places` with title, price, coordinates, and `owner_id`.
2. **API** validates the request format and data types.
3. **API** calls the `Facade` to execute `create_place()`.
4. **Facade** performs business validation, confirming the `owner_id` exists and validating price/coordinates.
5. **Facade** creates the `Place` entity and, if amenities are provided, verifies their existence to establish Many-to-Many links.
6. **Facade** instructs **Persistence** to save the Place and its associations.
7. **Persistence** commits the data and returns confirmation.
8. **API** delivers the final response to the client.

**Role of Layers:**

* **Presentation**: Acts as the gateway for incoming property data.
* **Business Logic**: Orchestrates the relationship between Owners, Places, and Amenities.
* **Persistence**: Manages the storage of the Place and relational mapping for amenities.

---

### 3️⃣ API Call: Review Submission

**Objective:** To enable a user to submit a rating and comment for a specific place.

**Brief Description:**
The system validates that both the user and the place exist, ensures the rating is within the allowed range, and links the review to both entities.

**Key Execution Steps:**

1. **Client** sends `POST /reviews` with `place_id`, `user_id`, `rating`, and `comment`.
2. **API** validates the basic JSON structure.
3. **API** triggers the `Facade` via `add_review()`.
4. **Facade** verifies the target `Place` and `User` exist and validates that the rating is within the accepted range (e.g., 1–5).
5. **Facade** creates the `Review` entity and requests the **Persistence** layer to save it.
6. **Persistence** stores the data and confirms.
7. **API** returns the result to the user.

**Role of Layers:**

* **Presentation**: Receives review data and maps it to the internal service.
* **Business Logic**: Ensures data integrity by checking dependencies (User/Place) before saving.
* **Persistence**: Records the review in the database.

---

### 4️⃣ API Call: Fetching a List of Places

**Objective:** To retrieve a list of all properties, potentially filtered by specific criteria.

**Brief Description:**
The system processes search parameters, queries the database for matching records, and returns a collection of places.

**Key Execution Steps:**

1. **Client** sends a `GET /places` request, optionally with query filters.
2. **API** parses parameters and calls the `Facade`.
3. **Facade** validates filter values and requests the **Persistence** layer to find records.
4. **Persistence** retrieves the data from storage and returns a list.
5. **Facade** may format or sanitize the list before passing it up.
6. **API** sends the list back to the **Client**.

**Role of Layers:**

* **Presentation**: Handles query parameters and returns the JSON collection.
* **Business Logic**: Standardizes the search request and handles results.
* **Persistence**: Performs the efficient retrieval of records.

---

### 💡 Summary of Sequence Principles

Across all four diagrams:

* **Flow Direction**: Every request follows a strict path: `Client → Presentation → Facade → Persistence`.
* **Encapsulation**: The API never talks to the Database directly; it must go through the **Facade**.
* **Consistency**: The **Facade** ensures business rules are applied identically regardless of the request source.