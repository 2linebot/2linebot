from apscheduler.schedulers.blocking import BlockingScheduler

sched=BlockingScheduler()

@sched.scheduled_job('cron', hour=6-23, minute=0-59)
def job():
    print('This job runs every minute from 6h00 to 23h59')

sched.start()
