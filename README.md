# Repository for BlaBlaCar's​ ​Technical Test

In this repository you will find the code for the technical test I have been given during BlaBlaCar's hiring process.

## Presentation

The goal is to make a simulation of mowers moving around on a rectangular lawn. This field is represented as a *NxM* grid, each square being given coordinates, the bottom left corner being *(0,0)* and the top right one *(N,M)*.

Each mower can move using 3 commands. 'F' which makes the mower go forward one square. 'R' and 'L' which make the mower turn 90° right and left respectively without moving. At any given time, the mower has a 'x' and 'y' position as well as an orientation (N, E, W, S) on the lawn.

The moving machines have to follow these rules :
- The mowers cannot go outside the lawn.
- The mowers cannot go on a occupied square.
If a command would break these rules, it is discarded.

The simulation is ran using a configuration file following this strucure:
- The first line corresponds to the upper right corner of the lawn.The bottom left corner is
implicitly (0, 0).
- The rest of the file describes the multiple mowers that are on the lawn. Each mower is described on two lines. The first line contains the mower's starting position and orientation in the format "X Y O". X and Y are the coordinates and O is the orientation. The second line contains the instructions for the mower to navigate the lawn. The instructions are not separated by spaces.

The simulation will be run on a machine with multiple CPUs so multiple mowers should be processed simultaneously in order to speed up the overall execution time.
At the end of the simulation, the final positions and orientations of the mowers are output by the application in the order they were declared in the configuration file.

## Project structure:
- **configs/** : *folder containing the config files used to setup the application*
- **src/** : *folder containing the source files of the application*
- **tests/** : *folder containing the tests files of the application*
- **output/** : *folder containing the results of the simulations (created during runtime)*
- .gitignore
- main.py
- README.md
- requirements.txt

## Installation

First of all you'll need to download the files for this project either by cloning this repository using git or by downloading the zipped file and extracting of your computer.

This application has been developped using Python 3.8.5. The required libraries and versions are available in the `requirements.txt` file. They can installed using either Pip or Anaconda.

## Usage

Once the project downloaded and the requirements installed, you are ready to use the application.

In the `configs` folder, create your configuration file (following the rules described in the presentation section) or use the example one.

From the root folder of this repository, run `python main.py -c config_name -v`. The `config_name` being the name of the configuration file you want to use.

The application accepts the following command line arguments:
- `-h` or `--help` to get help on the usage of the app
- `-c` or `--config` to select the config file to use in the simulation (**mandatory**)
- `-v` or `--verbose` to run the application in verbose mode

The output of the application is saved in a file in the `output` folder. You can also enable the verbose option to get outputs in the terminal.

Unitary tests are available and should be run to check the validity of the application. From the root folder of this repository, run `pytest` to execute all the tests. Results of the tests will be printed in the terminal.