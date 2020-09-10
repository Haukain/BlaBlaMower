# content of test_sysexit.py
import pytest
import os

from src.Parser import Parser

root_path = os.getcwd()
test_configs_folder = os.path.join(root_path, "tests", "test_configs")


class TestParser:

    def test_parsing_incorrect_syntax(self):

        subfolder = "incorrect_syntax"

        # Test with incorrect number of lines in the file
        test_config_path = os.path.join(test_configs_folder, subfolder, "incorrect_number_of_lines")
        parser = Parser(test_config_path)

        with pytest.raises(ValueError):
            parser.parse_config_file()

    def test_parsing_incorrect_board_sizes(self):

        subfolder = "incorrect_board_sizes"

        # Test with incorrect character in board size
        test_config_path = os.path.join(test_configs_folder, subfolder, "incorrect_character")
        parser = Parser(test_config_path)

        with pytest.raises(ValueError):
            parser.parse_config_file()

        # Test with missing value in board size
        test_config_path = os.path.join(test_configs_folder, subfolder, "missing_value")

        parser = Parser(test_config_path)

        with pytest.raises(ValueError):
            parser.parse_config_file()

        # Test with negative value in board size
        test_config_path = os.path.join(test_configs_folder, subfolder, "negative_value")

        parser = Parser(test_config_path)

        with pytest.raises(ValueError):
            parser.parse_config_file()

    def test_parsing_incorrect_mower_positions(self):

        subfolder = "incorrect_mower_positions"

        # Test with incorrect direction
        test_config_path = os.path.join(test_configs_folder, subfolder, "incorrect_direction")
        parser = Parser(test_config_path)

        with pytest.raises(ValueError):
            parser.parse_config_file()

        # Test with a missing value in an position line
        test_config_path = os.path.join(test_configs_folder, subfolder, "missing_value")
        parser = Parser(test_config_path)

        with pytest.raises(ValueError):
            parser.parse_config_file()

        # Test with multiple mowers assigned to the same initial position
        test_config_path = os.path.join(test_configs_folder, subfolder, "multiple_mowers_on_position")
        parser = Parser(test_config_path)

        with pytest.raises(ValueError):
            parser.parse_config_file()

        # Test with a negative value in an initial position
        test_config_path = os.path.join(test_configs_folder, subfolder, "negative_value")
        parser = Parser(test_config_path)

        with pytest.raises(ValueError):
            parser.parse_config_file()

        # Test with a mower assigned to an out of bounds position
        test_config_path = os.path.join(test_configs_folder, subfolder, "out_of_bounds")
        parser = Parser(test_config_path)

        with pytest.raises(ValueError):
            parser.parse_config_file()

        # Test with a lower case direction
        test_config_path = os.path.join(test_configs_folder, subfolder, "lower_case_direction")
        parser = Parser(test_config_path)

        with pytest.raises(ValueError):
            parser.parse_config_file()

    def test_parsing_incorrect_mower_instructions(self):

        subfolder = "incorrect_mower_instructions"

        # Test with an incorrect direction
        test_config_path = os.path.join(test_configs_folder, subfolder, "incorrect_direction")
        parser = Parser(test_config_path)

        with pytest.raises(ValueError):
            parser.parse_config_file()

        # Test with a lower case direction
        test_config_path = os.path.join(test_configs_folder, subfolder, "lower_case_direction")
        parser = Parser(test_config_path)

        with pytest.raises(ValueError):
            parser.parse_config_file()

    def test_parsing_correct_configurations(self):

        subfolder = "correct_configs"

        # Test original example
        test_config_path = os.path.join(test_configs_folder, subfolder, "base_example")
        parser = Parser(test_config_path)

        board_size, mowers = parser.parse_config_file()
        assert board_size == (5, 5)
        assert mowers == [
            ((1, 2, "N"), ["L", "F", "L", "F", "L", "F", "L", "F", "F"]),
            ((3, 3, "E"), ["F", "F", "R", "F", "F", "R", "F", "R", "R", "F"])
        ]

        # Test with a big rectangle board
        test_config_path = os.path.join(test_configs_folder, subfolder, "big_rectangle_board")
        parser = Parser(test_config_path)

        board_size, mowers = parser.parse_config_file()
        assert board_size == (300, 500)
        assert mowers == [
            ((80, 236, "W"), ["L", "F", "L", "F"]),
            ((300, 378, "S"), ["F", "F", "R", "F"])
        ]

        # Test with many mowers
        test_config_path = os.path.join(test_configs_folder, subfolder, "many_mowers")
        parser = Parser(test_config_path)

        board_size, mowers = parser.parse_config_file()
        assert board_size == (10, 10)
        assert mowers == [
            ((6, 4, "N"), ["L", "F"]),
            ((3, 3, "S"), ["R", "F", "F", "R"]),
            ((1, 2, "S"), ["L", "F", "L", "F", "L", "F", "L", "F", "F"]),
            ((2, 3, "E"), ["R", "F", "R", "L", "L", "R", "F"]),
            ((1, 8, "W"), ["L", "F", "L", "F"]),
            ((4, 3, "E"), ["F", "F", "R", "L"]),
            ((1, 4, "N"), ["L", "F", "L", "F", "L", "F", "L", "F", "F"]),
            ((4, 5, "N"), ["F", "F", "R", "F"]),
            ((1, 1, "N"), ["F", "F"]),
            ((3, 4, "E"), ["F", "R", "R", "F"]),
            ((8, 8, "W"), ["F", "L", "F", "F"]),
            ((3, 9, "E"), ["F", "F", "R", "F"]),
            ((10, 2, "S"), ["L", "F", "L", "F", "L", "F", "L", "F", "F"]),
            ((3, 5, "W"), ["L", "L", "L", "R", "R"]),
            ((6, 2, "N"), ["L", "F", "L", "F", "L", "F", "L", "F", "F"]),
            ((3, 7, "E"), ["F", "F", "L", "L", "R", "R", "L", "R", "R", "F"])
        ]
