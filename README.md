# Customer Support Chatbot (Streamlit + Dialogflow)

## 📝 Project Overview
This project is a modern, multi-turn customer support chatbot web app built with Streamlit and Dialogflow. It is designed to provide instant, 24/7 support for e-commerce or service websites, similar to the chatbots used by Amazon, Flipkart, and Zomato. The chatbot can answer FAQs, help users track orders, process returns and refunds, check product availability, and more. It supports dynamic, context-aware conversations, meaning it can handle follow-up questions, remember context, and prompt for missing information (like order ID or return reason) in a natural, conversational way.

The UI is inspired by Telegram, featuring chat bubbles, avatars, and a vertical quick-reply menu for common support topics. All business logic, slot filling, and context management are handled by Dialogflow, making it easy to extend or update the bot by editing intents in Dialogflow.

---

## 🚀 Features
- **Modern UI:** Telegram-style chat bubbles, vertical quick-reply menu, and beautiful gradient background.
- **Multi-turn Conversations:** Handles follow-ups, slot filling, and context (e.g., asks for order ID, reason for return, etc.).
- **Dialogflow Integration:** All intent logic, slot filling, and context handled by Dialogflow agent.
- **Easy Customization:** Add or update intents in Dialogflow, and the bot updates instantly.
- **No white boxes:** Clean, immersive chat experience.

---

## 💡 Usage
- The chatbot UI will open in your browser.
- Use the vertical menu to quickly ask about common support topics.
- Type your own questions or follow up as in a real chat.
- The bot will guide you through multi-step flows (e.g., order tracking, returns, refunds).

---

## 🌐 Deployment
- You can deploy this app for free on [Streamlit Community Cloud](https://streamlit.io/cloud) or any cloud VM.
- For Streamlit Cloud, add your `dialogflow_service_account.json` as a secret.

---

## 📁 Project Structure
```
Chat_bot/
├── streamlit_app.py                # Main Streamlit UI
├── dialogflow_utils.py             # Dialogflow integration
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── .gitignore                      # Git ignore rules
├── dialogflow_service_account.json # (Not committed) Dialogflow credentials
└── coustomer-support-bot/
    └── intents/                    # Dialogflow intents (JSON)
```

---

## 🤖 Customization
- Add or edit intents in Dialogflow for new flows.
- Update the vertical menu in `streamlit_app.py` to match your support topics.
- Tweak the CSS for your brand colors or style.

---

## 📞 Support
For help, open an issue or contact the maintainer.