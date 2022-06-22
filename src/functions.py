def check_name(trial_name: str) -> bool:
    """
    Determine whether a proposed name is valid.

    Single names are OK, as are names with spaces.
    >>> check_name("Deedlit")
    True
    >>> check_name("Raistlin Majere")
    True

    Long and short names are not allowed.
    >>> check_name("thequickbrownfoxjumpedoverthelazydogs")
    False
    >>> check_name("aa")
    False

    Numbers are not allowed.
    >>> check_name("Elfy2")
    False

    Special characters are not allowed.
    >>> check_name("delete_all_data()")
    False
    """
    return (
        isinstance(trial_name, str)
        and all(c.isalpha() or c == " " for c in trial_name)
        and 3 <= len(trial_name) <= 20
    )
