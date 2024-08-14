# Developed by Howard Nikhil
def determine_characteristics():
    # Welcome message to the user
    print("Welcome! Let's determine some simple psychological characteristics.")

    # Ask the user if they prefer spending time alone (Introvert) or with others (Extrovert)
    q1 = input("Do you prefer spending time alone (A) or with a group of people (B)? (A/B): ").strip().upper()
    if q1 == "A":
        personality_type = "Introvert"  # User prefers solitude
    else:
        personality_type = "Extrovert"  # User prefers being with others

    # Ask the user if they see the glass as half full (Optimistic) or half empty (Pessimistic)
    q2 = input("Do you usually see the glass as half full (A) or half empty (B)? (A/B): ").strip().upper()
    if q2 == "A":
        outlook = "Optimistic"  # User has a positive outlook
    else:
        outlook = "Pessimistic"  # User has a negative outlook

    # Ask the user if they make decisions with their head (Thinker) or heart (Feeler)
    q3 = input("Do you make decisions more with your head (A) or your heart (B)? (A/B): ").strip().upper()
    if q3 == "A":
        decision_making = "Thinker"  # User is more logical
    else:
        decision_making = "Feeler"  # User is more emotional

    # Ask the user if they prefer a structured plan (Structured) or going with the flow (Flexible)
    q4 = input("Do you prefer a structured plan (A) or going with the flow (B)? (A/B): ").strip().upper()
    if q4 == "A":
        planning_style = "Structured"  # User prefers planning
    else:
        planning_style = "Flexible"  # User prefers spontaneity

    # Ask the user if they focus on details (Detailed) or the big picture (Big Picture)
    q5 = input("Do you focus more on details (A) or the big picture (B)? (A/B): ").strip().upper()
    if q5 == "A":
        focus = "Detailed-oriented"  # User focuses on details
    else:
        focus = "Big-picture thinker"  # User focuses on the overall view

    # Summarize and print out the results based on the user's answers
    print("\nBased on your answers, here are your simple psychological characteristics:")
    print(f"1. Personality Type: {personality_type}")
    print(f"2. Outlook: {outlook}")
    print(f"3. Decision Making: {decision_making}")
    print(f"4. Planning Style: {planning_style}")
    print(f"5. Focus: {focus}")

# The main function to start the program
if __name__ == "__main__":
    determine_characteristics()
