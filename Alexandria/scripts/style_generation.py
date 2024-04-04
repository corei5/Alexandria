import scripts.llm
import scripts.api_key
import scripts.prompts

API_KEY = scripts.api_key.API_KEY

def get_style_genre(input_text):

      text = scripts.prompts.style_genre_prompt(input_text)
      for i in range(5):
        style_genre = scripts.llm.ask_LLM ('NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO', "You are a very smart very intelligence assistant who is very helpful.", text , API_KEY ,temperature=0.5,top_p=0.95,max_tokens=1000, frequency_penalty=1.1,presence_penalty=1.1)
        try:
          if not style_genre== None and len(style_genre)>100:
            break
        except:
          pass
      return style_genre