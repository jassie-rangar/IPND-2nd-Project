ques = [["__1__ is the oldest democracy of the World.\n__2__ is the fastest animal on the land.\n__3__ is the longest river on earth.\n__4__ is the nearest star to planet earth.",['britain','cheetah','nile','sun']],
       ["Light travel fastest in __1__ .\n__2__ are the people and language of SriLnaka.\n__3__ is the full form of SEALs(the US millitary special operations force).\n__4__ is the largest Gurudwara of india.",['vaccum','sinhalese','sea air land','golden temple']],
       ["East India Company came into existance when England was ruled by __1__.\n__2__ was the first Governal-Genral of Bengal.\n__3__ was the first english newspaper of India.\n__4__ introduced Englisg as a official language in India.",['normans','warren hastings','the bengal gazette','sir charles wood']]]

def choose_level():
    level = int(raw_input(" "*11+"Select the level\n  "+ " "*9 +"Enter 1 ==== EASY\n  "+ " "*9 +"Enter 2 ==== MEDIUM\n  "+ " "*9 +"Enter 3 ==== HARD\n"))
    return level-1
    #because complire will take 1 as input and in return will give us 2 as output but we want it to start from 1 thats why level-1 = 1-1 = 0.

def replace_word(question,answer_list,answer_index):
    toReplace = "__"+str(answer_index+1)+"__"
    question = question.replace(toReplace,answer_list[answer_index])
    #this function will replace the blank spaces with the correct answer from the list of answers and even replace the with proper index to avoid any error.
    return question

def right_ans():
    print("\n wohoo!! Right Answer!! :) \n")
    # if answer will be correct then it will print whoo!! Right Answer!! :) as output.

def wrong_ans():
    print("\n ohoo..! Wrong Answer!! :( \n")
    print("\n lets try one more time!! :) \n")
    # if answer will be incorrext then it will print ohoo..! Wrong Answer!! :( as output and will suggest to try again.

def check_answer(user_input,answer_list,answer_index):
    if user_input == answer_list[answer_index]:
        return True
    return False
    #if the answer given by user matches the answer given in answer list then it will return true else will return false.

def question_quiz(answer_index):
    print("\n\nWhat should be in  "+"__"+ str(answer_index +1)+"__ ?")
    return raw_input("\n")
    #this is asigning the answer given by user in string.


def play_game():
    print ("\n")
    print(" "*10+"Welcome to the Genral Knowledge Quiz !!\n\n")
    #this will be displayed as welcome message to the user
    level = choose_level()
    answer_index = 0
    question = ques[level][0]
    answer_list = ques[level][1]
    #print(answer_list[answer_index])
    question_limit = 4
    while answer_index < question_limit:
        print(question)
        user_input = question_quiz(answer_index)
        if check_answer(user_input,answer_list,answer_index):
            question = replace_word(question,answer_list,answer_index)
            answer_index += 1
            right_ans()
        else:
            wrong_ans()
play_game()
