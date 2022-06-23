"""
functions.py
Functions for the game.
"""

from typing import Tuple


def check_name(trial_name: str) -> Tuple[bool, str]:
    """
    Determine whether a proposed name is valid.

    Single names are OK, as are names with spaces.
    >>> check_name('Deedlit')
    (True, 'That is a good name!')
    >>> check_name('Raistlin Majere')
    (True, 'That is a good name!')

    Long and short names are not allowed.
    >>> check_name('thequickbrownfoxjumpedoverthelazydogs')
    (False, 'That name is too long!')
    >>> check_name('aa')
    (False, 'That name is too short!')

    Numbers and special characters are not allowed.
    >>> check_name('Elfy2')
    (False, 'Names can only contain letters and spaces!')
    >>> check_name('delete_all_data()')
    (False, 'Names can only contain letters and spaces!')
    """

    result = False
    if not all(c.isalpha() or c == " " for c in trial_name):
        message = "Names can only contain letters and spaces!"
    elif len(trial_name) < 3:
        message = "That name is too short!"
    elif len(trial_name) > 20:
        message = "That name is too long!"
    else:
        result = True
        message = "That is a good name!"

    return result, message
