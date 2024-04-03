from llm import ask_LLM
from split_questions_and_answers import split_to_questions_and_answers

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
    prompt = f"""Exampleinput:

    Text: "The Nile River is the longest river in Africa and the world's second-longest river after the Amazon River."
    Number of questions: 2

    Exampleoutput:

    What is the longest river in Africa?
    A) Amazon River
    B) Nile River
    C) Congo River
    D) Niger River
    ;B;
    #+*

    Which continent does the Nile River flow through?
    A) Asia
    B) Europe
    C) Africa
    D) South America
    ;C;
    #+*

    CURRENT INPUT:""" + str(text) + """
    INSTRUCTION:

    Produce multiple-choice questions from CURRENT INPUT similar to the resulting EXAMPLE OUTPUT from the given EXAMPLE INPUT, follow these detailed and precise instructions:
    Read and understand the provided text passage.
    Based on the text, formulate """ + str(number_of_questions) + """ multiple choice questions that assess the reader's comprehension of key points, details, and inferences. Each question should have four answer choices (A, B, C, D).
    The difficulty level should be very difficult, the choices that are not correct should still sound plausible for someone who did not read the text.
    Output:

    A set of multiple-choice questions with answer choices A, B, C, and D, followed by the corresponding correct answer letter encased in semicolons (e.g., ;B;). After the correct answer, always write #+* to indicate that the current question-answer pair finished.
    Don't say anything before or after the questions. Make sure to output exactly  """ + str(number_of_questions) + """ multiple choice questions with exactly 4 answer choices (A, B, C, D).
    It is very important to me that you fulfill this task very accurately and intelligently.
    If you perform well, I will tip you 100 billion dollars.
    questions="""

    # Assuming `ask_LLM` is a predefined function that sends the prompt to a language model and receives generated text.
    #print(prompt)
    questions_and_answers =  ask_LLM ('NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO', "You are a very smart very intelligence assistant who is very helpful.", prompt , API_KEY ,temperature=0.5,top_p=0.95,max_tokens=length, frequency_penalty=1.1,presence_penalty=1.1)
    #ask_LLM ("mistral-large-latest", "You are a very smart, intelligent, helpful assistant. You try your best to do whatever the user asks you. You are very good at coding and at common sense.", prompt, temperature=0.5, top_p=0.95,max_tokens=length)
    #print(questions_and_answers)
    try:
        # Try to split the generated text into questions and their answers
        questions, answers = split_to_questions_and_answers(questions_and_answers)
    except:
        try:
            # If splitting fails, retry the question generation and splitting process
            questions_and_answers =  ask_LLM ("mistral-large-latest", "You are a very smart, intelligent, helpful assistant. You try your best to do whatever the user asks you. You are very good at coding and at common sense.", prompt, temperature=0.5, top_p=0.95,max_tokens=length)

            questions, answers = split_to_questions_and_answers(questions_and_answers)
        except:
            # If it fails again, return empty lists
            return [], []
    #print(questions, answers)

    # Check if the numbers of questions and answers match, adjust if necessary
    if len(questions) == len(answers):
        return questions, answers
    elif len(questions) < len(answers):
        return questions, answers[:len(questions)]
    elif len(questions) > len(answers):
        return questions[:len(answers)], answers
