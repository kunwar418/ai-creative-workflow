import pandas as pd
from datetime import datetime
from src.product_agent import ProductResearchAgent
from src.strategy_agent import CreativeStrategyAgent
from src.prompt_agent import PromptGenerationAgent
from src.image_workflow import ImageGenerationWorkflow
from src.video_workflow import VideoGenerationWorkflow
from src.critic_agent import ReviewCriticAgent

class BulkProcessor:
    def __init__(self):
        self.jobs = {}
    
    def process_csv(self, csv_path):
        df = pd.read_csv(csv_path)
        results = []
        for idx, row in df.iterrows():
            job_id = f"job_{datetime.now().timestamp()}_{idx}"
            self.jobs[job_id] = {'status': 'processing', 'url': row['url']}
            results.append(self.process_single_url(row['url'], job_id))
        return results
    
    def process_single_url(self, url, job_id):
        try:
            product_agent = ProductResearchAgent()
            product_info = product_agent.extract_product_info(url)
            
            strategy_agent = CreativeStrategyAgent()
            strategies = strategy_agent.generate_strategies(product_info)
            
            prompt_agent = PromptGenerationAgent()
            image_prompts = prompt_agent.generate_image_prompts(product_info, strategies, 5)
            video_prompts = prompt_agent.generate_video_prompts(product_info, strategies, 2)
            
            image_workflow = ImageGenerationWorkflow()
            import time
            images = []
            for i, p in enumerate(image_prompts):
                images.append(image_workflow.generate_image(p, i))
                time.sleep(5)
            
            video_workflow = VideoGenerationWorkflow()
            videos = [video_workflow.generate_video(p, i) for i, p in enumerate(video_prompts)]
            
            critic = ReviewCriticAgent()
            evaluation = critic.evaluate({'images': images, 'videos': videos})
            
            self.jobs[job_id] = {'status': 'completed', 'images': images, 'videos': videos, 'evaluation': evaluation}
            
            return {'job_id': job_id, 'product': product_info['title'], 'images': images, 'videos': videos}
        except Exception as e:
            self.jobs[job_id] = {'status': 'failed', 'error': str(e)}
            return None