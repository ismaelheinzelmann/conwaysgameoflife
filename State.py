class State:

    def __init__(self, state):
        self.state = state

    def _set_state(self, state):
        self.state = state
    
    def set_menu(self):
        self.state = "menu"

    def set_game(self):
        if self.state == "menu":
            self.state = "game"
            