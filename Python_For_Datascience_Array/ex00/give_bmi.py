def ErrorHandlingBMI(height, weight):
    """Validate inputs for the give_bmi function.

    Checks that height and weight are lists of int/float
    with the same length.
    Returns True if valid, otherwise prints an error message.
    """
    if not isinstance(height, list):
        return print("ARG IS NOT A LIST!")
    else:
        for item in height:
            if not (isinstance(item, int) | isinstance(item, float)):
                return print("HEIGHT LIST NOT VALID!")
        for item in weight:
            if not (isinstance(item, int) | isinstance(item, float)):
                return print("WEIGHT LIST NOT VALID!")
        if len(height) != len(weight):
            return print("THE LIST ARE NOT THE SAME SIZE!")
    return True


def ErrorHandlingApplyLimit(bmi, limit):
    """Validate inputs for the apply_limit function.

    Checks that bmi is a list of int/float and limit is an int.
    Returns True if valid, otherwise prints an error message.
    """
    if not isinstance(bmi, list):
        return print("ARG IS NOT A LIST!")
    elif not isinstance(limit, int):
        return print("LIMIT IS NOT AN INTEGER!")
    else:
        for item in bmi:
            if not (isinstance(item, int) | isinstance(item, float)):
                return print("LIST IS NOT VALID!")
    return True


def give_bmi(height: list[int | float], weight: list[int | float]):
    """Calculate BMI from height and weight lists.

    BMI = weight (kg) / (height (m) ^ 2).
    Returns a list of BMI values.
    """
    # BMI = weight (kg) / (height (m) ^ 2)
    if ErrorHandlingBMI(height, weight):
        return [weight[index] / (height[index] ** 2)
                for index in range(0, len(height))]


def apply_limit(bmi: list[int | float], limit: int):
    """Apply a BMI limit and return a list of booleans.

    Returns True for each BMI value above the limit, False otherwise.
    """
    if ErrorHandlingApplyLimit:
        return [True if item > limit else False for item in bmi]

# height = [2.71, 1.15]
# weight = [165.3, 38.4]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))
