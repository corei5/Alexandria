import pandas as pd
from datasets import load_dataset

from style_generation import get_style_genre
from first_n_words import get_first_n_words
from llm import ask_LLM
from kg_content import extract_kg_content
from minhash_vector import create_minhash_vector
from reconstruction_content import extract_reconstruction_content
from evaluate import evaluate_peformance

# Load the dataset from Hugging Face
dataset = load_dataset("CShorten/ML-ArXiv-Papers")

# Extract the 'train' split
train_dataset = dataset["train"]

# Create lists for titles and abstracts
titles = [entry['title'] for entry in train_dataset]
abstracts = [entry['abstract'] for entry in train_dataset]

# Create a list with concatenated title and abstract for each sample
concatenated_texts = [f"{title} {abstract}" for title, abstract in zip(titles, abstracts)]

API_KEY = "2356018b771d503cd9202a0a35195998bc3fabda6b1e6b379ee6ecc479f67401"

stop_len = 5000

all_kg_results = []
all_reconstruction_results = []
input_string_so_far_list = []
for input_text in concatenated_texts[:10]:

    writing_style = get_style_genre(get_first_n_words(input_text, 1000))

    # sentences= text_to_sentences(input_text)
    # sentences =sentences_to_large_strings(sentences)
    sentences = [input_text]
    # print(sentences)
    # continue
    current_kg = []
    current_kg.append("<style_analysis>" + writing_style + "</style_analysis>")
    print("<style_analysis>" + writing_style + "</style_analysis>")
    segment_nr = 1
    reconstruction_so_far = ""
    input_string_so_far = ""
    for sentence in sentences:
        input_string_so_far += sentence
        if len(input_string_so_far) > stop_len:
            break
        print("INPUT:", sentence)
        print("-----")
        '''
        prompt="""INPUT_TEXT:
        """+sentence+"""
        INSTRUCTION:
        Paraphrase the given input text so that every statement is rephrased into sentences that contain only three to ten words each. Use a simple structure and make sure to retain all information, names, numbers, and dates from the original text, without losing any information. The output text should consist exclusively of factual, neutrally phrased sentences that are three to ten words long. All information must be preserved, but without any artistic nuances. Direct speech in the source text should not be replicated as such, but it should be laid out in short sentences who said or did what in which order, ensuring a neutral, information-rich text."""
  
        reply = ask_LLM ('NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO', "You are a very smart very intelligence assistant who is very helpful.", input_text , API_KEY ,temperature=0.5,top_p=0.95,max_tokens=1000, frequency_penalty=1.1,presence_penalty=1.1)
        '''

        # Determine the slice of the last 50 elements (if the list has more than 50 elements)
        current_kg_context = current_kg[-50:] if len(current_kg) > 50 else current_kg

        # Concatenate the elements into a single string
        current_kg_context = ' '.join(current_kg_context)
        text = """FORMAT_EXAMPLE:
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

        for i in range(5):
            knowledge_graph_segment = ask_LLM('NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO',
                                              "You are a very smart very intelligence assistant who is very helpful.",
                                              text, API_KEY, temperature=0.5, top_p=0.95, max_tokens=1000,
                                              frequency_penalty=1.1, presence_penalty=1.1)
            if not (extract_kg_content(knowledge_graph_segment) == None):
                break
        try:
            current_kg.append("<segment " + str(segment_nr) + ">\n" + extract_kg_content(
                knowledge_graph_segment) + "<source_sentence_min_hash: " + str(
                create_minhash_vector(sentence)) + " >\n" + "</segment " + str(segment_nr) + ">\n")
            print("<segment " + str(segment_nr) + ">\n" + extract_kg_content(
                knowledge_graph_segment) + "<source_sentence_min_hash: " + str(
                create_minhash_vector(sentence)) + " >\n" + "</segment " + str(segment_nr) + ">\n")
        except:
            current_kg.append(
                "<segment " + str(segment_nr) + ">\n" + knowledge_graph_segment + "<source_sentence_min_hash: " + str(
                    create_minhash_vector(sentence)) + " >\n" + "</segment " + str(segment_nr) + ">\n")
            print("<segment " + str(segment_nr) + ">\n" + knowledge_graph_segment + "<source_sentence_min_hash: " + str(
                create_minhash_vector(sentence)) + " >\n" + "</segment " + str(segment_nr) + ">\n")

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
        for i in range(5):
            next_reconstruction = ask_LLM('NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO',
                                          "You are a very smart very intelligence assistant who is very helpful.",
                                          prompt, API_KEY, temperature=0.5, top_p=0.95, max_tokens=4000,
                                          frequency_penalty=1.1, presence_penalty=1.1)
            if not (extract_reconstruction_content(next_reconstruction) == None):
                break

        reconstruction_so_far += extract_reconstruction_content(next_reconstruction)
        print(extract_reconstruction_content(next_reconstruction))
        segment_nr += 1
    all_kg_results.append(current_kg)
    all_reconstruction_results.append(reconstruction_so_far)
    input_string_so_far_list.append(input_string_so_far)

# eval

df = pd.DataFrame({
    'Input_Texts': input_string_so_far_list,
    'Output_Graphs': all_kg_results,
    'Output_Reconstructions': all_reconstruction_results, })

print("500 word sample evalution:", "\n")
base_cap_500, original_cap_500, knowledgegraph_cap_500, reconstruction_cap_500 = evaluate_peformance(df, 5,
                                                                                                     "q_a_kg.parquet")

print("No context correct answer percentage:", base_cap_500, "\n")
print("Original context correct answer percentage:", original_cap_500, "\n")
print("Knowledgegraph context correct answer percentage:", knowledgegraph_cap_500, "\n")
print("Reconstruckted text context correct answer percentage:", reconstruction_cap_500, "\n")

