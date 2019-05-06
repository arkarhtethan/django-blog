

def must_be_superuser(fun):

    def wrapper(request):

        if not request.is_authenticated:

            raise Http
