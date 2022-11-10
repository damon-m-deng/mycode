#!/usr/bin/env python3

import html

def main():
    
    trivia= {
            "category": "Entertainment: Film",
            "type": "multiple",
            "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
            "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
            "incorrect_answers": [
                "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
                "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
                "&quot;Round up the usual suspects.&quot;"
                ]
            }

    correct = html.unescape(trivia['correct_answer'])
    incorrect1 = html.unescape(trivia['incorrect_answers'][0])
    incorrect2 = html.unescape(trivia['incorrect_answers'][1])
    incorrect3 = html.unescape(trivia['incorrect_answers'][2])
    
    while True:
        answer = input(trivia['question']+'\n'+"A. "+incorrect1+'\n'+"B. "+incorrect3+'\n'+"C. "+correct+'\n'+"D. "+incorrect2+'\n')
        if(answer == 'A'):
            print("correct!")
            break
        else:
            print("wrong, try again.")

if __name__ == "__main__":
    main()
