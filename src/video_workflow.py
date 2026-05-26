import requests
import os
from dotenv import load_dotenv

load_dotenv()

class VideoGenerationWorkflow:
    def __init__(self):
        self.output_folder = "generated_videos"
        os.makedirs(self.output_folder, exist_ok=True)
        self.api_key = os.getenv("LTX_API_KEY")
        
        if not self.api_key or self.api_key == "your_ltx_api_key_here":
            print("Warning: Valid LTX_API_KEY not found in .env file. Using placeholders.")
    
    def generate_video(self, prompt, index):
        self.current_prompt = prompt  # Store prompt for use in placeholder
        if not self.api_key or self.api_key == "your_ltx_api_key_here":
            return self.create_placeholder_video(index)
        
        try:
            url = "https://api.ltx.video/generate"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "prompt": prompt,
                "duration": 5,
                "resolution": "720p"
            }
            
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            
            if response.status_code == 200:
                result = response.json()
                video_url = result.get('video_url')
                
                if video_url:
                    video_response = requests.get(video_url)
                    filename = f"{self.output_folder}/video_{index+1}.mp4"
                    with open(filename, 'wb') as f:
                        f.write(video_response.content)
                    print(f"Video saved: {filename}")
                    return filename
            
            return self.create_placeholder_video(index)
            
        except Exception as e:
            print(f"Video generation error: {e}")
            return self.create_placeholder_video(index)
    
    def create_placeholder_video(self, index):
        filename = f"{self.output_folder}/video_{index+1}.txt"
        with open(filename, 'w') as f:
            f.write(f"Video {index+1}\n")
            f.write(f"Prompt: {getattr(self, 'current_prompt', 'No prompt available')}\n")
            f.write("To generate real videos: Add valid LTX_API_KEY to .env file\n")
        return filename