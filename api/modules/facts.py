import random       

#   function to get all facts
def get_facts():                                                    
    facts_stripped = []                                             # creating empty list

    try:
        with open('api/resources/facts.txt', 'r') as facts_file:    # opening facts file
            facts_stripped = [line.strip() for line in facts_file]  # adding stripped line to list

    #handling exceptions
    except FileNotFoundError:                                   
        return "Failed to get facts"
    except Exception as e:
        return f"Unknown error: {e}" 

    return facts_stripped                                           # returning facts

#   funtion to get random fact
def get_random_fact():
    facts = get_facts()                                             # getting all facts as a list
    random_fact = random.choice(facts)                              # getting random fact

    return random_fact                                              # returning random fact