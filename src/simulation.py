import logging
from multiprocessing import Process, Queue

from src.Mower import Mower


# Function executing the lifecycle of a mower
def mower_process(mower, out_queue, in_queue):

    max_tick = len(mower.instructions_queue)
    # Loop until the end of the instructions
    for current_tick in range(0, max_tick):
        # Execute a new instruction
        mower.tick(current_tick)
        # Notify the main process that we executed our step
        out_queue.put((mower.wants_to_move, mower.desired_x, mower.desired_y, mower.orientation))
        # Resolve using the permission sent by the main process
        permission = in_queue.get()
        mower.resolve(permission)


# Run a new simulation
def run(lawn_size, mowers_configs, verbose_enabled=False):

    # To enable the multiprocessing of mowers we have to create one process per mower
    mower_processes = []
    for i in range(len(mowers_configs)):
        # Create a queue carrying message from the mower process to the main process
        process_to_main_queue = Queue()
        # Create a queue carrying message from the main process to the mower process
        main_to_process_queue = Queue()
        # Create a mower object from the configuration
        mower = Mower(lawn_size, mowers_configs[i][0], mowers_configs[i][1])
        # Spawn a process executing the mower_process function
        process = Process(target=mower_process, args=(mower, process_to_main_queue, main_to_process_queue))
        mower_processes.append((process_to_main_queue, main_to_process_queue, process))

        process.start()

    # Store the current status of all the mowers [total_number_of_instructions, x_position, y_position, orientation]
    current_mower_status = [[len(mower_config[1]), mower_config[0][0], mower_config[0][1], mower_config[0][2]] for mower_config in mowers_configs]

    # Loop until the max number of instructions
    for current_tick in range(0, max([mower_status[0] for mower_status in current_mower_status])):

        # Log current step info if verbose enabled
        if(verbose_enabled):
            logging.info(f"\nTick n°{current_tick}")
            logging.info(f"Running Mowers : {len([mower_status for mower_status in current_mower_status if current_tick < current_mower_status[i][0]])}")
            for i, mower_status in enumerate(current_mower_status):
                logging.info(f"Mower n°{i}")
                logging.info(f"Position: ({mower_status[1]}, {mower_status[2]}), Orientation: {mower_status[3]}")

        # Loop on every mower to resolve to resolve conflicts
        # Priority for conflict resolution is done following the order in which the mower are declared in the config file
        for i, process in enumerate(mower_processes):
            # If the mower still has instructions to execute
            if(current_tick < current_mower_status[i][0]):
                # Read its queue to get the results of the last instruction
                wants_to_move, desired_x, desired_y, orientation = process[0].get()
                current_mower_status[i][3] = orientation
                permission = False
                # The mower is allowed to move only if it wants to move and the desired position is not occupied
                if(wants_to_move):
                    if((desired_x, desired_y) not in [(status[1], status[2]) for status in current_mower_status]):
                        current_mower_status[i][1] = desired_x
                        current_mower_status[i][2] = desired_y
                        permission = True
                # Send permission status to the mower
                process[1].put(permission)

    # Close the queue and end the processes
    for process in mower_processes:
        process[0].close()
        process[1].close()
        process[2].join()

    # Send back the results of the simulation
    final_mower_status = [(mower_status[1], mower_status[2], mower_status[3]) for mower_status in current_mower_status]
    return final_mower_status
