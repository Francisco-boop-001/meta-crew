#!/usr/bin/env python
import os
from meta.crew import MetaCrew

# Disable telemetry to avoid connection issues
os.environ["CREWAI_TELEMETRY"] = "False"

def main():
    # Define your specific request as a string
    user_request = "I want a crew that implements the CrewAI framework to perform market research on the latest trends in AI technology."
    
    # Print startup information
    print(f"\nStarting MetaCrew with request: \"{user_request}\"")
    print("----------------------------------------")
    
    try:
        # Initialize the MetaCrew
        meta_crew = MetaCrew()
        
        # Create and kick off the crew with the user request
        crew_instance = meta_crew.crew()
        
        # Pass the user request to the crew kickoff
        result = crew_instance.kickoff(inputs={"request": user_request})
        
        # Display the result
        print("\nMetaCrew Blueprint Result:")
        print("--------------------------")
        print(result)
        
    except Exception as e:
        print(f"\nError during execution: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
