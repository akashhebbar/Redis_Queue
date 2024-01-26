
Step1: Install Requirements

pip install -r requirements.tx

Step 2: Run FastAPI project

uvicorn main:app --port 10000 --reload

Step 3: Run Redis worker(optional)
rq worker task_queue


Note: Redis must be installed on system