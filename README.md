Overview

This project simulates the future of work in an AI-driven economy using an agent-based model (ABM) built with the Mesa framework in Python. The simulation explores how workers, corporations, and governments interact under varying conditions of automation, policy interventions, and worker adaptability.
The goal of this simulation is to understand how different strategies — such as reskilling subsidies, regulation of automation, and corporate strategy shifts — impact employment levels, worker well-being, and corporate competitiveness.

Project Structure
File	Description
agent.py	Defines the WorkerAgent, CorporationAgent, and GovernmentAgent classes and their behaviors.
model.py	Defines the AIWFModel, which initializes agents, controls the environment, and tracks system-wide metrics like unemployment.
run.py	Runs the simulation for a set number of steps and outputs a plot of unemployment rate over time.
requirements.txt	List of Python packages needed to run the simulation (mainly Mesa, matplotlib, pandas).
AI_Workforce_Odyssey_Policy_Game.pdf	Full analysis report describing the simulation setup, scenarios, results, and conclusions.

How to Run the Simulation
Clone the Repository or download the project files.
Install required libraries (if not already installed):
bash
Copy
pip install mesa matplotlib pandas
Run the simulation:
bash
Copy
python run.py
View Output: A graph showing unemployment rate over simulation steps will be generated automatically.

Agents
WorkerAgent: Decides whether to reskill based on automation pressure and policy support.
CorporationAgent: Chooses between automation, augmentation, or human-centric strategies depending on the level of automation.
GovernmentAgent: Monitors unemployment and corporate automation rates, and dynamically switches between neutral, subsidy, or regulation policies.
Key Features
Dynamic interactions between workers, corporations, and government agents.
Adjustable parameters for automation level, worker adaptability, and policy triggers.
Visualization of unemployment rate trends across different scenarios.
Scenario variations modeling different real-world future possibilities (e.g., full automation, aggressive reskilling, augmentation strategies, worker resistance).

Sample Output
Graphs showing unemployment trends over time under various policy and automation scenarios.
Analysis report detailing system behavior for eight different test scenarios.

Requirements
Python 3.7+
Mesa
Matplotlib
Pandas
Install all requirements with:
bash
Copy
pip install -r requirements.txt
