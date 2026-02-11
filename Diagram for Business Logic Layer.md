graph TD
    subgraph PresentationLayer [Presentation Layer]
        direction TB
        ServiceAPI[Services & API REST]
    end

    subgraph BusinessLogicLayer [Business Logic Layer]
        direction TB
        Facade[HBnB Facade]
        Models[Domain Models: User, Place, Review, Amenity]
    end

    subgraph PersistenceLayer [Persistence Layer]
        direction TB
        Repository[Data Repository]
        Database[(Database Storage)]
    end

    ServiceAPI -->|Calls methods| Facade
    Facade -->|Orchestrates| Models
    Models -->|Data Operations| Repository
    Repository -->|Persists/Retrieves| Database