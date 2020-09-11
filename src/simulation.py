import os
import logging

def run(mowers, verbose_enabled=False):

    for current_tick in range(0, max([len(mower.instructions_queue) for mower in mowers])):

        # Only run mowers with instructions left
        running_mowers = [mower for mower in mowers if len(mower.instructions_queue) > current_tick]

        # TODO: Add parallelization
        # Executing a new step for every mower
        for mower in running_mowers:
            mower.tick(current_tick)

        # After every mower has done executing its step
        # Verify the desired moves of the mowers and resolve the conflicts
        for mower in mowers:
            if(mower.wants_to_move):
                if((mower.desired_x, mower.desired_y) not in [(mower.x, mower.y) for mower in mowers]):
                    mower.resolve(True)
                else:
                    mower.resolve(False)

        # Printing tick status if verbose logging is enabled
        if(verbose_enabled):
            for i, mower in enumerate(mowers):
                logging.info(f"Tick n°{current_tick}")
                logging.info(f"\nRunning Mowers : {len([mower for mower in mowers if len(mower.instructions_queue) > current_tick])}")
                logging.info(f"Mower n°{i}")
                logging.info(f"Position: ({mower.x}, {mower.y}), Orientation: {mower.orientation}")

    return mowers
