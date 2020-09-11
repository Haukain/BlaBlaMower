from utils import AVAILABLE_DIRECTIONS, AVAILABLE_ORIENTATIONS, next_element, previous_element


class Mower():

    def __init__(self, lawn_size, position, instructions):
        self.lawn_width = lawn_size[0]
        self.lawn_height = lawn_size[1]

        self.x = position[0]
        self.y = position[1]
        self.orientation = position[2]
        self.instructions_queue = instructions

        self.wants_to_move = False
        self.desired_x = self.x
        self.desired_y = self.y

    def tick(self, n):
        current_instruction = self.instructions_queue[n]

        if(current_instruction == "F"):
            self.forward()
        else:
            self.stay()
            if(current_instruction == "R"):
                self.turn(is_right_turn=True)
            else:
                self.turn(is_right_turn=False)

    def forward(self):
        delta_x, delta_y = AVAILABLE_DIRECTIONS[self.orientation]
        new_x = self.x + delta_x
        new_y = self.y + delta_y
        if((new_x >= 0) and (new_x <= self.lawn_width) and (new_y >= 0) and (new_y <= self.lawn_height)):
            self.wants_to_move = True
            self.desired_x = new_x
            self.desired_y = new_y
        else:
            self.wants_to_move = False
            self.desired_x = self.x
            self.desired_y = self.y

    def stay(self):
        self.wants_to_move = False
        self.desired_x = self.x
        self.desired_y = self.y

    def turn(self, is_right_turn):
        if(is_right_turn):
            new_orientation = next_element(AVAILABLE_ORIENTATIONS, self.orientation)
        else:
            new_orientation = previous_element(AVAILABLE_ORIENTATIONS, self.orientation)
        self.orientation = new_orientation

    def resolve(self, permission):
        if(permission):
            self.x = self.desired_x
            self.y = self.desired_y
            self.wants_to_move = False
        else:
            self.desired_x = self.x
            self.desired_y = self.y
            self.wants_to_move = False
