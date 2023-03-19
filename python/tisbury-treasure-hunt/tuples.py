"""Functions to help Azara and Rui locate pirate treasure."""

from typing import Tuple, Union

RuiRecord = Tuple[str, Tuple[str, str], str]

def get_coordinate(record: Tuple[str, str]) -> str:
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


#def convert_coordinate(coordinate: str) -> Tuple[str, ...]: #number of items in a tuple type hint flexible:
def convert_coordinate(coordinate: str) -> Tuple[str, str]:
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return (coordinate[0], coordinate[1])
    #return tuple(coordinate)


def compare_records(azara_record: Tuple[str, str], rui_record: RuiRecord) -> bool:
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    return azara_record[1] == ''.join(rui_record[1])


def create_record(azara_record: Tuple[str, str], rui_record: RuiRecord) -> Union[tuple, str]:
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if azara_record[1] == ''.join(rui_record[1]):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group: tuple) -> str:
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).

    Clean up the combined records from Azara and Rui so that there's only one set of
    coordinates per record. Make a report so they can see one list of everything they
    need to put on their maps. Implement the clean_up() function that takes a
    tuple of tuples (everything from both lists), looping through the outer tuple,
    dropping the unwanted coordinates from each inner tuple and adding each to a 'report'.
    Format and return the 'report' so that there is one cleaned record on each line.
    """

    return ''.join([f'{(t[0],) + t[2:]}\n' for t in combined_record_group])
