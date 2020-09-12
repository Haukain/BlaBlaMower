# Storing the available orientations  and the delta they would apply in the clockwise order
AVAILABLE_DIRECTIONS = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
# Storing only the orientations in the clockwise order
AVAILABLE_ORIENTATIONS = list(AVAILABLE_DIRECTIONS)
# Available instructions for the mowers (forward, left and right)
AVAILABLE_INSTRUCTIONS = ["F", "L", "R"]


# Get the next element in a list given an element e
# If e is the last element, return the first one
def next_element(list, e):
    element_index = list.index(e)
    new_index = (element_index + 1) % len(list)
    return list[new_index]


# Get the previous element in a list given an element e
# If e is the first element, return the last one
def previous_element(list, e):
    element_index = list.index(e)
    new_index = (element_index - 1) % len(list)
    return list[new_index]
