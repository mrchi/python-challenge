# coding=utf-8

import base64
import tempfile
import pathlib
import subprocess
import wave

import requests

url = "http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html"
resp = requests.get(url)
attachment = b"".join(resp.content.split(b"\n")[27:1986])
wav_content = base64.b64decode(attachment)

wav_path = pathlib.Path(tempfile.gettempdir()) / "ch18.wav"
with open(wav_path, "wb") as f:
    f.write(wav_content)
subprocess.call(["open", wav_path])  # Only for macOS

# clue = "sorry"
reformed_wav_path = pathlib.Path(tempfile.gettempdir()) / "ch18-reformed.wav"
with wave.open(str(wav_path), "rb") as wav, wave.open(
    str(reformed_wav_path), "wb"
) as reformed_wav:
    reformed_wav.setnchannels(wav.getnchannels())
    reformed_wav.setsampwidth(wav.getsampwidth())
    reformed_wav.setframerate(wav.getframerate())
    for i in range(wav.getnframes()):
        frame = wav.readframes(1)[::-1]
        reformed_wav.writeframesraw(frame)
subprocess.call(["open", reformed_wav_path])  # Only for macOS

clue = "idiot"
answer = "idiot2"
print(f"http://butter:fly@www.pythonchallenge.com/pc/hex/{answer}.html")
