class NonPositiveError(Exception):
    pass


class  PositiveList(list):
    def append(self, object):
        if object > 0:
            super().append(object)
        elif object <= 0:
            raise NonPositiveError