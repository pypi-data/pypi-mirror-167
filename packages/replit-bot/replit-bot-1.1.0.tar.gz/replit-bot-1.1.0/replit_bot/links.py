from os import environ

class Links:
    """bot urls (docs/apis)"""
    def __init__(self) -> None:
        self.docs: str = f"https://{environ['REPL_SLUG']}.{environ['REPL_OWNER']}.repl.co"
        self.api: str = self.docs + '/api/'

links = Links()