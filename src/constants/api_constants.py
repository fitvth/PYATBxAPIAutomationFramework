# APIConstants - Class which contain all the endpoints.
# Keep the URLs

class APIConstants:

    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    def url_put_patch_delete(self,booking_id):
        return "https://restful-booker.herokuapp.com/booking"+str(booking_id)