from fractions import Fraction

def solution(pegs):
    length = len(pegs)

    if (not pegs) or length == 1:
        return [-1, -1]

    even = True if length % 2 == 0 else False
    radius = -pegs[0] + pegs[length - 1] if even else -pegs[0] + -pegs[length - 1]

    for i in range(1, length - 1):
        radius += 2 * (-1) ** (i + 1) * pegs[i]

    radius = Fraction(2 * (radius / 3.0 if even else radius)).limit_denominator()

    if radius < 2:
        return [-1, -1]

    curr_radius = radius
    for i in range(0, length - 2):
        center_diff = pegs[i + 1] - pegs[i]
        next_radius = center_diff - curr_radius
        if curr_radius < 1 or next_radius < 1:
            return [-1, -1]
        else:
            curr_radius = next_radius

    return [radius.numerator, radius.denominator]
