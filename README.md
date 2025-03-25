# AI-Powered DNS Resolver with NLP-Based Query Understanding
An AI-based DNS resolver that detects and blocks malicious domains, with NLP-powered query understanding.

## How to Run
```bash
git clone <repo-url>
cd ai_dns_resolver
pip install -r requirements.txt
python main.py

# AI-Powered DNS Resolver with NLP-Based Query Understanding

## Overview
This project is an innovative, AI-powered DNS resolver that leverages Natural Language Processing (NLP) to interpret user queries and resolve domain names. Unlike a traditional DNS resolver that simply translates domain names to IP addresses, this project uses machine learning to detect potentially malicious domains and NLP techniques to understand user requests expressed in natural language. This makes it ideal for cybersecurity applications, network optimization, and improving user experience by automatically handling and validating DNS queries.

## Key Features
- **DNS Resolution:** Translates domain names to IP addresses using the `dnspython` library.
- **Machine Learning for Security:** Uses a trained Random Forest model (via scikit-learn) to classify domains as safe or malicious based on dummy features (with room for improvement by integrating real-time threat intelligence).
- **NLP-Based Query Understanding:** Utilizes spaCy and fuzzy matching (via fuzzywuzzy) to extract domain names from natural language queries.
- **Redis Caching:** Implements caching to speed up repeated queries and reduce network latency.
- **API Endpoint:** Exposes functionality through a Flask-based REST API, enabling easy integration with other systems.
- **Containerization:** Provides a Dockerfile for containerizing the application for scalable deployments.

## How It Works
1. **User Input:** The user inputs a natural language query (e.g., "Find the IP address of google.com" or "What is the IP for facebook?").
2. **NLP Processing:** The NLP module (`nlp_processor.py`) processes the query to extract a domain name. If the domain is not clearly provided, it uses fuzzy matching against common domains.
3. **DNS Resolution & Security Check:** The extracted domain is passed to the AI module (`model.py`) where:
   - A pre-trained Random Forest model is loaded.
   - The domain is classified as safe or malicious using dummy feature extraction (a placeholder for future enhancements).
   - If classified as malicious, the request is blocked.
   - If safe, the domain is resolved to its corresponding IP address using the `dnspython` library.
4. **API Response:** The Flask API (`server.py`) returns a JSON response containing the original query, extracted domain, and result (either an IP address or a block message).
5. **Caching:** Optionally, Redis caching (`cache.py`) is used to store and retrieve recent query results for faster subsequent lookups.

## Technologies Used
- **Python 3.10/3.11:** Core programming language.
- **dnspython:** For DNS resolution.
- **Flask:** For building the RESTful API.
- **scikit-learn:** For machine learning model creation and inference.
- **pandas:** For data handling during model training.
- **Joblib:** For model persistence.
- **spaCy:** For NLP-based query processing.
- **fuzzywuzzy & python-Levenshtein:** For fuzzy matching and typo correction.
- **Redis:** For caching DNS resolution results.
- **Docker:** For containerization and deployment.

## Project Structure
