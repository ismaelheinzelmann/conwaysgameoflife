class State:

    def __init__(self, state):
        self.state = state
        self.help = False

    def set_state(self, state):
        self.state = state
    
    def set_creating(self):
        self.state = "creating"

    def set_evolving(self):
        if self.state == "creating":
            self.state = "game"

    def switch_help(self):
        self.help = not self.help
            