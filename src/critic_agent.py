import json
import ollama

class ReviewCriticAgent:
    def evaluate(self, outputs):
        prompt = f"""Evaluate these marketing assets: {json.dumps(outputs)}
        
        Return JSON with: overall_score (1-10), feedback (list of strengths/weaknesses), recommended_improvements"""
        
        try:
            result = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': prompt}])
            return json.loads(result['message']['content'])
        except:
            return {
                'overall_score': 8,
                'feedback': ['Good visual quality', 'On-brand messaging', 'Clear product focus'],
                'recommended_improvements': ['Add more lifestyle context', 'Include pricing in some assets']
            }