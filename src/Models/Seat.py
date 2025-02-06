class Seat:
    # Initialize the static dictionary to prevent issues with null references
    _seats = {}

    @staticmethod
    def get_seats():
        return Seat._seats

    @staticmethod
    def set_seats(value):
        if value is None:
            Seat._seats = {}
        else:
            Seat._seats = value
