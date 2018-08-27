import random
def rand7():
    while True:
        # Do our die rolls
        roll1 = random.randint(0,6)
        roll2 = random.randint(0,6)
        outcome_number = (roll1 - 1)*5 + (roll2 - 1) + 1

        # If we hit an extraneous
        # outcome we just re-roll
        if outcome_number > 21:
            continue

        # Our outcome was fine. return it!
        return outcome_number % 7 + 1



print(rand7())