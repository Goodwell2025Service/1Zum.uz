from .whishlist import Whishlist


def whishlist_context(request):
    return {"whishlist": Whishlist(request)}