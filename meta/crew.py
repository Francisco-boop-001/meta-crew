#!/usr/bin/env python
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, task, crew

class MetaCrew(CrewBase):
    """
    MetaCrew is responsible for designing specialized Crews based on user requests.
    It ensures that every design strictly adheres to the CrewAI framework and coding best practices.
    """
    # Load configurations from YAML files in the meta folder
    agents_config = "meta/agents.yaml"
    tasks_config = "meta/tasks.yaml"

    @agent
    def knowledge_specialist(self) -> Agent:
        return Agent(config=self.agents_config["knowledge_specialist"])

    @agent
    def research_analyst(self) -> Agent:
        return Agent(config=self.agents_config["research_analyst"])

    @agent
    def systems_architect(self) -> Agent:
        return Agent(config=self.agents_config["systems_architect"])

    @agent
    def validator(self) -> Agent:
        return Agent(config=self.agents_config["validator"])

    @task
    def interpret_request_task(self) -> Task:
        return Task(config=self.tasks_config["interpret_request_task"])

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"])

    @task
    def design_task(self) -> Task:
        return Task(config=self.tasks_config["design_task"])

    @task
    def validation_task(self) -> Task:
        return Task(config=self.tasks_config["validation_task"])

    @crew
    def crew(self) -> Crew:
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
            verbose=True
        )

if __name__ == "__main__":
    meta_crew = MetaCrew()
    result = meta_crew.crew().kickoff()
    print("MetaCrew blueprint result:", result)
