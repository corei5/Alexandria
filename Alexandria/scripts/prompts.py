#Zero-Shot Prompting - Done 
#Few-Shot Prompting (1-shot)
#Few-Shot Prompting (3-shot)
#Few-Shot Prompting (5-shot)
#Few-Shot Prompting (10-shot)
#Zero-shot COT Prompting - Done


def Zero_Shot_KG_reconstruction_prompt(reconstruction_so_far, current_kg):
    prompt = """RECONSTRUCTION SO FAR:
      """ + str(reconstruction_so_far) + """
      INPUT KNOWLEDGE GRAPH SEGMENT:
      """ + str(current_kg[-1]) + """
      INSTRUCTION:
      RECONSTRUCTION SO FAR is a written from a knowleade graph and the knowledge graph had been constructed from a original text. RECONSTRUCTION SO FAR aims to recrunstruct the original text as factual and authentic as possible.
      INPUT KNOWLEDGE GRAPH SEGMENT is a part of the knowledge graph that has not been integrated yet into RECONSTRUCTION SO FAR.
      Based on the information (facts and events) in INPUT KNOWLEDGE GRAPH SEGMENT, write me a well written, easily understandable, very accurate text about its contents, in a plausible order, manner and style. Be very factual and do not make up any new stuff. Write it in a manner, that it fits seamlessly as a continuation of RECONSTRUCTION SO FAR.

      Write <reconstruction> right in front of your output of the reconstruction and </reconstruction> at it's end.
      It is very important to me that you fulfill this task very very accurately and intelligently.
      If you perform well, i will tip you 100 billion dollars.

      """
    return prompt

def Few_1_Shot_KG_reconstruction_prompt(reconstruction_so_far, current_kg):
    pass
def Few_3_Shot_KG_reconstruction_prompt(reconstruction_so_far, current_kg):
    pass
def Few_5_Shot_KG_reconstruction_prompt(reconstruction_so_far, current_kg):
    pass
def Few_10_Shot_KG_reconstruction_prompt(reconstruction_so_far, current_kg):
    pass

def KG_reconstruction_prompt(reconstruction_so_far, current_kg):
    prompt = """RECONSTRUCTION SO FAR:
      """ + str(reconstruction_so_far) + """
      INPUT KNOWLEDGE GRAPH SEGMENT:
      """ + str(current_kg[-1]) + """
      INSTRUCTION:
      RECONSTRUCTION SO FAR is a written from a knowleade graph and the knowledge graph had been constructed from a original text. RECONSTRUCTION SO FAR aims to recrunstruct the original text as factual and authentic as possible.
      INPUT KNOWLEDGE GRAPH SEGMENT is a part of the knowledge graph that has not been integrated yet into RECONSTRUCTION SO FAR.
      Based on the information (facts and events) in INPUT KNOWLEDGE GRAPH SEGMENT, write me a well written, easily understandable, very accurate text about its contents, in a plausible order, manner and style. Be very factual and do not make up any new stuff. Write it in a manner, that it fits seamlessly as a continuation of RECONSTRUCTION SO FAR.

      Write <reconstruction> right in front of your output of the reconstruction and </reconstruction> at it's end.
      It is very important to me that you fulfill this task very very accurately and intelligently.
      If you perform well, i will tip you 100 billion dollars.

      Let's think step by step.
      """
    return prompt


