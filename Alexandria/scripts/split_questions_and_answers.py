def split_to_questions_and_answers(text):
    questions = []
    correct_answers = []
    data_list = text.split("#+*")
    #print(data_list)
    for rawtext in data_list:
      #print(rawtext)
      if len(rawtext)<2:
        continue

      tmp = rawtext.split(";")
      question= tmp[0]
      answer = tmp[1]
      questions.append(question.replace("questions=","").strip())
      correct_answers.append(answer)


    return questions, correct_answers
