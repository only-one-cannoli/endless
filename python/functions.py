def check_name(trial_name: str) -> bool:
    return (
        isinstance(trial_name, str)
        and all(c.isalpha() or c == " " for c in trial_name)
        and len(trial_name) <= 15
    )
