from apscheduler.schedulers.blocking import BlockingScheduler
from chatbot import irritating_message

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(irritating_message, 'interval', seconds=10)

sched.start()