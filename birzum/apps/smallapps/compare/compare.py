from django.conf import settings


class Compare(object):
    def __init__(self, request):
        """
        Initialize the compare.
        """

        self.session = request.session
        compare = self.session.get(settings.COMPARE_SESSION_ID)
        if not compare:
            # save an empty compare in the session
            compare = self.session[settings.COMPARE_SESSION_ID] = {}
        self.compare = compare

    def add(self, product_id):
        """
        Add a product to the compare or update its quantity.
        """
        if product_id not in self.compare.keys():
            self.compare[product_id] = True
        
        self.save()
    
    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product_id):
        """
        Remove a product from the compare.
        """
        if product_id in self.compare:
            del self.compare[product_id]
            self.save()

    def clear(self):
        # remove compare from session
        del self.session[settings.COMPARE_SESSION_ID]
        self.save()
