class PromptGenerationAgent:
    def generate_image_prompts(self, product_info, strategies, count=5):
        prompts = []
        for i in range(count):
            angle = strategies['angles'][i % len(strategies['angles'])]
            prompt_text = f"Product marketing image for {product_info['title']}. {angle['visual_theme']}. {angle['hook']} Professional ecommerce photography style. Clean background. Product placement. High quality. 4K."
            prompts.append(prompt_text)
        return prompts
    
    def generate_video_prompts(self, product_info, strategies, count=2):
        prompts = []
        for i in range(count):
            angle = strategies['angles'][i % len(strategies['angles'])]
            prompt_text = f"Short product video ad for {product_info['title']}. {angle['hook']} {angle['caption']}. Professional lighting. Smooth camera movement. 5 seconds. Product showcase."
            prompts.append(prompt_text)
        return prompts