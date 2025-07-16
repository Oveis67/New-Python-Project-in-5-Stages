
# First we can define calc average function

def calc_average(scores):
    average = sum(scores) / len(scores)
    return average

# Then we should define determine grade function

def determine_grade(scores):
    if 90 <= scores <= 100:
        return "A"
    elif 80 <= scores <= 90:
        return "B"
    elif 70 <= scores < 80:
        return "C"
    elif 60 <= scores < 70:
        return "D"
    else: 
        return "F"

# so define the main function for loop

def main():
    scores = []
    for i in range(5): 
        score = float(input(f"Enter your score {i+1}: "))
        scores.append(score)
    
    i = 1
    for score in scores:
        grade = determine_grade(score)
        print(f"Score {i}:{score} - Grade: {grade}")
        i += 1

# finally print the Average score and grade 

    average = calc_average(scores)
    determine_grade_average = determine_grade(average)
    print(f"Avrege score: {average} Grade:{determine_grade_average}")


# and call the main function 

main()





# Thanks Charlie
# Best Regards
# Oveis Bagheri