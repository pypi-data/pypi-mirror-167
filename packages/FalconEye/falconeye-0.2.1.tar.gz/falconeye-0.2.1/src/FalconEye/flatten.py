class Flatten:
    def __init__(self, obj):
        self.obj = obj
        self.items = {}
        self.queue = []
        def runtime(obj=obj):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if isinstance(value, dict):
                        self.queue.append(value)
                    else:
                        self.items[key] = value
            if self.queue:
                next_item = self.queue.pop()
                runtime(next_item)
        runtime()