"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Ramaker Impersonations. " \
                    "Please tell me who to impersonate by saying " \
                    "what does blank say"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me who to impersonate by saying " \
                    "what does blank say."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Ramaker Impersonations. " \
                    "get wrecked"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_impersonate_attributes(familyMember):
    return {"familyMember": familyMember}

def list_members(intent, session):
	card_title = intent['name']
	session_attributes = {}
	should_end_session = False

	speech_output = "Family members are Dad, Mom, Grace, Mason, Elise, Cooper, and Jasper."
	reprompt_text = ""

	return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def impersonate_member(intent, session):
	session_attributes= {}
	reprompt_text=None
	should_end_session = False

	family_member = intent['slots']['Member']['value']
	session_attributes = create_impersonate_attributes(family_member)

	if (family_member == 'dad' or family_member == 'Dad'):
		speech_output = "Does it smell like popcorn in here? You all cost me too much money. By the way you're grounded."
	elif (family_member == 'mom' or family_member == 'Mom'):
		speech_output = "Somebody buy me some shoes and then give me a massage. Nevermind I'm about to fall zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
	elif (family_member == 'grace' or family_member == 'Grace'):
		speech_output = "Ooooh Jacob. You're so dreamy. Lets send each other kissy faces on Snapchat. Smoochy smoochy smootch. Hashtag boyfriend."
	elif (family_member == 'mason' or family_member == 'Mason'):
		speech_output = "Breh. Get wrecked. KOBY! Get wrecked. Breh. Breh. KOBY! Breh."
	elif (family_member == 'elise' or family_member == 'Elise'):
		speech_output = "I can sing and dance and play the clarinet and do gymnastics and do cartwheels and I have a dogs and a rainbow loom and oh I see a butterfly I'm hungry can I have a snack?"
	elif (family_member == 'cooper' or family_member == 'Cooper'):
		speech_output = "Mom. Mom. Mom. Pet me. Mom. Mom. Mom. Mom. Pet me. Pet me. Mom."
	elif (family_member == 'jasper' or family_member == 'Jasper'): 
		speech_output = "First I'm going to steal a shoe. Then I'm going to pee on it. Then I'm going to chew on it. Then I'm going to pee on it again. Then I'm going to run away. Then I'm going to puke."
	else:
		speech_output = "I don't know who that is."

	return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

"""def set_color_in_session(intent, session):
     Sets the color in the session and prepares the speech to reply to the
    user.
    

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Color' in intent['slots']:
        favorite_color = intent['slots']['Color']['value']
        session_attributes = create_favorite_color_attributes(favorite_color)
        speech_output = "I now know your favorite color is " + \
                        favorite_color + \
                        ". You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))"""


"""def get_color_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "You can say, my favorite color is red."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))"""


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
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "ListMembersIntent":
        return list_members(intent, session)
    elif intent_name == "ImpersonateIntent":
        return impersonate_member(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
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
