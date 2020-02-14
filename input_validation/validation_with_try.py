def average(score1, score2, score3):
    NUMBER_TESTS = 3

    if score1 < 0 or score2 < 0:
        raise ValueError
    else :
        return float((score1 + score2 + score3) / NUMBER_TESTS)
