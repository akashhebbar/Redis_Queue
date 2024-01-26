from fastapi import FastAPI
from redis import Redis
from rq import Queue
from pydantic import BaseModel
from job import print_numbers

app = FastAPI()
# redis connection

redis_con = Redis(host="localhost", port=6379)
task_queue = Queue("task_queue", connection=redis_con)


class JobItem(BaseModel):
    end: int


@app.get("/")
def homage_page():
    return {"message": "Welcome to Redis Queue"}


@app.post("/task")
def post_job(job: JobItem):
    end = job.end
    queued_job = task_queue.enqueue(print_numbers, end)
    return {"success": True, "job_id": queued_job.id}
