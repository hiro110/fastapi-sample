from functools import wraps

def sample_decorator():
    def _sample_decorator(f):
        @wraps(f)
        def __sample_decorator(*args, **kwargs):
            # just do here everything what you need
            print('before decorator')
            result = f(*args, **kwargs)
            print('decorator result: %s' % result)
            print('after decorator')
            return result
        return __sample_decorator
    return _sample_decorator