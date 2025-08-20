
# CREW AI Psycho – Therapeutic AI Playground 🤖✨ 

Welcome to **CREW AI**, a minimal yet powerful demo that shows how AI agents can collaborate in creative scenarios.
Here, an **anxious patient 🤯** engages in **therapy sessions 🛋️** with a **compassionate psychoanalyst 🧠**, exploring thoughts, emotions, and possible paths toward healing.

Watch their conversations unfold as they try to identify the roots of anxiety and discover coping strategies. 🌱💡

---

## ⚡ Quickstart: Installation & Example

This project was generated with **CrewAI `create`**, which gives you a working structure out of the box.

✅ Runs locally with **Ollama** (no API keys required)
✅ Works smoothly on a **MacBook Pro Silicon** 💻
✅ Uses **`ollama/llama3.2:latest`** as the LLM 🦙 *(but can be setup to any other LLM)*

---

### 🔧 1. Install Python & Virtual Environment (using [uv](https://docs.crewai.com/en/installation))

```bash
uv venv --python 3.12           # 🐍 Create Python 3.12 virtual environment  
source crew-env/bin/activate    # 🎛️ Activate virtual environment  
uv pip install crewai           # 📦 Install CrewAI  
uv pip install crewai --upgrade # ⬆️ Upgrade CrewAI (if needed)  
```

---

### 🏗️ 2. Create a CrewAI Project

> copy content of main/psycho folder into your "crewai-env" folder.
or
```bash
crewai create crew psycho # Create Default Project Structure from Crew AI
```

---

### 🚀 3. Run the Local LLM

Open a separate terminal and run Ollama with the latest **Llama 3.2**:

```bash
ollama run llama3.2:latest
```

---

### 🎭 4. Run the Crew!

```bash
crewai run
```

Sit back, relax, and watch the **patient** and **psychoanalyst** interact in real time.
You’ll observe a fascinating dialogue emerge between AI agents. 🌌🗣️

---

## 🌟 Why This Project is Cool

* 🛠️ **Hands-on**: Learn CrewAI concepts with a minimal, working setup.
* 🎭 **Roleplay Simulation**: Agents play out therapeutic interactions.
* 🧑‍💻 **No Subscriptions Needed**: 100% local and private.
* ⚡ **Lightweight**: Perfect for AI amateurs and hobbyists.

---

## 💡 Next Steps

After running this example, you can:

* 🧩 Add more agents (e.g., a “Supervisor” or “Friend” role).
* 🔄 Extend tasks into multi-session therapy.
* 🎨 Customize with different LLMs or topics.

---

✨ Have fun experimenting with **CrewAI**, and let your imagination guide your AI agents!
