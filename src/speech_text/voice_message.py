from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
import pyaudio
import wave
def vm_to_text(audiofile):
    load_dotenv(find_dotenv())
    client = OpenAI()
    
    audio_file= open(audiofile, "rb")
    transcript = client.audio.translations.create(
        model="whisper-1", 
        file=audio_file,
        response_format='text'
    )
    print(transcript)
    return(transcript)

def record_voice(seconds = 5):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("Start recording")
    frames = []
    for _ in range(int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Recording stopped")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open("vm.wav", "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == "__main__":
    secs_to_record = int(input("enter duration of voice message to record. The recording will start after you press enter\n"))
    record_voice(secs_to_record)
    audiofile = "vm.wav"
    vm_to_text(audiofile)