

class AportError(Exception):
    """
    Base Aport application exception class.
    """


class CacheKeyNotExistError(AportError):
    """
    Raised when given key not exists in cache
    """
