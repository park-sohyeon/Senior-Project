def find_address(input_add):
    a = open("address/" + input_add + ".txt", "r", encoding="utf-8")
    selected_address = a.readline().split(",")
    return selected_address