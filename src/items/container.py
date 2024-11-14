
class Container:
    def __init__(self, id, name, description, is_open=False, is_locked=False, is_lockable=False):
        self.id = id
        self.name = name
        self.description = description
        self.items = []
        self.is_open = is_open
        self.is_locked = is_locked
        self.is_lockable = is_lockable

    def open(self):
        if not self.is_open and not self.is_locked:
            self.is_open = True
            return f"You open the {self.name}."
        else:
            return f"The {self.name} is already open."

    def close(self):
        if self.is_open:
            self.is_open = False
            return f"You close the {self.name}."
        else:
            return f"The {self.name} is already closed."

    def lock(self):
        if self.is_lockable:
            if not self.is_open and not self.is_locked:
                self.is_locked = True
                return f"You lock the {self.name}."
            elif self.is_open:
                return f"You must close the {self.name} before you can lock it."
            elif self.is_locked:
                return f"The {self.name} is already locked."
        else:
            return f"You cannot lock the {self.name}."

    def unlock(self):
        if self.is_lockable:
            if self.is_locked:
                self.is_locked = False
                return f"You unlock the {self.name}."
            else:
                return f"The {self.name} is already unlocked."
        else:
            return f"The {self.name} cannot be locked or unlocked."

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
        else:
            return None

    def get_items(self):
        return self.items