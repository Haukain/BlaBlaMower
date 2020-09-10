# BlaBlaMower main program

import os

from Parser import Parser
from Mower import Mower

if __name__ == "__main__":

    root_path = os.getcwd()
    configs_folder = os.path.join(root_path, "configs")

    config_name = "instructions_set_1"
    config_path = os.path.join(configs_folder, config_name)
    parser = Parser(config_path)

    board_size, mowers_configs = parser.parse_config_file()

    print(board_size)
    print(mowers_configs)

    mowers = [Mower(mower_config[0], mower_config[1]) for mower_config in mowers_configs]
