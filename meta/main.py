#!/usr/bin/env python
from meta.crew import MetaCrew

def main():
    # Define your specific request as a plain string.
    request = "I want a crew that performs market research on the latest trends in AI technology."
    meta_crew = MetaCrew()
    # Pass the request string directly to the kickoff method.
    result = meta_crew.crew().kickoff(request)
    print("MetaCrew blueprint result:", result)

if __name__ == "__main__":
    main()
