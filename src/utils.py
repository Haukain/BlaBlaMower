AVAILABLE_DIRECTIONS = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
AVAILABLE_ORIENTATIONS = list(AVAILABLE_DIRECTIONS)
AVAILABLE_INSTRUCTIONS = ["F", "L", "R"]


def next_element(list, e):
    element_index = list.index(e)
    new_index = (element_index + 1) % len(list)
    return list[new_index]


def previous_element(list, e):
    element_index = list.index(e)
    new_index = (element_index - 1) % len(list)
    return list[new_index]
