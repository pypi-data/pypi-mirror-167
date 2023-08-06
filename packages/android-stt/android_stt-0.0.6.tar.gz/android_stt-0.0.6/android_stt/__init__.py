import time
from jnius import autoclass
import android
from android.permissions import request_permissions, Permission
request_permissions([Permission.RECORD_AUDIO])
Bundle = autoclass('android.os.Bundle')
PA = autoclass('org.kivy.android.PythonActivity')

class RecognizerListenerBase:
	def onBeginningOfSpeech(self):
		print('onBeginningOfSpeech()')

	def onPartialResults(self, partialResults):
		print('onPartialResults() called', particalResults)
		strArray = partialResults.getStringArrayList(SR.RESULTS_RECOGNITION)
		return strArray
		
	def onReadyForSpeech(self, params):
		print('onReadyForSpeech() called', params)

	def onResults(self, results):
		print('onResults() called', results)
		strArray = results.getStringArrayList(SR.RESULTS_RECOGNITION)
		return strArray

	def onEndOfSpeech(self):	
		print('onEndOfSpeech() called')

	def onError(self, error):
		if self.on_error:
			self.on_error(error)


class AndroidNativeSTT(object):
	"""
	use case:
	tts = AndroidNativeSTT()
	listener = RecognizerListenerBase(tts)
	tts.setListener(listener)
	tts.startListening()
	....
	tts.stopListening()
	"""
	def __init__(self):
		SR = autoclass('android.speech.SpeechRecognizer')
		self.context = PA.mActivity
		if not SR.isRecognitionAvailable(self.context):
			raise Exception('Recognition not available')
		if SR.isOnDeviceRecognitionAvailable(self.context):
			self._stt = SR.createOnDeviceSpeechRecognizer(self.context)
		else:
			self._stt = SR.createSpeechRecognizer(self.context)
		self.listener = None

	def setListener(self, listener):
		self.listener = listener
		self._stt.setRecognitionListener(listener)

	def startListening(self):
		if self.listener is None:
			return
		Intent = autoclass('android.speech.RecognizerIntent')
		intent = Intent(Intent.ACTION_RECOGNIZE_SPEECH)
		intent.putExtra(Intent.EXTRA_LANGUAGE, "en-US");
		intent.putExtra(Intent.EXTRA_LANGUAGE_MODEL, \
						Intent.LANGUAGE_MODEL_FREE_FORM)
		self._stt.startListener(intent)

	def stopListener(self):
		self._stt.stopListening()


	def cancel(self):
		self._stt.cancel()

	def __del__(self):
		self._stt.destroy()

