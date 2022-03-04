"""Exercise 4: Extract Variable (alias introduce explaining variable)"""

WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05


def is_cooking_criteria_satisfied(time, temperature, pressure, desired_state):
    amount_cooked = time * temperature * pressure * COOKED_CONSTANT
    desires_well_done = desired_state == 'well-done'
    desires_medium = desired_state == 'medium'
    is_well_done = amount_cooked > WELL_DONE
    is_medium = amount_cooked > MEDIUM

    if desires_well_done and is_well_done:
        return True
    if desires_medium and is_medium:
        return True
    return False
