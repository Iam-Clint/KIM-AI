# KimAI – Chat with Helen

![KimAI Banner](https://i.imgur.com/6fJ0o0v.png)

> **A real-time AI chatbot with a sleek dark-blue interface**  
> **Created by:** **Clinton Adedoja**  
> **Institution:** **Veritas University Abuja**

---

## Live Demo

[https://kimai-helen.onrender.com](https://kimai-helen.onrender.com)

---

## Features

- **Real-time AI responses** using **Groq API** (`llama-3.1-8b`)
- **Mature dark-blue/black UI** with smooth animations
- **Mobile-friendly** design
- **Helen remembers conversation context** (last 4 messages)
- **Creator awareness**: Helen knows she was made by **Clinton Adedoja**
- **100% free & hosted on Render.com**

---

## Tech Stack

| Component       | Technology           |
|----------------|----------------------|
| Backend         | Python, Flask        |
| AI Model        | Groq (`llama-3.1-8b`)|
| Frontend        | HTML, CSS, JavaScript|
| Hosting         | Render.com (Free)    |
| Version Control | Git & GitHub         |

---

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR-USERNAME/kimai-helen.git
cd kimai-helen

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your Groq API key
echo "GROQ_API_KEY=lgrk_your_key_here" > .env

# 4. Run the app
python main.py
