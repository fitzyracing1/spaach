"""
Real-time Speech-to-Text
Captures audio from microphone and prints transcribed text in real-time.
Press Ctrl+C to stop.
"""

import speech_recognition as sr


def main():
    print("Starting real-time speech-to-text...")
    print("Press Ctrl+C to stop.\n")

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("✓ Microphone active - start speaking\n")

            while True:
                audio = recognizer.listen(source, phrase_time_limit=5)
                try:
                    text = recognizer.recognize_google(audio)
                    if text.strip():
                        print(f"> {text}")
                except sr.UnknownValueError:
                    print("(could not understand)")
                except sr.RequestError as e:
                    print(f"(speech service error: {e})")

    except KeyboardInterrupt:
        print("\n\nStopping speech-to-text...")
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure you have SpeechRecognition and PyAudio installed:")
        print("  pip install SpeechRecognition pyaudio")
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
