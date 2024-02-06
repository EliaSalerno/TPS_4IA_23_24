import time
import azure.cognitiveservices.speech as speechsdk
#-------------------------------------------------------------
#  costanti
#-------------------------------------------------------------
SUBSCRIPTION_KEY="5ba79c9336da495996c3ed52817ecc53"
REGION="westeurope"
#-------------------------------------------------------------
#  configurazione (proxy opzionale)
#-------------------------------------------------------------
speech_config = speechsdk.SpeechConfig(
    subscription=SUBSCRIPTION_KEY,
    region=REGION)
speech_config.speech_synthesis_language="it-IT"
#speech_config.set_proxy("proxy.intranet",3128,"","")
#-------------------------------------------------------------
#  creazione sintetizzatore vocale 
#-------------------------------------------------------------
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
#-------------------------------------------------------------
#  sintesi
#-------------------------------------------------------------
text="ciao, come va?"
result = speech_synthesizer.speak_text_async(text).get()
print(result)
