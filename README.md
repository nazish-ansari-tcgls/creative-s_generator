🎨 Creative Generator










Creative Generator is an AI-powered creative automation framework built using a multi-agent architecture to generate high-quality marketing creatives at scale. It is designed for branding, real estate marketing, campaign visuals, persona-based creatives, and automated design workflows.

🚀 Features

🧠 Multi-Agent Orchestration

🎯 Prompt & Creative Intelligence

🎨 Visual Styling & Brand Control

🖼️ Image-based Reasoning

✅ Automated QA & Validation

🧩 Modular & Extensible Architecture

📊 Dashboard-Driven Execution

🏗️ Architecture Overview

The system follows an agent-driven pipeline, where each agent performs a specialized role and contributes to a refined final creative.

Input → Category Analysis → Prompt Generation
      → Visual + Styling → Messaging
      → QA Validation → Synthesis → Output

📂 Project Structure
creative-s_generator/
│
├── Dashboard.py
├── requirements.txt
│
├── assets/
│   ├── inputs/
│   ├── outputs/
│   └── logo/
│
├── backend/
│   ├── orchestrator.py
│   ├── constants.py
│   ├── schemas.py
│   │
│   ├── agents/
│   │   ├── category_agent.py
│   │   ├── prompt_generation.py
│   │   ├── visual_agent.py
│   │   ├── styling_agent.py
│   │   ├── messaging_agent.py
│   │   ├── qa_agent.py
│   │   ├── synthesizer_agent.py
│   │   └── creative_generation.py
│   │
│   └── utils/
│       ├── image_utils.py
│       └── storage.py

🤖 Agents & Responsibilities
Agent	Responsibility
Category Agent	Determines creative intent
Prompt Generation Agent	Builds optimized prompts
Visual Agent	Image understanding & reasoning
Styling Agent	Branding & aesthetic rules
Messaging Agent	Copy & messaging generation
QA Agent	Quality assurance
Synthesizer Agent	Final creative assembly
Orchestrator	Agent coordination
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/creative-s_generator.git
cd creative-s_generator

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate    # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
python Dashboard.py

📦 Asset Management
Folder	Purpose
assets/inputs/	Reference images / inputs
assets/outputs/	Generated creatives
assets/logo/	Brand logos
🛠️ Use Cases

🏢 Real estate marketing creatives

📈 Investor persona brochures

🎯 Campaign posters & banners

🧬 Brand-consistent visual generation

🤖 Automated creative pipelines


📍 Roadmap

⏳ Batch creative generation

🌐 Web-based UI (Streamlit / React)

📊 Creative scoring & analytics

🧠 Persona-driven generation

🔁 Versioned creative history


👤 Author

Nazish Ali Ansari
AI Creative Automation | Generative Media | Design Systems

📜 License

This project is licensed under the MIT License.
