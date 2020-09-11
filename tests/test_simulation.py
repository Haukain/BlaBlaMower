import pytest
import os

from src.Mower import Mower
from src import simulation

class TestSimulation:

    def test_base_example(self):

        # Base example given with the instructions of the test
        lawn_size = (5, 5)
        mowers = [
            Mower(
                lawn_size,
                (1, 2, 'N'),
                ["L", "F", "L", "F", "L", "F", "L", "F", "F"]
            ),
            Mower(
                lawn_size,
                (3, 3, 'E'),
                ["F", "F", "R", "F", "F", "R", "F", "R", "R", "F"]
            )
        ]

        final_mowers = simulation.run(mowers)

        assert (final_mowers[0].x, final_mowers[0].y, final_mowers[0].orientation) == (1, 3, 'N')
        assert (final_mowers[1].x, final_mowers[1].y, final_mowers[1].orientation) == (5, 1, 'E')

    def test_out_of_bounds(self):

        # During this example, mowers will try to go out of bounds

        lawn_size = (3, 3)
        mowers = [
            Mower(
                lawn_size,
                (0, 1, 'W'),
                ["F", "R", "F"]
            ),
            Mower(
                lawn_size,
                (3, 3, 'E'),
                ["F", "R", "R"]
            )
        ]

        final_mowers = simulation.run(mowers)

        assert (final_mowers[0].x, final_mowers[0].y, final_mowers[0].orientation) == (0, 2, 'N')
        assert (final_mowers[1].x, final_mowers[1].y, final_mowers[1].orientation) == (3, 3, 'W')

    def test_concurrency(self):

        # During this example mowers will try to go on occupied positions
        # First mower 2 were mower 1 already is
        # Then mower 1 will want to move before mower 2 leaved the square free

        lawn_size = (3, 3)
        mowers = [
            Mower(
                lawn_size,
                (0, 3, 'N'),
                ["F", "F", "R", "F"]
            ),
            Mower(
                lawn_size,
                (2, 3, 'W'),
                ["F", "F", "L", "F"]
            )
        ]

        final_mowers = simulation.run(mowers)

        assert (final_mowers[0].x, final_mowers[0].y, final_mowers[0].orientation) == (0, 3, 'E')
        assert (final_mowers[1].x, final_mowers[1].y, final_mowers[1].orientation) == (1, 2, 'S')

    def test_inactive_mower(self):

        # Test that having no instructions doesn't crash the simulation
        # Also check that inactive mowers still occupy positions

        lawn_size = (2, 0)
        mowers = [
            Mower(
                lawn_size,
                (0, 0, 'S'),
                []
            ),
            Mower(
                lawn_size,
                (2, 0, 'W'),
                ["F", "F", "F"]
            )
        ]

        final_mowers = simulation.run(mowers)

        assert (final_mowers[0].x, final_mowers[0].y, final_mowers[0].orientation) == (0, 0, 'S')
        assert (final_mowers[1].x, final_mowers[1].y, final_mowers[1].orientation) == (1, 0, 'W')
