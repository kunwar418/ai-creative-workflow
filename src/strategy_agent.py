import json
import ollama

class CreativeStrategyAgent:
    def generate_strategies(self, product_info):
        prompt = f"""For product: {product_info['title']}
        Features: {product_info['features']}
        Audience: {product_info['target_audience']}
        
        Generate 3 creative marketing angles. Return JSON with: angles (list of objects with hook, visual_theme, caption)"""
        
        result = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': prompt}])
        
        try:
            strategies = json.loads(result['message']['content'])
        except:
            strategies = {
                'angles': [
                    {'hook': 'Never run out of battery again!', 'visual_theme': 'Modern lifestyle', 'caption': '30hr battery life keeps you going'},
                    {'hook': 'Hear every detail', 'visual_theme': 'Premium audio experience', 'caption': 'Studio quality sound'},
                    {'hook': 'Work from anywhere', 'visual_theme': 'Professional setting', 'caption': 'Perfect for remote work'}
                ]
            }
        return strategies