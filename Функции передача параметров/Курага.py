def dried_apricots(new: list) -> None:
    for item in range(len(new)):
        if new[item] <= apricots[item] / 2:
            apricots[item] = 0
        elif new[item] > apricots[item]:
            apricots[item] = new[item]