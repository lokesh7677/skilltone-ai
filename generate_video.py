import openai
import requests
from gtts import gTTS
from moviepy.editor import *
import os

openai.api_key = "your-openai-api-key"

def generate_script(skill_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Write a 45-second educational script about {skill_prompt} for a YouTube Short."}]
    )
    return response['choices'][0]['message']['content']

def text_to_speech(text, output_path="voice.mp3"):
    tts = gTTS(text)
    tts.save(output_path)
    return output_path

def download_stock_video(skill, output_path="stock.mp4"):
    # Use Pexels or Pixabay video API
    # Example placeholder: Use local placeholder video
    os.system(f"curl -o {output_path} https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4")
    return output_path

def merge_audio_video(video_path, audio_path, final_output="final_video.mp4"):
    video = VideoFileClip(video_path).subclip(0, 45)
    audio = AudioFileClip(audio_path)
    final = video.set_audio(audio)
    final.write_videofile(final_output, fps=24)
    return final_output

def generate_skill_video(skill):
    script = generate_script(skill)
    print("SCRIPT:", script)

    audio_path = text_to_speech(script)
    video_path = download_stock_video(skill)
    final_video = merge_audio_video(video_path, audio_path)

    return final_video
