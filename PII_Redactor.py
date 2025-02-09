from presidio_analyzer import AnalyzerEngine
analyzer = AnalyzerEngine()

from presidio_anonymizer import AnonymizerEngine
anonymizer = AnonymizerEngine()


# text = """<NAME>
# • <EMAIL> • CITY, STATE • https://www.linkedin.com/in/LINK
# """
# results = analyzer.analyze(text=text, entities=["PHONE_NUMBER", "EMAIL_ADDRESS", "PERSON", "LOCATION", "URL"], language="en")

# for result in results:
#     print(result)


# anonymized_text = anonymizer.anonymize(text=text, analyzer_results=results)

# print("\nOriginal Text:")
# print(text)
# print("\nAnonymized Text:")
# print(anonymized_text.text)



def redact_pii(user_text):
    results = analyzer.analyze(text=user_text, entities=["US_SSN", "PHONE_NUMBER", "EMAIL_ADDRESS", "PERSON", "CREDIT_CARD"], language="en")
    anonymized_text = anonymizer.anonymize(text=user_text, analyzer_results=results)
    return anonymized_text.text

if __name__ == "__main__":
    while True:
        user_text = input("\nEnter text (or type 'exit' to quit): ")
        if user_text.lower() == "exit":
            break
        print("\nRedacted Output:")
        print(redact_pii(user_text))