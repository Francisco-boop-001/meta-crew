#!/usr/bin/env python
import os
import yaml
from crewai import Agent, Crew, Process, Task
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

class MetaCrew:
    """
    MetaCrew is responsible for designing specialized Crews based on user requests.
    It ensures that every design strictly adheres to the CrewAI framework and coding best practices.
    """
    def __init__(self):
        # Load configuration files from YAML
        config_dir = os.path.dirname(__file__)
        with open(os.path.join(config_dir, "agents.yaml"), "r", encoding="utf-8") as f:
            self.agents_config = yaml.safe_load(f)
        with open(os.path.join(config_dir, "tasks.yaml"), "r", encoding="utf-8") as f:
            self.tasks_config = yaml.safe_load(f)
    
    def knowledge_specialist(self):
        """Creates the Knowledge Specialist agent."""
        return Agent(
            role=self.agents_config["knowledge_specialist"]["role"],
            goal=self.agents_config["knowledge_specialist"]["goal"],
            backstory=self.agents_config["knowledge_specialist"]["backstory"],
            llm=self.agents_config["knowledge_specialist"]["llm"],
        )

    def research_analyst(self):
        """Creates the Research Analyst agent."""
        return Agent(
            role=self.agents_config["research_analyst"]["role"],
            goal=self.agents_config["research_analyst"]["goal"],
            backstory=self.agents_config["research_analyst"]["backstory"],
            llm=self.agents_config["research_analyst"]["llm"],
        )

    def systems_architect(self):
        """Creates the Systems Architect agent."""
        return Agent(
            role=self.agents_config["systems_architect"]["role"],
            goal=self.agents_config["systems_architect"]["goal"],
            backstory=self.agents_config["systems_architect"]["backstory"],
            llm=self.agents_config["systems_architect"]["llm"],
        )

    def validator(self):
        """Creates the Validator agent."""
        return Agent(
            role=self.agents_config["validator"]["role"],
            goal=self.agents_config["validator"]["goal"],
            backstory=self.agents_config["validator"]["backstory"],
            llm=self.agents_config["validator"]["llm"],
        )

    def interpret_request_task(self):
        """Creates the task for interpreting user requests."""
        return Task(
            description=self.tasks_config["interpret_request_task"]["description"],
            expected_output=self.tasks_config["interpret_request_task"]["expected_output"],
            agent=self.knowledge_specialist(),
        )

    def research_task(self):
        """Creates the task for conducting research."""
        return Task(
            description=self.tasks_config["research_task"]["description"],
            expected_output=self.tasks_config["research_task"]["expected_output"],
            agent=self.research_analyst(),
        )

    def design_task(self):
        """Creates the task for designing crew configurations."""
        return Task(
            description=self.tasks_config["design_task"]["description"],
            expected_output=self.tasks_config["design_task"]["expected_output"],
            agent=self.systems_architect(),
        )

    def validation_task(self):
        """Creates the task for validating the blueprint."""
        return Task(
            description=self.tasks_config["validation_task"]["description"],
            expected_output=self.tasks_config["validation_task"]["expected_output"],
            agent=self.validator(),
        )

    def crew(self):
        """Creates the MetaCrew with all agents and tasks."""
        try:
            # Get the absolute path to the knowledge directory docs file
            docs_path = os.path.abspath(os.path.join(
                os.path.dirname(__file__), 
                "knowledge", 
                "CrewAI_docs.txt"
            ))
            
            # Create a TextFileKnowledgeSource with the docs file
            knowledge_source = TextFileKnowledgeSource(
                file_paths=[docs_path]
            )
            
            return Crew(
                agents=[
                    self.knowledge_specialist(),
                    self.research_analyst(),
                    self.systems_architect(),
                    self.validator()
                ],
                tasks=[
                    self.interpret_request_task(),
                    self.research_task(),
                    self.design_task(),
                    self.validation_task()
                ],
                process=Process.sequential,
                verbose=True,
                knowledge_sources=[knowledge_source]
            )
        except Exception as e:
            print(f"Error creating crew: {str(e)}")
            raise

if __name__ == "__main__":
    meta_crew = MetaCrew()
    result = meta_crew.crew().kickoff()
    print("MetaCrew blueprint result:", result)
