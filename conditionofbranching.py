def determine_grade(score):
    if 90 <= score <= 100:
        return "A", "Very Good"
    
    if 80 <= score <= 89:
        return "B", "Good"
    
    if 70 <= score <= 79:
        return "C", "Great"
    
    if 60 <= score <= 69:
        return "D", "Study More"
    
    return "E", "Not PASS"  


score = 20
grade, predicate = determine_grade(score)
print(f"Score: {score}, Grade: {grade}, Predicate: {predicate}")
