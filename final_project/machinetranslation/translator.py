''' English and french translation project using machine learning'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
'''Define a variable to hold your authentication api key.'''

VERSION_LT = '2018-05-01'
''' These are the translation version details.'''

language_translator = LanguageTranslatorV3(version = VERSION_LT, authenticator = authenticator)
language_translator.set_service_url(url)

def english_to_french(english_text):
    '''write code to translate from english to french'''
    french_text = language_translator.translate(english_text, model_id = 'en-fr').get_result()
    return french_text['translations'][0]['translation']
print(english_to_french(input("Please Input English Text: "))) #take an input)

def french_to_english(french_text):
    '''write code to translate from french to english'''
    english_text = language_translator.translate(french_text, model_id = 'fr-en').get_result()
    return english_text['translations'][0]['translation']
print(french_to_english(input("Please Input French Text: "))) #take an input)
