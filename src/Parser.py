class Parser:

    def __init__(self, file_path):

        self.file_path = file_path

    def parse_config_file(self):

        f = open(self.file_path, "r")
        lines = f.readlines()

        # Check that the config file has a correct number of lines (1 board size line and pairs of lines for mowers)
        if(len(lines) % 2 != 1):
            raise ValueError(f'Given configuration file {self.file_path} has an incorrect number of lines')

        # Get the first config line and split on the " " character to get the board size
        board_size_line = lines.pop(0)
        board_size = board_size_line.split(" ")

        # Check that the width and height values of the board are 2 positive integers
        if(len(board_size) < 2):
            raise ValueError(f'Given configuration file {self.file_path} has an incorrect board size (Not enough values)')
        try:
            width = int(board_size[0])
            height = int(board_size[1])
        except ValueError:
            print(f'Given configuration file {self.file_path} has an incorrect board size (Non-integer characters)')
            raise
        if(width < 0 or height < 0):
            raise ValueError(f'Given configuration file {self.file_path} has an incorrect board size (negative values)')
        # If no prior exception was raised, the board size is valid
        board_size = (width, height)

        # Get the mowers positions & instructions
        mowers = []
        for i in range(len(lines)):
            if(i % 2 == 0):

                mower_id = i//2

                initial_position_line = lines[i]
                instructions_line = lines[i+1]

                # Get the 3 components of the initial position
                initial_position = initial_position_line.split('\n')[0].split(" ")

                # Check that the x and y values of the mower initial position are 2 positive integers within the board
                if(len(initial_position) < 3):
                    raise ValueError(f'Given configuration file {self.file_path} has an incorrect initial position for mower n°{mower_id}')
                try:
                    x = int(initial_position[0])
                    y = int(initial_position[1])
                except ValueError:
                    print(f'Given configuration file {self.file_path} has an incorrect initial position for mower n°{mower_id}')
                    raise
                if(x < 0 or x > board_size[0] or y < 0 or y > board_size[1]):
                    raise ValueError(f'Given configuration file {self.file_path} has an incorrect initial position for mower n°{mower_id}')

                # Check that the x,y position is not already occupied by another mower
                if((x, y) in [(mower[0][0], mower[0][1]) for mower in mowers]):
                    raise ValueError(f'Given configuration file {self.file_path} has multiple mowers using the same initial position')

                # Check that the direction is valid
                direction = initial_position[2]
                if(direction not in ["N", "E", "W", "S"]):
                    raise ValueError(f'Given configuration file {self.file_path} has an incorrect initial direction for mower n°{mower_id}')

                # If no prior exception was raised, the mower position and direction is valid
                initial_position = (x, y, direction)

                # Get the instruction list of the mower
                instructions = list(instructions_line.split('\n')[0])
                # Check that it contains only correct characters
                for it in instructions:
                    if(it not in ["F", "L", "R"]):
                        raise ValueError(f'Given configuration file {self.file_path} has an incorrect instruction list for mower n°{mower_id}')

                # Add this mower to the list
                mowers.append((initial_position, instructions))

        # Return the board size and the list of mowers extracted from the config file
        return board_size, mowers
