class ObjectNotFoundError(Exception):
    def __init__(self, object_id: int, class_name: str):
        self.class_name = class_name
        self.object_id = object_id