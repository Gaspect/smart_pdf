from rest_framework import views, response, request, status
from django.core.files.uploadedfile import InMemoryUploadedFile
from api.serializers import CustomSerializer
from django.conf import settings
from extractor_base.extractor import Extractor
'''
Main class for this API, implement the logic related to how show 
the results of the diferents info extractors 
'''
class PdfAPI(views.APIView):   
    serializer_class = CustomSerializer
    extractor:Extractor = None
    name = 'Pdf APi'

    def get_extractor(self):
        '''
        Return the extractor in the class field 'extractor' if teh field is a 'AbstractInfoExtractor' type
        the method generate a instance and return it, in case that the field is None raise an exeception
        '''
        if self.extractor  is None:
            raise Exception("The extractor is None, this can't hapen, for fix the bug you must pass a extractor in \
                    the call of 'as_view' method or properly asign the field extractor or override the 'get_extractor'\
                    methdo in a class child of PdfApi class.")
        if isinstance(self.extractor, Extractor):
            return self.extractor
        return self.extractor()

    def post(self, request:request.Request, format = None):
        '''
        The method that process a post request and return a response with the data calculated by the info extractors
        can be overrided for alternative implementation
        '''
        c_serializer = CustomSerializer(data = request.data)

        if c_serializer.is_valid():
            with request.data['file'] as f:
                try:
                    data = self.get_extractor().get_info(f)
                    return response.Response(data)
                except :
                    return response.Response(data={'File':'The file is not recognized as a pdf, make sure it is in good condition'}, 
                                             status = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

        return response.Response(data=c_serializer.errors, status = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)