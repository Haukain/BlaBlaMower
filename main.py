# BlaBlaMower main program

import os
import argparse
import logging

from src.Parser import Parser
from src.Mower import Mower
from src import simulation

if __name__ == "__main__":
    # Create an argument parser for the application
    args_parser = argparse.ArgumentParser(description='Automatic lawn mowing application')
    args_parser.add_argument('-v', '--verbose', action='store_true', help='activate the verbose mode of the application')
    args_parser.add_argument('-c', '--config', required=True, help='name of the configuration file to use')

    args = args_parser.parse_args()
    if(args.verbose):
        logging.basicConfig(format="%(message)s", level=logging.INFO)

    # Get the required config file
    root_path = os.getcwd()
    configs_folder = os.path.join(root_path, "configs")
    config_name = args.config
    config_path = os.path.join(configs_folder, config_name)

    # Create a parser for the config file
    parser = Parser(config_path)
    # Parse the config file to get the lawn size and the mowers parameters
    lawn_size, mowers_configs = parser.parse_config_file()
    logging.info(f"Lawn size: {lawn_size}")
    logging.info(f"Number of mowers: {len(mowers_configs)}")

    mowers = [Mower(lawn_size, mower_config[0], mower_config[1]) for mower_config in mowers_configs]

    # Run the simulation using the created mowers
    # Get the final results
    final_mowers = simulation.run(mowers, args.verbose)

    # Saving the results in the output folder
    # And printing them if verbose is enabled
    logging.info("\nEnd Results")
    results = ""
    for i, mower in enumerate(mowers):
        logging.info(f"Mower n°{i}")
        logging.info(f"Position: ({mower.x}, {mower.y}), Orientation: {mower.orientation}")
        results += f"{mower.x} {mower.y} {mower.orientation}\n"
    with open(os.path.join(root_path, "output", config_name), "w") as f:
        f.write(results)
        f.close()
