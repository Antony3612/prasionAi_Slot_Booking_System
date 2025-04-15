from praisonaiagents import Agent, Task, PraisonAIAgents

appointment_agent = Agent(
    name="AppointmentScheduler",
    instructions="""
    You are an assistant that helps users schedule and view their appointments for the day.
    
    Rules:
    1. Ensure no appointment overlaps.
    2. Always keep 15 mins tea break at 11:00 AM.
    3. Always keep 1 hour lunch break from 1:00 PM to 2:00 PM.
    4. Appointments must be between 8:30 AM and 5:30 PM.
    5. Add appointments to a JSON file.
    6. Allow viewing today's structured appointment plan.
    7. each meeting should be in 30 min.
    8. get the user's name and reason for the appointment.
    9. If the user doesn't provide a date, assume it's today.
    """,
    llm="gemini/gemini-1.5-flash-8b"
)

while(True):
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    planning_response = appointment_agent.start(user_input)
    print("Agent :", planning_response)