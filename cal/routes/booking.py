from cal.urls.booking import BOOKING_ROUTES

class BookingRoutes:
    """ 
    A class to manage booking routes.
    This class provides methods to build URLs for booking-related API endpoints.
    """

    @staticmethod
    def get(bookingUid): return BOOKING_ROUTES["get"].format(bookingUid=bookingUid)

    @staticmethod
    def list(): return BOOKING_ROUTES["list"]

    @staticmethod
    def create(): return BOOKING_ROUTES["create"]

    @staticmethod
    def get_recordings(bookingUid): return BOOKING_ROUTES["get_recordings"].format(bookingUid=bookingUid)

    @staticmethod
    def get_transcript(bookingUid): return BOOKING_ROUTES["get_transcript"].format(bookingUid=bookingUid)
    
    @staticmethod
    def reschedule(bookingUid): return BOOKING_ROUTES["reschedule"].format(bookingUid=bookingUid)

    @staticmethod
    def cancel(bookingUid): return BOOKING_ROUTES["cancel"].format(bookingUid=bookingUid)

    @staticmethod
    def mark_absent(bookingUid): return BOOKING_ROUTES["mark_absent"].format(bookingUid=bookingUid)

    @staticmethod
    def reassign_auto(bookingUid): return BOOKING_ROUTES["reassign_auto"].format(bookingUid=bookingUid)

    @staticmethod
    def reassign_specific(bookingUid, userId): return BOOKING_ROUTES["reassign_specific"].format(bookingUid=bookingUid, userId=userId)

    @staticmethod
    def confirm(bookingUid): return BOOKING_ROUTES["confirm"].format(bookingUid=bookingUid)

    @staticmethod
    def decline(bookingUid): return BOOKING_ROUTES["decline"].format(bookingUid=bookingUid)

    @staticmethod
    def add_to_calendar_links(bookingUid): return BOOKING_ROUTES["add_to_calendar_links"].format(bookingUid=bookingUid) 

    @staticmethod
    def references(bookingUid): return BOOKING_ROUTES["references"].format(bookingUid)