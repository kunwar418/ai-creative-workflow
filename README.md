# AI Product Creative Generation Workflow

An automated multi-agent AI system that generates product marketing images and videos from any product URL. The system uses 7 specialized AI agents working together to research products, create creative strategies, generate prompts, produce visual content, and evaluate quality.

## Features

- **Product Research Agent**: Extracts product information (title, features, price, brand, target audience) from any URL
- **Creative Strategy Agent**: Generates 3 unique marketing angles with hooks, visual themes, and captions
- **Prompt Generation Agent**: Creates optimized prompts for image and video generation models
- **Image Generation Workflow**: Generates 5 product marketing images using AI
- **Video Generation Workflow**: Generates 2 short product videos/reels using AI
- **Review/Critic Agent**: Evaluates generated content quality, consistency, and branding
- **Bulk Processing Layer**: Processes multiple product URLs via CSV upload with job tracking

## Tech Stack

- **Python 3.10+** - Core programming language
- **Ollama + Llama 3.2** - Local LLM for AI agents (free, runs on your machine)
- **Pollinations.ai** - Free image generation API
- **LTX Video API** - Video generation (optional, free tier available)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/kunwar418/ai-creative-workflow.git
cd ai-creative-workflow
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
###  2. Install Ollama
```bash
ollama pull llama3.2
```
# Create a .env file in the root directory:

```bash
LTX_API_KEY=your_ltx_api_key_here
```
### 3. Run the Application
```bash
python main.py
```

ai-creative-workflow/
├── src/
│   ├── product_agent.py      # Extracts product information
│   ├── strategy_agent.py     # Generates creative marketing angles
│   ├── prompt_agent.py       # Creates optimized prompts
│   ├── image_workflow.py     # Generates 5 product images
│   ├── video_workflow.py     # Generates 2 product videos
│   ├── critic_agent.py       # Evaluates quality and consistency
│   └── bulk_processor.py     # Handles CSV uploads and job tracking
├── data/
│   └── sample_products.csv   # Sample CSV for bulk processing
├── generated_images/         # Output folder for images
├── generated_videos/         # Output folder for videos
├── main.py                   # Main entry point
├── requirements.txt          # Python dependencies
└── README.md                 # This file

Product: Premium Wireless Headphones

 Generated 5 images:
  - generated_images/image_1.png
  - generated_images/image_2.png
  - generated_images/image_3.png
  - generated_images/image_4.png
  - generated_images/image_5.png

 Generated 2 videos:
  - generated_videos/video_1.mp4
  - generated_videos/video_2.mp4

   Product URL/CSV
       │
       ▼
┌──────────────────┐
│ Product Research │  ← Extracts title, features, price, brand
│     Agent        │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│Creative Strategy │  ← Generates hooks, visual themes, captions
│     Agent        │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Prompt Generator │  ← Creates optimized prompts for images/videos
│     Agent        │
└────────┬─────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌───────┐ ┌───────┐
│Image  │ │Video  │
│Gen    │ │Gen    │
│5 images│ │2 videos│
└───┬───┘ └───┬───┘
    │         │
    └────┬────┘
         ▼
┌──────────────────┐
│  Review/Critic   │  ← Scores quality, provides feedback
│     Agent        │
└──────────────────┘

