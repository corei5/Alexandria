import pandas as pd
import numpy as np
from scripts.multiple_choice_question import generate_multiple_choice_question
from scripts.extract_answers import answer_questions
from scripts.equalize_list_length import equalize_list_lengths


def evaluate_answers_(correct_answers, received_answers):
    print("...............yes,evaluate_answers_is_calling ..............")
    # print(correct_answers)
    # print(".....................received_answers..........")
    # print(received_answers)
    """
    Compares the received answers with the correct answers and returns a score as a percentage.

    Parameters:
    - correct_answers (List[str]): The correct answers.
    - received_answers (List[str]): The answers received from the answering function.

    Returns:
    - float: The percentage of correct answers.
    """
    correct_answer_count = 0
    for i, answer in enumerate(correct_answers):
        if answer == received_answers[i]:
            correct_answer_count += 1
    try:
        # Calculate the percentage of correct answers
        percentage_correct = (correct_answer_count / len(correct_answers)) * 100
    except ZeroDivisionError:
        # Return None if division by zero occurs (empty correct_answers list)
        percentage_correct = None
    return percentage_correct


def evaluate_peformance(df, number_of_questions, file_name_save_questions):
    input_texts = df["Input_Texts"].tolist()
    knowledgegraphs = df["Output_Graphs"].tolist()
    reconstructed_texts = df["Output_Reconstructions"].tolist()

    base_caps = []
    original_caps = []
    knowledgegraph_caps = []
    reconstruction_caps = []

    Try_up_to = 3

    text_questions_answers_dict_list=[]
    for i in range(len(input_texts)):
        for _ in range(Try_up_to):  # Try up to 3 times
            try:
                questions, correct_answers = generate_multiple_choice_question(input_texts[i], number_of_questions)
                print("questions, correct_answers ", questions, correct_answers )
                text_questions_answers_dict={}
                text_questions_answers_dict["text"]=input_texts[i]
                text_questions_answers_dict["kg"]=knowledgegraphs[i]
                text_questions_answers_dict["reconstruction"]=reconstructed_texts[i]
                text_questions_answers_dict["questions"]= questions
                text_questions_answers_dict["correct_answers"]= correct_answers
                text_questions_answers_dict_list.append(text_questions_answers_dict )
                break  # If successful, break the loop
            except Exception as e:
                print(f"Error generating questions for sample {i}: {e}")
    df = pd.DataFrame({
        'text_questions_answers_dicts': text_questions_answers_dict_list,
    })

    #df.to_parquet(file_name_save_questions, row_group_size=1000)
    #df.to_csv("dataset/questions_answer_save.csv", encoding='utf-8', index=False)



    for i in range(len(text_questions_answers_dict_list)):
        
        #print("text_questions_answers_dict_list[i]",text_questions_answers_dict_list[i])
        
        for j in range(Try_up_to):  # Try up to 3 times
            try:
                #print(str(j)+". try no context")
                no_context_answers = answer_questions(text_questions_answers_dict_list[i]["questions"], None)
                #print("no_context_answers", no_context_answers)
                break  # If successful, break the loop
            except Exception as e:
                print(f"Error getting no context answers for sample {i}: {e}")

        for j in range(Try_up_to):  # Try up to 3 times
            try:
                #print(str(j)+". try original context")
                original_context_answers = answer_questions(text_questions_answers_dict_list[i]["questions"], text_questions_answers_dict_list[i]["text"])
                #print("original_context_answers", original_context_answers)
                break  # If successful, break the loop
            except Exception as e:
                print(f"Error getting original context answers for sample {i}: {e}")

        for j in range(Try_up_to):  # Try up to 3 times
            try:
                #print(str(j)+". try kg context")
                knowledgegraph_context_answers = answer_questions(text_questions_answers_dict_list[i]["questions"], text_questions_answers_dict_list[i]["kg"])
                #print("knowledgegraph_context_answers", knowledgegraph_context_answers)
                break  # If successful, break the loop
            except Exception as e:
                print(f"Error getting knowledge graph context answers for sample {i}: {e}")

        for j in range(Try_up_to):  # Try up to 3 times
            #try:
            #print(str(j)+". try reconstruction context")
            reconstruction_context_answers = answer_questions( text_questions_answers_dict_list[i]["questions"], text_questions_answers_dict_list[i]["reconstruction"])
            #print("reconstruction_context_answers", reconstruction_context_answers)

            break  # If successful, break the loop
            #except Exception as e:
            #    print(f"Error getting reconstruction context answers for sample {i}: {e}")

        # make sure correct answers and returned answers are of same len
        #print(text_questions_answers_dict_list[i]["correct_answers"])

        correct_answers_short, no_context_answers_short = equalize_list_lengths(text_questions_answers_dict_list[i]["correct_answers"], no_context_answers)
        #print("correct_answers_short, no_context_answers_short", correct_answers_short, no_context_answers_short)
        
        print("....................correct_answers_short............")
        print(correct_answers_short)
        
        base_cap = evaluate_answers_(correct_answers_short, no_context_answers_short)

        print("....................base_cap......................")
        print(base_cap)

        correct_answers_short, original_context_answers_short = equalize_list_lengths(text_questions_answers_dict_list[i]["correct_answers"], original_context_answers)
        print("correct_answers_short, original_context_answers_short", correct_answers_short, original_context_answers_short)
        original_cap = evaluate_answers_(correct_answers_short, original_context_answers_short)

        correct_answers_short, knowledgegraph_context_answers_short = equalize_list_lengths(text_questions_answers_dict_list[i]["correct_answers"], knowledgegraph_context_answers)
        print("correct_answers_short, knowledgegraph_context_answers_short", correct_answers_short, knowledgegraph_context_answers_short)
        knowledgegraph_cap = evaluate_answers_(correct_answers_short, knowledgegraph_context_answers_short)

        correct_answers_short, reconstruction_context_answer_short = equalize_list_lengths(text_questions_answers_dict_list[i]["correct_answers"], reconstruction_context_answers)
        print( "correct_answers_short, reconstruction_context_answer_short",  correct_answers_short, reconstruction_context_answer_short )
        reconstruction_cap = evaluate_answers_(correct_answers_short, reconstruction_context_answer_short)

        base_caps.append(base_cap)
        original_caps.append(original_cap)
        knowledgegraph_caps.append(knowledgegraph_cap)
        reconstruction_caps.append(reconstruction_cap)

    # Remove None values from lists
    base_caps = [x for x in base_caps if x is not None]
    original_caps = [x for x in original_caps if x is not None]
    knowledgegraph_caps = [x for x in knowledgegraph_caps if x is not None]
    reconstruction_caps = [x for x in reconstruction_caps if x is not None]

    # Calculate mean, return 0 if no elements left
    base_cap = np.mean(base_caps) if base_caps else 0
    original_cap = np.mean(original_caps) if original_caps else 0
    knowledgegraph_cap = np.mean(knowledgegraph_caps) if knowledgegraph_caps else 0
    reconstruction_cap = np.mean(reconstruction_caps) if reconstruction_caps else 0

    return base_cap, original_cap, knowledgegraph_cap, reconstruction_cap, df



