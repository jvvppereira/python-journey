# AI ChatBot with Streamlit

A simple **AI chatbot web app** built with **Python** and **Streamlit**.
The application allows users to send messages through a chat interface and receive responses from an AI model.

This project is designed for **learning and experimentation**, demonstrating how to integrate an AI provider with a simple frontend.

---

## 🚀 Features

* Simple **chat interface**
* **Conversation history** stored in session memory
* Integration with AI providers
* Easy to extend for experiments or learning
* Built with minimal code using Streamlit

---

## 🧰 Technologies Used

* Python
* Streamlit
* Hugging Face Inference API
* OpenAI (optional integration)

---

## 📦 Installation

Clone the repository and install the dependencies.

```bash
pip install streamlit openai huggingface_hub
```

---

## 🔑 Configuration

Set your API token in the code:

```python
TOKEN = "your_token_here"
```

If using Hugging Face, generate a token at:

https://huggingface.co/settings/tokens

---

## ▶️ Running the App

Start the Streamlit server:

```bash
streamlit run main.py
```

Then open the local URL shown in the terminal (usually):

```
http://localhost:8501
```

---

## 💬 How It Works

The chatbot follows a simple workflow:

1. Display the chat interface
2. User sends a message
3. The message is stored in session memory
4. The message is sent to the AI provider
5. The AI response is displayed and stored in the conversation history

Conversation history is stored using:

```python
st.session_state
```

This allows the chatbot to **remember previous messages during the session**.

---

## 🤖 Supported Models

Example models you can use with Hugging Face:

* Meta-Llama-3-8B-Instruct

  * Quality: ⭐⭐⭐⭐
  * Speed: ⭐⭐⭐
  * Resource usage: Medium

* Phi-3-mini-4k-instruct

  * Quality: ⭐⭐⭐
  * Speed: ⭐⭐⭐⭐
  * Resource usage: Low

You can switch models in the code:

```python
InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token=TOKEN
)
```

---

## 🧠 Project Structure

Typical structure:

```
.
├── main.py
└── README.md
```

---

## ⚙️ Key Concepts Demonstrated

* Building a **chat UI with Streamlit**
* Using **session state for conversation memory**
* Integrating **AI APIs**
* Caching model clients using:

```python
@st.cache_resource
```

This avoids reloading the client on every refresh.

---

## 📚 Learning Goals

This project is useful for learning:

* AI API integration
* Chat interface design
* Streamlit development
* Prompt-based AI interactions

---

## 🛠 Possible Improvements

Some ideas to expand the project:

* Streaming responses
* Save chat history to a database
* Add multiple model options
* Implement authentication
* Deploy online

---

## 📄 License

This project is intended for **educational purposes**.
