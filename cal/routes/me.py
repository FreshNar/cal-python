from cal.urls.me import ME_ROUTES

class MeRoutes:
    """
    A class to manage user-related routes.

    """

    @staticmethod
    def get():
        # Get my profile
        return ME_ROUTES["get"]
    
    @staticmethod
    def update():
        # Update my profile
        return ME_ROUTES["update"]