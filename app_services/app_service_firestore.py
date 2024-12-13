from google.cloud import firestore
import datetime
import os

db = firestore.Client(project=os.getenv("PROJECT_ID"))

def save_feedback(module,feature,feedback, question,answer):
    data = {
        "module": module,
        "feature": feature,
        "feedback": feedback,
        "question": question,
        "answer":answer
    }
    db.collection("feedbacks").document(str(datetime.datetime.now(tz=datetime.timezone.utc))).set(data)