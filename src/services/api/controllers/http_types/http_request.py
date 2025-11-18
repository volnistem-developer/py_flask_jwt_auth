class HttpRequest:
    def __init__(
        self,
        body: dict = None,
        headers: dict = None,
        params: dict = None,
        token_info: dict = None,
    ) -> None:
        self.body = body
        self.headers = headers
        self.params = params
        self.token_info = token_info
