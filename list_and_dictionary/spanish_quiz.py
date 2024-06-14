"""
File: spanish_quiz.py
---------------------
A simple dictionary practice which give user quiz to test their spanish
"""

def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    score = 0
    for key in translations:
        query = input(f"What is the Spanish translation for {key}? ")
        answer = translations[key]
        if (query == answer):
            print("That is correct!")
            score += 1
        else:
            print(f"That is incorrect, the Spanish translation for {key} is {answer}.")
        print("")
    print(f"You got {score}/{len(translations)} words correct, come study again soon!")
    
if __name__ == '__main__':
    main()