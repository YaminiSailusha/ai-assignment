# Phase 2: Simple Autonomous Bot (No LangGraph needed)

# Mock search tool
def mock_search(query):
    if "ai" in query.lower():
        return "AI is rapidly replacing many jobs in tech industry"
    elif "crypto" in query.lower():
        return "Bitcoin price is rising due to new investments"
    else:
        return "Tech industry is evolving quickly"


# Step 1: Decide topic
def decide_topic(bot_id):
    if bot_id == "BotA":
        return "AI future"
    elif bot_id == "BotB":
        return "Technology problems"
    else:
        return "Stock market"


# Step 2: Generate post
def generate_post(bot_id):
    topic = decide_topic(bot_id)
    context = mock_search(topic)

    post = {
        "bot_id": bot_id,
        "topic": topic,
        "post_content": f"{context}. This clearly shows my opinion as {bot_id}."
    }

    return post


# Test
if __name__ == "__main__":
    result = generate_post("BotA")
    print(result)