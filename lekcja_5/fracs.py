import math


def add_frac(frac1, frac2):  # frac1 + frac2frac2[0]
    frac1 = prepare_for_actions(frac1)
    frac2 = prepare_for_actions(frac2)
    denominator_1 = frac1[1]
    denominator_2 = frac2[1]
    if denominator_1 == 0:
        return frac2
    if denominator_2 == 0:
        return frac1
    if denominator_1 != denominator_2:
        frac1 = turn_to_shared_denominator(frac1, denominator_2)
        frac2 = turn_to_shared_denominator(frac2, denominator_1)
    return turn_to_lowest([frac1[0] + frac2[0], frac1[1]])


def sub_frac(frac1, frac2):  # frac1 - frac2
    frac1 = prepare_for_actions(frac1)
    frac2 = prepare_for_actions(frac2)
    denominator_1 = frac1[1]
    denominator_2 = frac2[1]
    if denominator_1 == 0:
        return [-frac2[0], frac2[1]]
    if denominator_2 == 0:
        return frac1
    if denominator_1 != denominator_2:
        frac1 = turn_to_shared_denominator(frac1, denominator_2)
        frac2 = turn_to_shared_denominator(frac2, denominator_1)
    return turn_to_lowest([frac1[0] - frac2[0], frac1[1]])


def mul_frac(frac1, frac2):  # frac1 * frac2
    frac1 = prepare_for_actions(frac1)
    frac2 = prepare_for_actions(frac2)
    return turn_to_lowest([frac1[0] * frac2[0], frac1[1] * frac2[1]])


def div_frac(frac1, frac2):  # frac1 / frac2
    frac1 = prepare_for_actions(frac1)
    frac2 = prepare_for_actions(frac2)
    return turn_to_lowest([frac1[0] * frac2[1], frac2[0] * frac1[1]])


def is_positive(frac):  # bool, czy dodatni
    frac = prepare_for_actions(frac)
    return frac[0] * frac[1] > 0


def is_zero(frac):  # bool, typu [0, x]
    if frac[0] == 0:
        return True
    return False


def cmp_frac(frac1, frac2):  # -1 | 0 | +1
    frac1 = prepare_for_actions(frac1)
    frac2 = prepare_for_actions(frac2)
    denominator_1 = frac1[1]
    denominator_2 = frac2[1]
    if denominator_1 != denominator_2 and denominator_1 != 0 and denominator_2 != 0:
        frac1 = turn_to_shared_denominator(frac1, denominator_2)
        frac2 = turn_to_shared_denominator(frac2, denominator_1)

    if frac1[0] > frac2[0]:
        return -1
    if frac1[0] < frac2[0]:
        return 1
    return 0


def frac2float(frac):
    if frac[0] == 0:
        return 0
    frac = prepare_for_actions(frac)
    return float(frac[0] / frac[1])


def turn_to_shared_denominator(frac1, frac2):
    return [frac1[0] * frac2, frac1[1] * frac2]


def prepare_for_actions(frac):
    is_denominator_zero(frac)
    return turn_to_lowest(frac)


def is_denominator_zero(frac):
    if frac[1] == 0:
        raise NameError("Denominator cannot be 0.")


def turn_to_lowest(frac):
    if is_zero(frac):
        return [0, 0]
    lowest = math.gcd(int(frac[0]), int(frac[1]))
    if lowest == 1:
        return frac
    return [frac[0] / lowest, frac[1] / lowest]
