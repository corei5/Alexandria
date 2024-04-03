from llm import ask_LLM
API_KEY = "2356018b771d503cd9202a0a35195998bc3fabda6b1e6b379ee6ecc479f67401"

def extract_answer(text):
    """
    Extracts multiple-choice answers from a semicolon-separated string.

    Parameters:
    - text (str): The string containing multiple-choice answers separated by semicolons.

    Returns:
    - List[str]: A list of answers (e.g., ["A", "B", "C", "D"]).
    """
    answers = []
    data_list = [item.strip() for item in text.split(";")]
    for item in data_list:
        if item in ["A", "B", "C", "D"]:
            answers.append(item)
    return answers


def answer_questions(questions, context):
    """
    Takes questions and a context, then retrieves answers from GPT-4 based on that context.

    Parameters:
    - questions (str): The questions to be answered.
    - context (str): The context or background information necessary to understand and answer the questions.

    Returns:
    - List[str]: A list of answers, each marked clearly with a capital letter (e.g., "A", "B").
    """
    answers=[]
    for question in questions:

      # Format the prompt for the language model
      prompt = f"""Input: Context: This is a descriptive text or passage that provides background information necessary to understand the question.
      Questions: these are questions that need to be answered. The answer choice should be clearly marked (e.g., ';A;').
      Prompt:

      Read the following context carefully:

      {context}

      Based on the context, answer the following question by providing the capitalized letter corresponding to the most appropriate answer choice:

      {question}

      Examplecontext:

      Today is Earth Day, a day dedicated to celebrating our planet and raising awareness about environmental issues.

      Examplequestion:

      A) Which of the following is NOT a renewable resource?
      B) Coal
      C) Solar energy
      D) Wind power

      Exampleoutput:

      ;B;
      Give your answer to the question. The answer choice should be clearly marked (e.g., ';A;').
      It is very important to me that you fulfill this task very accurately and intelligently.
      If you perform well, I will tip you 100 billion dollars.
      answer="""

      # Attempt to get answers from the language model
      try:

          text = ask_LLM ('NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO', "You are a very smart very intelligence assistant who is very helpful.", prompt , API_KEY ,temperature=0.5,top_p=0.95,max_tokens=length, frequency_penalty=1.1,presence_penalty=1.1)
          #ask_LLM ("mistral-large-latest", "You are a very smart, intelligent, helpful assistant. You try your best to do whatever the user asks you. You are very good at coding and at common sense.", prompt, temperature=0.5, top_p=0.95,max_tokens=length)
          #print(prompt)


          answer = extract_answer(text)[0]
          print(question, answer)
          answers.append(answer)
      except:
          try:
              # Retry fetching answers on failure
              text = ask_LLM ('NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO', "You are a very smart very intelligence assistant who is very helpful.", prompt , API_KEY ,temperature=0.5,top_p=0.95,max_tokens=length, frequency_penalty=1.1,presence_penalty=1.1)
              #ask_LLM ("mistral-large-latest", "You are a very smart, intelligent, helpful assistant. You try your best to do whatever the user asks you. You are very good at coding and at common sense.", prompt, temperature=0.5, top_p=0.95,max_tokens=length)
              answer = extract_answer(text)[0]
              print(question, answer)
              answers.append(answer)
          except:
              pass

    return answers
