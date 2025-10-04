from rest_framework import serializers
from .models import TrainingData, AnalysisResult
import json

class TrainingDataSerializer(serializers.ModelSerializer):
    data = serializers.JSONField()

    class Meta:
        model = TrainingData
        fields = ['id', 'created_at', 'data', 'status']

    def to_internal_value(self, data):
        if 'data' in data:
            data['data'] = json.dumps(data['data'])
        return super().to_internal_value(data)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['data'] = json.loads(ret['data'])
        return ret

class AnalysisResultSerializer(serializers.ModelSerializer):
    input_data = serializers.JSONField()
    result = serializers.JSONField()

    class Meta:
        model = AnalysisResult
        fields = ['id', 'created_at', 'input_data', 'result']

    def to_internal_value(self, data):
        if 'input_data' in data:
            data['input_data'] = json.dumps(data['input_data'])
        if 'result' in data:
            data['result'] = json.dumps(data['result'])
        return super().to_internal_value(data)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['input_data'] = json.loads(ret['input_data'])
        ret['result'] = json.loads(ret['result'])
        return ret
