import spacy
from fuzzywuzzy import process

nlp = spacy.load("en_core_web_sm")

def extract_domain(query):
    """Extract domain name from natural language query."""
    doc = nlp(query.lower())
    domain_candidates = [token.text for token in doc if "." in token.text]
    if domain_candidates:
        return domain_candidates[0]

    common_domains = ["google.com", "facebook.com", "youtube.com", "twitter.com"]
    best_match = process.extractOne(query, common_domains)
    return best_match[0] if best_match else None

if __name__ == "__main__":
    query = input("Enter your DNS query: ")
    print("Extracted domain:", extract_domain(query))
