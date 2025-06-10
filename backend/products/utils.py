# utils.py

import re

def parse_user_sentence(sentence):
    sentence = sentence.lower()

    CATEGORIES = ['shoes', 'phone', 'shirt', 'laptop', 'bag']

    # Extract category
    category = next((cat for cat in CATEGORIES if cat in sentence), None)

    # Extract price under ₹/rs.
    price_match = re.search(r'(under|below)\s*(₹|rs\.?)?\s*(\d+)', sentence)
    max_price = int(price_match.group(3)) if price_match else None

    return {
        'category': category,
        'max_price': max_price
    }
