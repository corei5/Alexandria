from scripts.llm import ask_LLM
from scripts.split_questions_and_answers import split_to_questions_and_answers
import scripts.prompts

API_KEY = "2356018b771d503cd9202a0a35195998bc3fabda6b1e6b379ee6ecc479f67401"
length = 4000

def generate_multiple_choice_question(text, number_of_questions):
    """
    Defines a function to generate multiple-choice questions from a text passage. It formats a prompt for an AI model,
    instructing it to produce multiple-choice questions similar to a provided example, based on the given text and number of questions.

    Parameters:
    - text (str): The text to analyze and create questions from.
    - number_of_questions (int): How many multiple-choice questions to generate.

    Returns:
    - Tuple[List[str], List[str]]: A tuple of two lists - one for questions and one for answers.
    """

    # Setting up the prompt for generating questions
    prompt = scripts.prompts.generate_multiple_choice_question_prompts(text, number_of_questions)
    # Assuming `ask_LLM` is a predefined function that sends the prompt to a language model and receives generated text.
    #print(prompt)
    questions_and_answers =  ask_LLM ('NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO', "You are a very smart very intelligence assistant who is very helpful.", prompt , API_KEY ,temperature=0.5,top_p=0.95,max_tokens=length, frequency_penalty=1.1,presence_penalty=1.1)
    #ask_LLM ("mistral-large-latest", "You are a very smart, intelligent, helpful assistant. You try your best to do whatever the user asks you. You are very good at coding and at common sense.", prompt, temperature=0.5, top_p=0.95,max_tokens=length)
    #print(".......................Print question and answer...............")
    #print(questions_and_answers)
    try:
        # Try to split the generated text into questions and their answers
        questions, answers = split_to_questions_and_answers(questions_and_answers)
        #print(questions, answers)

    except:
        try:
            # If splitting fails, retry the question generation and splitting process
            questions_and_answers =  ask_LLM ("mistral-large-latest", "You are a very smart, intelligent, helpful assistant. You try your best to do whatever the user asks you. You are very good at coding and at common sense.", prompt, temperature=0.5, top_p=0.95,max_tokens=length)

            questions, answers = split_to_questions_and_answers(questions_and_answers)
            #print(questions, answers)
        except:
            # If it fails again, return empty lists
            #print("....................I failed............")
            return [], []
    #print(questions, answers)

    # Check if the numbers of questions and answers match, adjust if necessary
    if len(questions) == len(answers):
        return questions, answers
    elif len(questions) < len(answers):
        return questions, answers[:len(questions)]
    elif len(questions) > len(answers):
        return questions[:len(answers)], answers
