import requests
import os
from PIL import Image, ImageDraw

class ImageGenerationWorkflow:
    def __init__(self):
        self.output_folder = "generated_images"
        os.makedirs(self.output_folder, exist_ok=True)
    
    def generate_image(self, prompt, index):
        try:
            url = f"https://pollinations.ai/prompt/{requests.utils.quote(prompt)}?width=1024&height=1024"
            response = requests.get(url, timeout=60)
            if response.status_code == 200:
                filename = f"{self.output_folder}/image_{index+1}.png"
                with open(filename, 'wb') as f:
                    f.write(response.content)
                return filename
            else:
                return self.create_placeholder_image(index)
        except Exception as e:
            return self.create_placeholder_image(index)
    
    def create_placeholder_image(self, index):
        filename = f"{self.output_folder}/image_{index+1}.png"
        img = Image.new('RGB', (1024, 1024), color='#2E4057')
        draw = ImageDraw.Draw(img)
        draw.text((200, 500), f"Product Image {index+1}", fill='white')
        img.save(filename)
        return filename