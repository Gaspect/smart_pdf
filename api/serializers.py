from rest_framework import serializers
from rest_framework.fields import Field
from django.core.validators import FileExtensionValidator

class CustomSerializer(serializers.Serializer):
    file = serializers.FileField(validators= [FileExtensionValidator(allowed_extensions=['pdf'])], 
                                 allow_empty_file=False, use_url=False,
                                 style={'base_template': 'pdf_input.html'},
                                 label = 'Choose a file...')