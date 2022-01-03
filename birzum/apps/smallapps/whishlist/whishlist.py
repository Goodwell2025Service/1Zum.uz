from django.conf import settings


class Whishlist(object):
    def __init__(self, request):
        """
        Initialize the whishlist.
        """

        self.session = request.session
        whishlist = self.session.get(settings.WHISHLIST_SESSION_ID)
        if not whishlist:
            # save an empty whishlist in the session
            whishlist = self.session[settings.WHISHLIST_SESSION_ID] = {}
        self.whishlist = whishlist

    def add(self, product_id):
        """
        Add a product to the whishlist or update its quantity.
        """
        if product_id not in self.whishlist.keys():
            self.whishlist[product_id] = True
        
        self.save()
    
    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product_id):
        """
        Remove a product from the whishlist.
        """
        if product_id in self.whishlist:
            del self.whishlist[product_id]
            self.save()

    def clear(self):
        # remove whishlist from session
        del self.session[settings.WHISHLIST_SESSION_ID]
        self.save()
