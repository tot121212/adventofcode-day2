def initialize_is_increasing(report : list[int]):
    print(report)
    if report[0] == report[1]: # base case essentially
        return None
    if report[0] < report[1]:
        return True
    if report[0] > report[1]:
        return False

def check_report_safety(report):
    is_increasing = initialize_is_increasing(report[:2])
    print("     is increasing initially: " + str(is_increasing))
    if is_increasing is None: # is not trending so its unsafe
        return False
    
    for index_of_level in range(1, len(report)): # check each level except first cuz were comparing with prev
        print("     index_of_level: " + str(index_of_level))
        level = report[index_of_level]
        prev_level = report[index_of_level - 1]

        print("     level: " + str(level) + " prev_level: " + str(prev_level))
        if level == prev_level:
            return False
        if abs(prev_level - level) > 3:
            return False
        if is_increasing and level < prev_level:
            return False
        elif not is_increasing and level > prev_level:
            return False
    return True

def main():
    reports = []

    with open("input.txt", "r") as file:
        lines = file.readlines()
        #reports.append([int(item) for item in lines[0].split(" ")])
        for line in lines:
            reports.append([int(item) for item in line.split(" ")])

    reports_safety = []

    for report in reports:
        print("report: " + str(report))
        is_report_safe = check_report_safety(report)
        print("     is report safe: " + str(is_report_safe))
        reports_safety.append(is_report_safe)

    print(reports_safety.count(True))

main()