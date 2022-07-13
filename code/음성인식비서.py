# 음성을 인식하여 텍스트로 바꾸고 텍스트의 조건에 따라 동작하는 음성인식 비서 만들기
# pip install SpeechRecognition 음성을 텍스트로 변환
# conda install pyaudio -y
# pip install playsound 음악파일을 파이썬에서 재생

import pyaudio
import wave
from playsound import playsound

# 녹음파일 형식 지정
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = r".\output.wav" # 녹음파일 위치 지정

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("음성녹음을 시작합니다.")

# 녹음 시작 
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("음성녹음을 완료하였습니다.")

# 녹음된 음서 저장
stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print("녹음된 파일을 재생합니다.")
playsound(WAVE_OUTPUT_FILENAME)
# ----------------------------------------------------------------------------

# import speech_recognition as sr

# try:
#     while True :
#         r = sr.Recognizer()
        
#         with sr.Microphone() as source: # 마이크에서 음성을 받음
#             print("음성을 입력하세요.")
#             audio = r.listen(source)
#         try: # 음성을 인식하여 반환
#             print("음성변환: " + r.recognize_google(audio, language='ko-KR'))
#         except sr.UnknownValueError:
#             print("오디오를 이해할수 없습니다.")
#         except sr.RequestError as e:
#             print(f"에러가 발생하였습니다. 에러원인: {e}")

# except KeyboardInterrupt:
#     pass
# ----------------------------------------------------------------------------

import speech_recognition as sr

try:
    while True :
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("음성을 입력하세요.")
            audio = r.listen(source)
        try:
            stt = r.recognize_google(audio, language='ko-KR')
            print("음성변환: " + stt)
            
            # 음성인식된 글자중에 특정 글자가 포함되어 있으면 프린트 출력
            if "안녕" in stt:
                print("네 안녕하세요")
            elif "날씨" in stt:
                print("정말 날씨가 좋네요")
            
        except sr.UnknownValueError:
            print("오디오를 이해할수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생하였습니다. 에러원인: {e}")

except KeyboardInterrupt:
    pass