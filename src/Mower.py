from src.utils import AVAILABLE_DIRECTIONS, AVAILABLE_ORIENTATIONS, next_element, previous_element


class Mower():

    def __init__(self, lawn_size, position, instructions):

        # Size of the lawn where the mower is
        self.lawn_width = lawn_size[0]
        self.lawn_height = lawn_size[1]

        # Position and orientation of the mower on the lawn
        self.x = position[0]
        self.y = position[1]
        self.orientation = position[2]

        # List of instruction the mower has to execute
        self.instructions_queue = instructions

        # Storing the desired x and y position after executing an instruction while waiting for permission
        self.wants_to_move = False
        self.desired_x = self.x
        self.desired_y = self.y

    # Step of the mower lifecycle
    def tick(self, n):

        # Read instruction n
        current_instruction = self.instructions_queue[n]

        # Depending on the instruction, either go forward ("F"), or stay and turn right ("R") or left ("L")
        if(current_instruction == "F"):
            self.forward()
        else:
            self.stay()
            if(current_instruction == "R"):
                self.turn(is_right_turn=True)
            else:
                self.turn(is_right_turn=False)

    # Execute a forward instruction
    def forward(self):
        # Depending on the orientaion of the mower get the position delta that will be applied if moving forward
        delta_x, delta_y = AVAILABLE_DIRECTIONS[self.orientation]
        new_x = self.x + delta_x
        new_y = self.y + delta_y

        # If the instruction doesn't break the rules, update the mower desired position and notify that the mower wants to move
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

    # Execute a turn instruction
    def turn(self, is_right_turn):
        # If it is a right turn get the next element in the list of possible orientations
        if(is_right_turn):
            new_orientation = next_element(AVAILABLE_ORIENTATIONS, self.orientation)
        # If it is a left turn, get the previous one
        else:
            new_orientation = previous_element(AVAILABLE_ORIENTATIONS, self.orientation)
        # Update the orientation immediatly
        self.orientation = new_orientation

    # Resolve the desired position
    # If allowed to move, update the real position
    # Else discard the instruction
    def resolve(self, permission):
        if(permission):
            self.x = self.desired_x
            self.y = self.desired_y
            self.wants_to_move = False
        else:
            self.desired_x = self.x
            self.desired_y = self.y
            self.wants_to_move = False
