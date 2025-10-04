from django.db import models
import json

class TrainingData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.TextField()  # Will store JSON as text
    status = models.CharField(max_length=20, default='pending')

    def set_data(self, data):
        self.data = json.dumps(data)

    def get_data(self):
        return json.loads(self.data)

class AnalysisResult(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    input_data = models.TextField()  # Will store JSON as text
    result = models.TextField()  # Will store JSON as text

    def set_input_data(self, data):
        self.input_data = json.dumps(data)

    def get_input_data(self):
        return json.loads(self.input_data)

    def set_result(self, data):
        self.result = json.dumps(data)

    def get_result(self):
        return json.loads(self.result)
