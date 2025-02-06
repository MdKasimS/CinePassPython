class Receipt:
    # Initialize the static dictionary to prevent null reference issues
    _receipts = {}

    @staticmethod
    def get_receipts():
        return Receipt._receipts

    @staticmethod
    def set_receipts(value):
        if value is None:
            Receipt._receipts = {}
        else:
            Receipt._receipts = value
