status_codes = {
    400:"Bad Request",
    401:"Unauthorized",
    402:"Payment Required",
    422:"Unprocessable Entity",
    429:"Too Many Requests",
    500:"Internal Server Error",
    503:"Service Unavailable"
}

class ApiException(Exception):
    def __init__(self, status_code: int, message: str = None):
        self.status_code = status_code
        self.message = message or status_codes.get(status_code, "Unknown Error")
        print('test commit 1')
        print('test commit 2')
        super().__init__(self.message)
