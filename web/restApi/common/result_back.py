class Result:
    def __init__(self, result_object, error=None):
        self.result_object = result_object
        self.error = error

    def exist_error(self):
        if self.error is not None:
            return True
        return False

    def jsnoify_result(self):
        if not self.exist_error():
            return self.result_object.__dict__
        else:
            return self.error.__dict__