def Zero_Shot_style_genre_prompt(input_text):
    prompt = """
      INSTRUCTION:
  Perform a succinct yet thorough analysis (50 to 200 words) of the text’s writing style, rhythm, genre, and more, carefully considering the distinctive features that typify its literary and communicative approach. Reflect on the following aspects:

  Format and Genre: How does the text situate itself within specific genres or sub-genres such as epic, tragedy, comedy, tragicomedy, mystery, thriller, horror, romance, speculative fiction (including fantasy, science fiction, and dystopian), magical realism, young adult (YA), children’s literature, flash fiction, creative nonfiction, biographical works, poetry (sonnet, haiku, free verse), historical narrative, legal or medical analysis, academic journal, self-help, how-to guides, or culinary reviews?
  Writing Style: Which terms best describe the text's style? Is it formal, informal, academic, conversational, ornate, sparse, lyrical, dry, satirical, or colloquial? Does it utilize rich figurative language, complex syntactic structures, discipline-specific terminology, or maintain simplicity and clarity?
  Rhythm and Flow: Evaluate the pacing and smoothness of the text. Does it engage with rapid, succinct sentences, or unfold through leisurely, intricate phrasing? How does the rhythm align with the genre and content, shaping the overall effect and engagement of the piece?
  Tone and Voice: Determine the dominant tone (e.g., hopeful, cynical, impartial, authoritative, whimsical, grave, sarcastic) and the nature of the authorial voice (e.g., intimate, distant, introspective, enthusiastic). How do these elements enrich the text’s unique character?
Comparison and Guidance for Writers: How could a literature expert concisely convey the text's stylistic essence to an author wishing to replicate this style in new works across diverse topics? Emphasize critical stylistic features such as sentence structure, lexicon, tone, and the implementation of narrative techniques or rhetorical devices that are quintessential for capturing the style’s core.
      INPUT_TEXT:
      """+input_text 

    return prompt

def Few_1_Shot_style_genre_prompt(input_text):
    pass
def Few_3_Shot_style_genre_prompt(input_text):
    pass
def Few_5_Shot_style_genre_prompt(input_text):
    pass
def Few_10_Shot_style_genre_prompt(input_text):
    pass


def style_genre_prompt(input_text):
    prompt = """
      INSTRUCTION:
  Perform a succinct yet thorough analysis (50 to 200 words) of the text’s writing style, rhythm, genre, and more, carefully considering the distinctive features that typify its literary and communicative approach. Reflect on the following aspects:

  Format and Genre: How does the text situate itself within specific genres or sub-genres such as epic, tragedy, comedy, tragicomedy, mystery, thriller, horror, romance, speculative fiction (including fantasy, science fiction, and dystopian), magical realism, young adult (YA), children’s literature, flash fiction, creative nonfiction, biographical works, poetry (sonnet, haiku, free verse), historical narrative, legal or medical analysis, academic journal, self-help, how-to guides, or culinary reviews?
  Writing Style: Which terms best describe the text's style? Is it formal, informal, academic, conversational, ornate, sparse, lyrical, dry, satirical, or colloquial? Does it utilize rich figurative language, complex syntactic structures, discipline-specific terminology, or maintain simplicity and clarity?
  Rhythm and Flow: Evaluate the pacing and smoothness of the text. Does it engage with rapid, succinct sentences, or unfold through leisurely, intricate phrasing? How does the rhythm align with the genre and content, shaping the overall effect and engagement of the piece?
  Tone and Voice: Determine the dominant tone (e.g., hopeful, cynical, impartial, authoritative, whimsical, grave, sarcastic) and the nature of the authorial voice (e.g., intimate, distant, introspective, enthusiastic). How do these elements enrich the text’s unique character?
Comparison and Guidance for Writers: How could a literature expert concisely convey the text's stylistic essence to an author wishing to replicate this style in new works across diverse topics? Emphasize critical stylistic features such as sentence structure, lexicon, tone, and the implementation of narrative techniques or rhetorical devices that are quintessential for capturing the style’s core.
      INPUT_TEXT:
      """+input_text +". Let's think step by step."

    return prompt


