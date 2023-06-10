#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import speech_recognition as sr
import openai

openai.api_key = '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'
def get_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": 'Assume you are Chatbot robot in Zewail city university called "Nour" talking to a child, you should respond to the following message and shortly answer in Arabic: '+ message +"in max of 100 words "},
        ]
    )
    return response .choices[0].message['content']
def audio_callback(audio):
    rospy.loginfo("Recognizing...")

    # Perform speech recognition
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio.data, language='en')
        rospy.loginfo("STT: " + text)

        # Get response from OpenAI
        response_text = get_response(text)

        # Publish the response to the STT topic
        stt_pub.publish(response_text)

    except sr.UnknownValueError:
        rospy.logwarn("Speech recognition could not understand audio")
    except sr.RequestError as e:
        rospy.logerr("Could not request results from Google Speech Recognition service; {0}".format(e))

def stt_node():
    rospy.init_node('stt_node')
    rospy.loginfo("STT node started")

    # Create a publisher for the STT topic
    stt_pub = rospy.Publisher('stt_topic', String, queue_size=10)

    # Create a speech recognizer
    recognizer = sr.Recognizer()

    # Configure microphone settings
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        recognizer.non_speaking_duration = 0.1
        recognizer.pause_threshold = 0.1
        recognizer.energy_threshold = 300

        # Start listening to audio input
        rospy.loginfo("Listening...")
        recognizer.listen_in_background(source, audio_callback)

    rospy.spin()

if __name__ == '__main__':
    stt_node()

