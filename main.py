import dns.resolver
from model import ai_resolve
from nlp_processor import extract_domain

def resolve_domain(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        return [ip.to_text() for ip in result]
    except Exception as e:
        return str(e)

def main():
    query = input("Enter your DNS query: ")
    domain = extract_domain(query)
    if domain:
        print(ai_resolve(domain))
    else:
        print("Could not extract a valid domain.")

if __name__ == "__main__":
    main()
