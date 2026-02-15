```mermaid

classDiagram
direction LR
    class BaseEntity {
	    +UUID4 id
	    +datetime created_at
	    +datetime updated_at
	    +create()
	    +update()
	    +delete()
    }

    class User {
	    +string first_name
	    +string last_name
	    +string email
	    +string password
	    +boolean is_admin
	    +register()
	    +update_profile()
	    +delete()
    }

    class Place {
	    +string title
	    +string description
	    +float price
	    +float latitude
	    +float longitude
	    +create()
	    +update()
	    +delete()
    }

    class Review {
	    +int rating
	    +string comment
        +create()
	    +update()
	    +delete()
    }

    class Amenity {
	    +string name
	    +string description
        +create()
	    +update()
	    +delete()
    }

	 BaseEntity

    BaseEntity <|-- User
    BaseEntity <|-- Place
    BaseEntity <|-- Review
    BaseEntity <|-- Amenity
    User "1" -- "0..*" Place : owns
