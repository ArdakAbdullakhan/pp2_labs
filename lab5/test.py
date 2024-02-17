import re

def snake_to_camel(snake_str):
    # Use regex to split the snake case string into words
    words = snake_str.split('_')
    
    # Capitalize the first letter of each word except the first one
    camel_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    
    # Join the words to form the camel case string
    camel_str = ''.join(camel_words)
    
    return camel_str

# Test the function
snake_case_string = "snake_case_example_string"
camel_case_string = snake_to_camel(snake_case_string)
print("Snake case string:", snake_case_string)
print("Camel case string:", camel_case_string)
