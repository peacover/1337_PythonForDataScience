def ErrorHandlingBMI(height, weight):
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
    if not isinstance(bmi, list):
        return print("ARG IS NOT A LIST!")
    elif not isinstance(limit, int):
        return print("LIMIT IS NOT AN INTEGER!")
    else:
        for item in bmi:
            if not (isinstance(item, int) |  isinstance(item, float)):
                return print("LIST IS NOT VALID!")
    return True

def give_bmi(height: list[int | float], weight: list[int | float]):
    # BMI = weight (kg) / (height (m) ^ 2)
    if ErrorHandlingBMI(height, weight):
        return [weight[index] / (height[index] ** 2) for index in range(0, len(height))]


def apply_limit(bmi: list[int | float], limit: int):
    if ErrorHandlingApplyLimit:
        return [True if item > limit else False for item in bmi]
    
# height = [2.71, 1.15]
# weight = [165.3, 38.4]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))