def Zero_Shot_KG_format_example_prompt(current_kg_context, sentence):
    prompt = """FORMAT_EXAMPLE:
              'Javier Milei': {
                  'relations': {
                      'won': 'Argentina's Presidential Elections',
                      'received_congratulations_from': 'Sergio Massa'
                  },
                  'attributes': {
                      'political_orientation': 'Far-right, Libertarian',
                      'description': 'Outsider, Anti-establishment'
                  }
              },
              'Argentina's Presidential Elections': {
                  'relations': {
                      'featured_candidates': ['Javier Milei', 'Sergio Massa'],
                      'occurred_in': 'Argentina'
                  },
                  'attributes': {
                      'year': '2023',
                      'outcome': 'Javier Milei won',
                      'context': 'High inflation rate, Economic decline'
                  }
              }

      CURRENT_KNOWLEDGE_GRAPH:
      """ + current_kg_context + """
      INSTRUCTION:
      Take INPUT_SENTENCE and convert it into a part of a knowledge graph using the same format as in FORMAT_EXAMPLE. Use a naming and wording for entities, attributes and relationships that is coherrent with CURRENT_KNOWLEDGE_GRAPH. Try to write DESCRIPTIVE, SELF EXPLAINING NAMES for ENTITIS, ATTRIBUTES and RELATIONSHIPS, so that it will be REALLY EASY TO READ and UNDERSTAND the knowleadge graph later, even withou domain knowledge. But nevertheless, include only facts and entities and relations and attributes into the output, that are stated in the INPUT_SENTENCES. BE VERY FACTUAL, ACCURATE AND ON THE POINT. Try to include ALL FACTS, DATES, NUMBERS & NAMES in the INPUT_SENTENCE in the knowledge graph. AVOID REDUNDANCIES in the knowledge graph (don't mention the same fact twicein in the graph). Write <kg>right in fornt of your output of the knowledge graph and </kg> at it's end. - It is very, very important for me, that you perform this task very accurately, with the highest quality, to the best of your abilities.

      INPUT_SENTENCES:
      """ + sentence 
    return prompt

def Few_1_Shot_KG_format_example_prompt(current_kg_context, sentence):
    pass
def Few_3_Shot_KG_format_example_prompt(current_kg_context, sentence):
    pass
def Few_5_Shot_KG_format_example_prompt(current_kg_context, sentence):
    pass
def Few_10_Shot_KG_format_example_prompt(current_kg_context, sentence):
    pass

def KG_format_example_prompt(current_kg_context, sentence):
    prompt = """FORMAT_EXAMPLE:
              'Javier Milei': {
                  'relations': {
                      'won': 'Argentina's Presidential Elections',
                      'received_congratulations_from': 'Sergio Massa'
                  },
                  'attributes': {
                      'political_orientation': 'Far-right, Libertarian',
                      'description': 'Outsider, Anti-establishment'
                  }
              },
              'Argentina's Presidential Elections': {
                  'relations': {
                      'featured_candidates': ['Javier Milei', 'Sergio Massa'],
                      'occurred_in': 'Argentina'
                  },
                  'attributes': {
                      'year': '2023',
                      'outcome': 'Javier Milei won',
                      'context': 'High inflation rate, Economic decline'
                  }
              }

      CURRENT_KNOWLEDGE_GRAPH:
      """ + current_kg_context + """
      INSTRUCTION:
      Take INPUT_SENTENCE and convert it into a part of a knowledge graph using the same format as in FORMAT_EXAMPLE. Use a naming and wording for entities, attributes and relationships that is coherrent with CURRENT_KNOWLEDGE_GRAPH. Try to write DESCRIPTIVE, SELF EXPLAINING NAMES for ENTITIS, ATTRIBUTES and RELATIONSHIPS, so that it will be REALLY EASY TO READ and UNDERSTAND the knowleadge graph later, even withou domain knowledge. But nevertheless, include only facts and entities and relations and attributes into the output, that are stated in the INPUT_SENTENCES. BE VERY FACTUAL, ACCURATE AND ON THE POINT. Try to include ALL FACTS, DATES, NUMBERS & NAMES in the INPUT_SENTENCE in the knowledge graph. AVOID REDUNDANCIES in the knowledge graph (don't mention the same fact twicein in the graph). Write <kg>right in fornt of your output of the knowledge graph and </kg> at it's end. - It is very, very important for me, that you perform this task very accurately, with the highest quality, to the best of your abilities.

      INPUT_SENTENCES:
      """ + sentence +". Let's think step by step."
    return prompt

def answer_questions_prompts(context, question):
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
    return prompt

def generate_multiple_choice_question_prompts(text, number_of_questions):
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
    return prompt
    
    
