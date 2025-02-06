class Bill:
    _bills = {}

    @classmethod
    def get_bills(cls):
        return cls._bills

    @classmethod
    def set_bills(cls, bills):
        cls._bills = bills
