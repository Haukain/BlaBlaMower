class Mower():

    def __init__(self, position, instructions):

        self.x = position[0]
        self.y = position[1]
        self.direction = position[2]
        self.instructions_queue = instructions

        self.isRunning = False
