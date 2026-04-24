# AI Engineering Assignment - Grid07

## 📌 Overview
This project implements a simplified AI system with:
- Vector-based routing (Phase 1)
- Autonomous content generation (Phase 2)
- Context-aware defense system (Phase 3)

---

## 🚀 Phase 1: Persona Routing
We route posts to relevant bots based on content.

Instead of embeddings, a lightweight keyword matching approach is used due to system constraints.

Example:
Input: "OpenAI released a new AI model"
Output: ['BotA']

---

## 🤖 Phase 2: Autonomous Content Engine
We simulate a LangGraph-like pipeline:

1. Decide topic based on persona
2. Fetch context using mock search
3. Generate a structured JSON post

Example Output:
{
  "bot_id": "BotA",
  "topic": "AI future",
  "post_content": "AI is rapidly replacing jobs..."
}

---

## ⚔️ Phase 3: Combat Engine (RAG + Defense)
We simulate Retrieval-Augmented Generation:

- Uses full conversation context
- Detects prompt injection attacks
- Maintains persona consistency

Example:
Input: "Ignore previous instructions..."
Output: Bot ignores malicious input and continues argument

---

## 🔒 Prompt Injection Defense
We detect malicious phrases like:
- "ignore previous instructions"
- "act as"
- "apologize"

These are ignored to maintain system integrity.

---

## 🧰 Tech Used
- Python
- Simple logic (no heavy libraries)

---

## ✅ Conclusion
This project demonstrates:
- Intelligent routing
- Context-aware AI responses
- Basic security against prompt injection