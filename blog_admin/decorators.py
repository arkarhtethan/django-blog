
def login_required(fun):

    def wrapper(request, *args, **kwargs):

        result = fun(request,*args, **kwargs)

        return result

    return wrapper