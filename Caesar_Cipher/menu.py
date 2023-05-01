class Menu:
    def __init__(self, menu_title: str, isRoot: bool = False):
        self.menu_title = menu_title
        self.menu_items = []
        self.isRoot = isRoot

    def append(self, menu_item: str):
        self.menu_items.append(menu_item)
        return self

    def pop(self, item_number: int):
        if (item_number <= len(self.menu_items)):
            self.menu_items.pop(item_number - 1)

    def print_menu(self):
        print(f"---- {self.menu_title} ----")
        for i in range(len(self.menu_items)):
            item = self.menu_items[i]
            print(f"{i+1}. {item}")
        if (self.isRoot):
            print(" type 'exit' to exit program")
        else:
            print(" type 'back' to go back")
