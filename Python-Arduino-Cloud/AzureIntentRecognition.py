import time
import azure.cognitiveservices.speech as speechsdk

#-------------------------------------------------------------
#  costanti
#-------------------------------------------------------------
SUBSCRIPTION_KEY="2cb7cdebb2f44404b9f2eef03f97890a"
APPLICATION_ID="39dd5c1f-9cd9-4dd4-b0d4-4df3f733779c"
REGION="westeurope"
#-------------------------------------------------------------
#  configurazione (proxy opzionale)
#-------------------------------------------------------------
intent_config = speechsdk.SpeechConfig(
    subscription=SUBSCRIPTION_KEY,
    region=REGION)
#intent_config.set_proxy("proxy.intranet",3128,"","")
intent_config.speech_recognition_language="it-IT"
#-------------------------------------------------------------
#  creazione riconoscitore vocale 
#-------------------------------------------------------------
intent_recognizer = speechsdk.intent.IntentRecognizer(speech_config=intent_config)
model = speechsdk.intent.LanguageUnderstandingModel(app_id=APPLICATION_ID)
intent_recognizer.add_all_intents(model)
#-------------------------------------------------------------
#  funzione di callback chiamata dopo ogni riconoscimento
#-------------------------------------------------------------
def riconosciuto(evt):
    print(evt.result)
#-------------------------------------------------------------
#  attivazione del riconoscitore
#-------------------------------------------------------------
intent_recognizer.recognized.connect(riconosciuto)
intent_recognizer.start_continuous_recognition()
#-------------------------------------------------------------
#  ciclo di attesa dei riconoscimenti
#-------------------------------------------------------------
while True:
    time.sleep(0.5)
#-------------------------------------------------------------
#  terminazione del riconoscimento
#  (mai attivata in questo esempio)
#-------------------------------------------------------------
intent_recognizer.stop_continuous_recognition()
