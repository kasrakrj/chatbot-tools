PROJECT_ID = 'score-fetcher-agent-ndcd'
SESSION_ID = '123456789'
LANGUAGE_CODE = 'en-US'



score1 = {
    810198331: 18,
    810196111: 17
}
score2 = {
    810198331:20,
    810196111:19
}

scores = {
    1: score1,
    2: score2
}



def detect_intent_texts(project_id, session_id, text, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    from google.cloud import dialogflow

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))


    text_input = dialogflow.TextInput(text=text, language_code=language_code)

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    print("=" * 20)
    print("Query text: {}".format(response.query_result.query_text))
    print(
        "Detected intent: {} (confidence: {})\n".format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence,
        )
    )
    if ('studentID' in response.query_result.fulfillment_text) and ('courseID' in response.query_result.fulfillment_text):
        list = response.query_result.fulfillment_text.split(' ')
        print(list)
        if scores.get(int(list[3])) != None:
            score = (scores.get(int(list[3]))).get(int(list[1]))
            if score != None:
                print(score)
            else:
                print("student not found")
        else: 
            print("course not found")
    else:    
        print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))

    


if __name__=="__main__":
    while(True):
        inp =  input("input: ")
        if inp != "exit":
            detect_intent_texts(PROJECT_ID, SESSION_ID, inp, LANGUAGE_CODE)
        else:
            break