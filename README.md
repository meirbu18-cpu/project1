# Workshop 1: 

## 1. Installing Prerequisites and setting up environment

These steps need to be done once. 

### 1.1. Python 3.11+

- Download from [python.org](https://www.python.org/downloads/)

- Verify Python is in your path. 
  - **Windows:** 
    - during installation, check "Add Python to PATH." 
    - To verify: open a new terminal and run `where python`

  - **Mac:**
  - edit `~/.zshrc` to include pyhton in `PATH` and add alias `python`
  - To verify: open a new terminal and run `which -a python3`

<!--    ```bash
    which -a python3          # see all Python installations on the system
    nano ~/.zshrc             # open shell config (or: code ~/.zshrc to open in VS Code)
    ```
  Add to the file:
  ```bash
  export PATH="/Library/Frameworks/Python.framework/Versions/3.14/bin/python3:$PATH"
  alias python=/Library/Frameworks/Python.framework/Versions/3.14/bin/python3
  ```
  Then reload:
  ```bash
  source ~/.zshrc
  ```
  Adjust the version number (`3.14`) to match what you installed.
  -->

- Confirm: `python --version`

### 1.2. VS Code and the Python Extension

We'll use VS Code development environment. If you prefer a different one thats totally fine. 

- Download [VS Code](https://code.visualstudio.com/)
- Open VS Code. 
- Create a local folder for this workshop files and open it in VS Code. 
- In VS Code, install the Python extension from the Extensions panel.
- The **Python Environments panel** (Explorer sidebar) lets you create, activate, and manage virtual environments and install packages visually — without touching the terminal. 
- Istalling Python packages can also be done with `pip`.

### 1.3. Create and Activate a Python Virtual Environment. (`venv`)

A virtual environment isolates the project's packages. This avoids package conflicts between projects. 


Create `venv` from VS Code Python extension Environment Manager, or from terminal:
```bash
python -m venv .venv
```

Activate the environment from VS Code Python extension Environments Managers panel → select the environment → Activate, or activate from terminal:
- Windows: `.venv\Scripts\activate`
- Mac/Linux: `source .venv/bin/activate`

When active, your terminal prompt shows the env name: `(.venv) %`


### 1.4. Claude Code VS Code Extension

During the course we will work with Claude Code. Claude is an AI assistant made by Anthropic. Claude Code is Claude's coding-focused sibling — built specifically for software development. 
You will need to create an account. The minimal [plan](https://claude.com/) to get Code abilities is Pro. 

Install VS Code extension for Claude Code [getting started](https://code.claude.com/docs/en/vs-code)

Open Claude in VS Code panel and chat with it a bit. 


### 1.5. Create a GitHub Code Repository 

We will be working with Git to manage code we develop during the course. This allows teams to develop software projects together.

- Create a GitHub account at [github.com](https://github.com) (or confirm an existing one) — you'll need your GitHub email for the Git configuration below

- Download Git from [git-scm.com](https://git-scm.com/)

- Configure after installing, using the same email as your GitHub account:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"
  ```
- **Authenticate with GitHub** — required to push code. Two options ([full guide](https://docs.github.com/en/authentication)):
  - **SSH** (recommended for developers): generate an SSH key and add it to your GitHub account — no passwords or token expiry to manage
  - **Personal Access Token (PAT)**: generate a token in GitHub Settings → Developer Settings → Personal Access Tokens, and use it as your password when pushing over HTTPS

- Create a private repo on Git Hub and clone it into your working folder.
- Create a branch. 

## 2. Python Basics Refresher
Copy the file `python-basics.ipynb` into your project.
This is a [Jupyter Notebook](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
This file has Python examples. 
Select as kernel the `venv` environment you created. 
Run the notebook and follow the cells for a python refresher. 

Commit your branch and publish it.

Locate your branch on GitHub and create a pull request with the added file.

## 3. First API Call

In order to call an AI API you will need an API key from a provider and purchase a budget for tokens. 

We recommend to use [OpenRouter](https://openrouter.ai/) it is a provider that supports all major models through a unified interface, OpenAI SDK compatible. We will be using it in the course examples.

### 3.1. OpenRouter Provider

[OpenRouter](https://openrouter.ai/docs/quickstart) is a unified LLM interface supporting several [models](https://openrouter.ai/models).

#### API Key Setup

Create an [OpenRouter](https://openrouter.io/) API key. Store it in the `.env` file with key `OPENROUTER_API_KEY`.

#### Call Chat API
Add file `ai-api-openrouter.py` to the VS Code project. 

Read it, run it, play with the various parameters (`max_tokens`, `model`, `messages`), and check how changing them impacts the response.

### 3.2. Anthropic Provider (Optional)
Anthropic provides API access to Claude via [Claude Console](https://platform.claude.com/dashboard).

#### API Key Setup

Create an [Anthropic](console.anthropic.com) API key. 
Store it in the `.env` file with key `ANTHROPIC_API_KEY`.

#### Call Chat API
Add file `ai-api-anthropic.py` to the VS Code project. 

Read it, run it, play with the various parameters (`max_tokens`, `model`, `messages`), and check how changing them impacts the response.

## 4. Git Integration
Commit the added file, push and merge the pr. Review these changes on GitHub.

## 5. Experience Hugging-Face Playground

[Hugging Face](https://huggingface.co/) is a popular open-source platform and community focused on artificial intelligence (AI) and machine learning (ML). Often described as the "GitHub of machine learning," it acts as a central hub where developers, researchers, and hobbyists can collaborate, share, and test AI models, datasets, libraries and applications.

Create a new environment and activate it in VS Code project. 
Run and follow the python notebook `hugging-face-playground.ipynb`.
