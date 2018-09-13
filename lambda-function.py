from __future__ import print_function
from sunfish import *
import time
import re

move_dict = {"alpha one": "a1", "alpha to": "a2", "alpha two": "a2", "alpha three": "a3", "alpha four": "a4", "alpha five": "a5", "alpha six": "a6", "alpha seven": "a7", "alpha eight": "a8",
             "bravo one": "b1", "bravo to": "b2", "bravo two": "b2", "bravo three": "b3", "bravo four": "b4", "bravo five": "b5", "bravo six": "b6", "bravo seven": "b7", "bravo eight": "b8",
             "charlie one": "c1", "charlie to": "c2", "charlie two": "c2", "charlie three": "c3", "charlie four": "c4", "charlie five": "c5", "charlie six": "c6", "charlie seven": "c7", "charlie eight": "c8",
             "delta one": "d1", "delta to": "d2", "delta two": "d2", "delta three": "d3", "delta four": "d4", "delta five": "d5", "delta six": "d6", "delta seven": "d7", "delta eight": "d8",
             "echo one": "e1", "echo to": "e2", "echo two": "e2", "echo three": "e3", "echo four": "e4", "echo five": "e5", "echo six": "e6", "echo seven": "e7", "echo eight": "e8",
             "foxtrot one": "f1", "foxtrot to": "f2", "foxtrot two": "f2", "foxtrot three": "f3", "foxtrot four": "f4", "foxtrot five": "f5", "foxtrot six": "f6", "foxtrot seven": "f7", "foxtrot eight": "f8",
             "golf one": "g1", "golf to": "g2", "golf two": "g2", "golf three": "g3", "golf four": "g4", "golf five": "g5", "golf six": "g6", "golf seven": "g7", "golf eight": "g8",
             "hotel one": "h1", "hotel to": "h2", "hotel two": "h2", "hotel three": "h3", "hotel four": "h4", "hotel five": "h5", "hotel six": "h6", "hotel seven": "h7", "hotel eight": "h8",
            "alpha 1": "a1", "alpha to": "a2", "alpha 2": "a2", "alpha 3": "a3", "alpha 4": "a4", "alpha 5": "a5", "alpha 6": "a6", "alpha 7": "a7", "alpha 8": "a8",
             "bravo 1": "b1", "bravo to": "b2", "bravo 2": "b2", "bravo 3": "b3", "bravo 4": "b4", "bravo 5": "b5", "bravo 6": "b6", "bravo 7": "b7", "bravo 8": "b8",
             "charlie 1": "c1", "charlie to": "c2", "charlie 2": "c2", "charlie 3": "c3", "charlie 4": "c4", "charlie 5": "c5", "charlie 6": "c6", "charlie 7": "c7", "charlie 8": "c8",
             "delta 1": "d1", "delta to": "d2", "delta 2": "d2", "delta 3": "d3", "delta 4": "d4", "delta 5": "d5", "delta 6": "d6", "delta 7": "d7", "delta 8": "d8",
             "echo 1": "e1", "echo to": "e2", "echo 2": "e2", "echo 3": "e3", "echo 4": "e4", "echo 5": "e5", "echo 6": "e6", "echo 7": "e7", "echo 8": "e8",
             "foxtrot 1": "f1", "foxtrot to": "f2", "foxtrot 2": "f2", "foxtrot 3": "f3", "foxtrot 4": "f4", "foxtrot 5": "f5", "foxtrot 6": "f6", "foxtrot 7": "f7", "foxtrot 8": "f8",
             "golf 1": "g1", "golf to": "g2", "golf 2": "g2", "golf 3": "g3", "golf 4": "g4", "golf 5": "g5", "golf 6": "g6", "golf 7": "g7", "golf 8": "g8",
             "hotel 1": "h1", "hotel to": "h2", "hotel 2": "h2", "hotel 3": "h3", "hotel 4": "h4", "hotel 5": "h5", "hotel 6": "h6", "hotel 7": "h7", "hotel 8": "h8",
                "beta one": "b1", "beta to": "b2", "beta two": "b2", "beta three": "b3", "beta four": "b4", "beta five": "b5", "beta six": "b6", "beta seven": "b7", "beta eight": "b8",
                "beta 1": "b1", "beta to": "b2", "beta 2": "b2", "beta 3": "b3", "beta 4": "b4", "beta 5": "b5", "beta 6": "b6", "beta 7": "b7", "beta 8": "b8"}


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_dialog_delegate(title, output, reprompt_text, should_end_session):
    return {
        'directives' : [
            {
                'type': "Dialog.Delegate"
            }
        ],
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }



# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response(session):
    if session['new'] == False:
        card_title = "Welcome"
        reprompt_text = "I didn't catch that."
        should_end_session = False
        session_attributes = session['attributes']
        speech_output = "Check out the skills page for instructions on use! To create a new game, say: Alexa, ask Obscura Chess to play. To start playing right away, send a command like: Alexa, move Echo 2 try Echo 4. To quit, say: Alexa, quit." 
    else:
        session_attributes = {}
        card_title = "Welcome"
        speech_output = "Check out the skills page for instructions on use! To create a new game, say: Alexa, ask Obscura Chess to play. To start playing right away, send a command like: Alexa, move Echo 2 try Echo 4. To quit, say: Alexa, quit." 
        reprompt_text = "Please resend your command." 
        should_end_session = False
        session_attributes['board'] = Position(initial, 0, (True,True), (True,True), 0, 0)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_favorite_color_attributes(favorite_color):
    return {"favoriteColor": favorite_color}




        
def start_game(intent_request, session):
    #initializing with attributes
    pos = Position(initial, 0, (True,True), (True,True), 0, 0)
    session_attributes = {}
    session_attributes['board'] = pos
    dialog_state = intent_request['dialogState']
    card_title = "Welcome"

        #color = 'white'
        #if color == 'white':
    speech_output = "I'm ready to play as black. Send a legal move order like: Alexa, move echo 2 try echo 4, or ask for help"
        #else:
            #speech_output = "I am ready to play as white."
    reprompt_text = "I didn't catch that."
    should_end_session = False
    
    if dialog_state in ("STARTED", "IN_PROGRESS"):
        return build_response(session_attributes, build_dialog_delegate(card_title, speech_output, reprompt_text, should_end_session))
    else:
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

        
def movei(intent, session):
    speech_output = ''
    session_attributes = {}
    movefrom = intent['slots']['movepiece']['value'].lower()
    moveto = intent['slots']['movedto']['value'].lower()
    
    #get the correct position for each move from the session variable
    #pos = Position(initial, 0, (True,True), (True,True), 0, 0)
    pos_text = session['attributes']['board']
    
    #get all the stuff out of the tuple so we can create a new object to pass
    boardstatus = pos_text[0]
    scorestatus = pos_text[1]
    wcstatus = pos_text[2]
    wcstatus1 = tuple(wcstatus)
    bcstatus = pos_text[3]
    bcstatus1 = tuple(bcstatus)
    epstatus = pos_text[4]
    kpstatus = pos_text[5]
    
    card_title = "Welcome"
    reprompt_text = "I didn't catch that."
    should_end_session = False
    
    #make the last known object
    pos = Position(boardstatus, scorestatus, wcstatus1, bcstatus1, epstatus, kpstatus)
    
    #parse the voice input moves
    if (movefrom not in move_dict) or (moveto not in move_dict):
        speech_output = "Please send your command again"
        session_attributes['board'] = pos
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))
    else:
    #pass to the eval function
        given = move_dict[movefrom] + move_dict[moveto]
        reval = try_move(pos, given)
        speech_output = reval['textresponse'] + reval['enginemove']
        #update the session if a new pos was created.
        session_attributes['board'] = reval['updatedboard']
        
    #change these later
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def try_move(pos, given):
    s = given
    if pos.score <= -MATE_LOWER:
        game_over(False, pos2)
    #define an object for the searcher
    searcher1 = Searcher()
    #parsing the given move as in sunfish library.
    move = None
    match = re.match('([a-h][1-8])'*2, given)
    if match:
        move = parse(match.group(1)), parse(match.group(2))
    else:
        ret = {"success": False, "updatedboard": pos, "enginemove": "", 'textresponse': "Invalid move sent"}
        return ret
    #check if the move is legal, and play if it is.
    if move in pos.gen_moves():
        pos1 = pos.move(move)
        
        if pos1.score <= -MATE_LOWER:
            game_over(True, pos1)
            
        move, score = searcher1.search(pos1, secs=0.25)
    
        cpuval = render(119-move[0]) + render(119-move[1])
        pos2 = pos1.move(move)
        
        if score == MATE_UPPER:
            game_over(False, pos2)
            
        ret = {"success": True, "updatedboard": pos2, "enginemove": "I made the move: " + cpuval + "Repeat: " + cpuval , 'textresponse': "You moved {}, ".format(s)}
        return ret
    #return the same board as input.
    else:
        ret = {"success": False, "updatedboard": pos, "enginemove": "", 'textresponse': "That's against the rules."}
        return ret
        
def game_over(player_won, pos):
    session_attributes = {}
    session_attributes['board'] = pos
    card_title = 'Done'
    if player_won:
        speech_output = "You won, good job!"
    else:
        speech_output = "I won! Better luck next time."
    
    reprompt_text = "aaaaa"
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))
        

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response(session)


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "ResignIntent":
        return game_over(False, False)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response(session)
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "StartGameIntent":
        return start_game(intent_request, session)
    elif intent_name == "MoveIntent":
        return movei(intent, session)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])