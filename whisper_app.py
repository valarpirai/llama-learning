import gradio as gr
import whisper
import pytube

model = whisper.load_model("tiny.en")

def download_audio(url):
    # Reading the above Taken movie Youtube link
    data = pytube.YouTube(url)
    # Converting and downloading as 'MP4' file
    audio = data.streams.get_audio_only()
    file_name = audio.download(output_path="audios/")
    print("Audio Downloaded ", file_name)
    return file_name

def generate_transcription(url):
    downloaded_file = download_audio(url)
    print("Speech Recognition started..")
    result = model.transcribe(downloaded_file, fp16=False)
    # print(result["text"])
    return result["text"]

demo = gr.Interface(fn=generate_transcription, 
                    inputs="text", 
                    outputs=gr.Textbox(lines=10, placeholder="Speech to text content..."),
                    title="OpenAI Whisper Speech Recognition",
                    description="Enter a youtube.com video URL and submit. Text will be generated from the Video")
    
if __name__ == "__main__":
    demo.launch(show_api=True)
