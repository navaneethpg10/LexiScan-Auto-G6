import re

def extract_dates(text):
    return re.findall(r'\b\d{1,2}\s+\w+\s+\d{4}\b', text)

def extract_money(text):
    return re.findall(r'\$\s?\d+(?:,\d{3})*(?:\.\d{2})?', text)

def extract_termination_clauses(text):
    clauses = []
    for line in text.split("."):
        if "terminate" in line.lower():
            clauses.append(line.strip())
    return clauses
