import json
with open("data/quiz.json") as json_file:
    quiz = json.load(json_file)



# print(quiz)

# for quiz, all_data in quiz.items():
#     print()
#     for all_questions, all_q_data in all_data.items():
#         print()
#             for question, options in all_q_data():
#                 if question == "question":
#                     print(f"Question {all_questions}: {options}")
#                 elif question == "options":
#                     for choices in question:
#                         print(f"            {choice}")                        

    # for j in json_data[i]:
    #         print(json_data[i][j])



for quiz,questions in quiz.items():
    for number,whole in questions.items():
        for category,details in whole.items():
            if category == "question":
                print(f"Question {number}: {details}")
            elif category == "options":
                for i in details:
                    print(f"       {i}")
