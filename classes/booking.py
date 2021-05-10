class Booking:
    def __init__(self, user_id, start_location, end_location, price, start_date, end_date, type, number):
        self.user_id = user_id
        self.start_location = start_location
        self.end_location = end_location
        self.price = price
        self.start_date = start_date
        self.end_date = end_date
        self.type = type
        self.number = number
        self.status = 'NOT CONFIRMED'
        self.payment_id = None

