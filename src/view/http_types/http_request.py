from typing import Dict

class HttpRequest:
    def __init__(
            self,
            header: Dict = None,
            body: Dict = None,
            query_params: Dict = None
        ) -> None:
        self.header = header
        self.body = body
        self.query_params = query_params

    def to_json(self) -> Dict:
        return {
            "header": self.header,
            "body": self.body,
            "query_params": self.query_params
        }
