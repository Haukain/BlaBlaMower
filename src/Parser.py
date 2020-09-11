from src.utils import AVAILABLE_INSTRUCTIONS, AVAILABLE_ORIENTATIONS


class Parser:

    def __init__(self, file_path):

        self.file_path = file_path

    def parse_config_file(self):

        f = open(self.file_path, "r")
        lines = f.readlines()

        # Check that the config file has a correct number of lines (1 lawn size line and pairs of lines for mowers)
        if(not len(lines)):
            raise ValueError(f'Given configuration file {self.file_path} is empty')
        if(len(lines) % 2 != 1):
            raise ValueError(f'Given configuration file {self.file_path} has an incorrect number of lines')

        # Get the first config line and split on the " " character to get the lawn size
        lawn_size_line = lines.pop(0)
        lawn_size = lawn_size_line.split(" ")

        # Check that the width and height values of the lawn are 2 positive integers
        if(len(lawn_size) < 2):
            raise ValueError(f'Given configuration file {self.file_path} has an incorrect lawn size (Not enough values)')
        try:
            width = int(lawn_size[0])
            height = int(lawn_size[1])
        except ValueError:
            print(f'Given configuration file {self.file_path} has an incorrect lawn size (Non-integer characters)')
            raise
        if(width < 0 or height < 0):
            raise ValueError(f'Given configuration file {self.file_path} has an incorrect lawn size (negative values)')
        # If no prior exception was raised, the lawn size is valid
        lawn_size = (width, height)

        # Get the mowers positions & instructions
        mowers = []
        for i in range(len(lines)):
            if(i % 2 == 0):

                mower_id = i//2

                initial_position_line = lines[i]
                instructions_line = lines[i+1]

                # Get the 3 components of the initial position
                initial_position = initial_position_line.split('\n')[0].split(" ")

                # Check that the x and y values of the mower initial position are 2 positive integers within the lawn
                if(len(initial_position) < 3):
                    raise ValueError(f'Given configuration file {self.file_path} has an incorrect initial position for mower n°{mower_id}')
                try:
                    x = int(initial_position[0])
                    y = int(initial_position[1])
                except ValueError:
                    print(f'Given configuration file {self.file_path} has an incorrect initial position for mower n°{mower_id}')
                    raise
                if(x < 0 or x > lawn_size[0] or y < 0 or y > lawn_size[1]):
                    raise ValueError(f'Given configuration file {self.file_path} has an incorrect initial position for mower n°{mower_id}')

                # Check that the x,y position is not already occupied by another mower
                if((x, y) in [(mower[0][0], mower[0][1]) for mower in mowers]):
                    raise ValueError(f'Given configuration file {self.file_path} has multiple mowers using the same initial position')

                # Check that the direction is valid
                direction = initial_position[2]
                if(direction not in AVAILABLE_ORIENTATIONS):
                    raise ValueError(f'Given configuration file {self.file_path} has an incorrect initial direction for mower n°{mower_id}')

                # If no prior exception was raised, the mower position and direction is valid
                initial_position = (x, y, direction)

                # Get the instruction list of the mower
                instructions = list(instructions_line.split('\n')[0])
                # Check that it contains only correct characters
                for it in instructions:
                    if(it not in AVAILABLE_INSTRUCTIONS):
                        raise ValueError(f'Given configuration file {self.file_path} has an incorrect instruction list for mower n°{mower_id}')

                # Add this mower to the list
                mowers.append((initial_position, instructions))

        # Return the lawn size and the list of mowers extracted from the config file
        return lawn_size, mowers
