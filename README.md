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

## 🌐 Preview
<img width="1915" height="788" alt="Screenshot 2025-07-20 003845" src="https://github.com/user-attachments/assets/771aa309-d783-4305-bb24-5cb4f127d9c1" />
<img width="1914" height="518" alt="Screenshot 2025-07-20 003906" src="https://github.com/user-attachments/assets/18f82e4b-045c-44e1-a730-b466fdd86036" />
<img width="1916" height="661" alt="Screenshot 2025-07-20 003951" src="https://github.com/user-attachments/assets/c2f58253-a170-4f03-b5a1-8a792629342c" />
<img width="1914" height="797" alt="Screenshot 2025-07-20 004059" src="https://github.com/user-attachments/assets/176cf7c0-2af9-4880-8b1d-cce63c4cdd59" />

---

## 📁 Project Structure
```
Chat_bot/
├── streamlit_app.py                # Main Streamlit UI
├── dialogflow_utils.py             # Dialogflow integration
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── .gitignore                      # Git ignore rules
└── coustomer-support-bot/
    └── intents/                    # Dialogflow intents (JSON)
```

---

## 🤖 Customization
- Add or edit intents in Dialogflow for new flows.
- Update the vertical menu in `streamlit_app.py` to match your support topics.
- Tweak the CSS for your brand colors or style.

---
## 👤 Author

**Developed by:**  
- Sankalp Tiwari  
- [LinkedIn](www.linkedin.com/in/sankalp-tiwari-350545203)  
- [GitHub](https://github.com/Sankalp-Dev06)
