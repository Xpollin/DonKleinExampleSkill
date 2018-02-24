def lambda_handler(event, context):
    # TODO implement
    if event['request']['type'] == 'LaunchRequest':
        return create_response('If you dont know how to use me you can ask for help by saying help', False)
    
    elif event['request']['type'] == 'SessionEndedRequest':
        return create_response('', True)
    
    elif event['request']['intent']['name'] == 'Help':
        return create_response('There are several commands, you can start by asking me who is Don Klein', False)
        
    elif event['request']['intent']['name'] == 'whoIsDonKlein':
        return create_response('Don is one super dude, you can also ask me what I think about Don', False)
    
    elif event['request']['intent']['name'] == 'WhatDoYouThink':
        return create_response("""Well, do you know if he is dating anyone? I am
        sweet on him oh baby. That's all I know about Don, I will have to check 
        his Tinder""", True)
    
    elif event['request']['intent']['name'] == 'endSession':
        return create_response('', True)
    
    

def create_response(text, shouldEndSession):
    return {
        'version': '1.0',
        'sessionAttributes': {},
        'response': {
          'outputSpeech': {
              'type': 'PlainText',
              'text': text
          },
          'card': {
              'type': 'Simple',
              'title': "Don",
              'content': text
          },
          'reprompt': {
              'outputSpeech': {
                  'type': 'PlainText',
                  'text': "text"
              }
          },
          'shouldEndSession': shouldEndSession
        }
    }