# CREW AI

## Installation & Minimalistic Example

This is a very simple CREW AI example, using Crew AI "create" to initiate a Project structure out of the box.
- The example is using a local "ollama" LLM, running on http://localhost:11434.
- No need for any LLM subscription, no OPENAI_API_TOKEN needed.
- Project runs well on a Macbook Pro M, with "ollama/llama3.2:latest" LLM.

**Scenario**

An AI Agent is dealing with anxiety and has decided to engage in therapy sessions with a very helpful psychoanalyst.
Watch their sessions as they try to identify the cause of this condition and decide to cope with it :-)

### 1. Install Python & Virtual Env (using "uv")
`source:` https://docs.crewai.com/en/installation

**Code:**

>uv venv --python 3.12           # Install Python & Virtual Env  
>source crew-env/bin/activate    # Activate Virtual Env  
>uv pip install crewai           # Install Crew AI  
>uv pip install crewai --upgrade # Upgrade Crew AI (only if needed)


### 2. Create Crew AI Project
> crewai create crew psycho

### 3. Run LLM
In a separate Terminal, run:
> ollama run llama3.2:latest

### 4. Run the Crew !
> crewai run 
