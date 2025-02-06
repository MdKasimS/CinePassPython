class Theatre:
    _theatres = {}

    def __init__(self, id, theatre_name, number_of_seats):
        self.id = id
        self.theatre_name = theatre_name
        self.number_of_seats = number_of_seats

    @classmethod
    def add_theatre(cls, theatre):
        if theatre.id not in cls._theatres:
            cls._theatres[theatre.id] = theatre
        else:
            raise ValueError(f"Theatre with ID {theatre.id} already exists.")

    @classmethod
    def display_theatre_details(cls, theatre_id):
        theatre = cls._theatres.get(theatre_id)
        if theatre:
            print(f"Theatre ID : {theatre.id}")
            print(f"Theatre Name : {theatre.theatre_name}")
            print(f"Seating Capacity : {theatre.number_of_seats}")
        else:
            print(f"Theatre with ID {theatre_id} not found.")

    @classmethod
    def get_theatre(cls, theatre_id):
        return cls._theatres.get(theatre_id)

    # Getters and Setters
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def theatre_name(self):
        return self._theatre_name

    @theatre_name.setter
    def theatre_name(self, value):
        self._theatre_name = value

    @property
    def number_of_seats(self):
        return self._number_of_seats

    @number_of_seats.setter
    def number_of_seats(self, value):
        self._number_of_seats = value


# Example usage:
theatre_1 = Theatre(1, "Cineplex", 150)
Theatre.add_theatre(theatre_1)

# Display theatre details
Theatre.display_theatre_details(1)

# Fetch a specific theatre
theatre = Theatre.get_theatre(1)
if theatre:
    print(f"Found theatre: {theatre.theatre_name}")
