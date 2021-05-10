# Author: Ronak

# State variable to store the login information
__state = {
    'current_user_id': None,
    'is_admin': False,
    'current_email': None
}

# Price coefficient to compute price based up the mode of transport
__price = {
    'AIR': 10,
    'RAIL': 5,
    'CAR': 8
}