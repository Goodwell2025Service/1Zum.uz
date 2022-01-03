from .compare import Compare


def compare_context(request):
    return {"compare": Compare(request)}
