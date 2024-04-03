from llm import ask_LLM
API_KEY = "2356018b771d503cd9202a0a35195998bc3fabda6b1e6b379ee6ecc479f67401"

def get_style_genre(input_text):

      text = """
      INSTRUCTION:
  Perform a succinct yet thorough analysis (50 to 200 words) of the text’s writing style, rhythm, genre, and more, carefully considering the distinctive features that typify its literary and communicative approach. Reflect on the following aspects:

  Format and Genre: How does the text situate itself within specific genres or sub-genres such as epic, tragedy, comedy, tragicomedy, mystery, thriller, horror, romance, speculative fiction (including fantasy, science fiction, and dystopian), magical realism, young adult (YA), children’s literature, flash fiction, creative nonfiction, biographical works, poetry (sonnet, haiku, free verse), historical narrative, legal or medical analysis, academic journal, self-help, how-to guides, or culinary reviews?
  Writing Style: Which terms best describe the text's style? Is it formal, informal, academic, conversational, ornate, sparse, lyrical, dry, satirical, or colloquial? Does it utilize rich figurative language, complex syntactic structures, discipline-specific terminology, or maintain simplicity and clarity?
  Rhythm and Flow: Evaluate the pacing and smoothness of the text. Does it engage with rapid, succinct sentences, or unfold through leisurely, intricate phrasing? How does the rhythm align with the genre and content, shaping the overall effect and engagement of the piece?
  Tone and Voice: Determine the dominant tone (e.g., hopeful, cynical, impartial, authoritative, whimsical, grave, sarcastic) and the nature of the authorial voice (e.g., intimate, distant, introspective, enthusiastic). How do these elements enrich the text’s unique character?
Comparison and Guidance for Writers: How could a literature expert concisely convey the text's stylistic essence to an author wishing to replicate this style in new works across diverse topics? Emphasize critical stylistic features such as sentence structure, lexicon, tone, and the implementation of narrative techniques or rhetorical devices that are quintessential for capturing the style’s core.
      INPUT_TEXT:
      """+input_text

      for i in range(5):
        style_genre = ask_LLM ('NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO', "You are a very smart very intelligence assistant who is very helpful.", text , API_KEY ,temperature=0.5,top_p=0.95,max_tokens=1000, frequency_penalty=1.1,presence_penalty=1.1)
        try:
          if not style_genre== None and len(style_genre)>100:
            break
        except:
          pass
      return style_genre