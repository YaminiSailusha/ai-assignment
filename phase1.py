# Simple keyword-based routing (no ML, no heavy libraries)

personas = {
    "BotA": ["ai", "crypto", "technology"],
    "BotB": ["capitalism", "privacy", "society"],
    "BotC": ["market", "trading", "money", "roi"]
}

def route_post_to_bots(post):
    post = post.lower()
    matched = []

    for bot, keywords in personas.items():
        for word in keywords:
            if word in post:
                matched.append(bot)
                break

    return matched


# Test
if __name__ == "__main__":
    post = "OpenAI released a new AI model replacing developers"
    print(route_post_to_bots(post))