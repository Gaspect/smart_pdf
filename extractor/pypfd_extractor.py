from extractor_base.extractor  import Extractor, IO, Dict, Any
from extractor.utils import *
from PyPDF4.pdf import PdfFileReader, DocumentInformation
from PyPDF4.xmp import XmpInformation



class PyPdfExtractor(Extractor):
    '''
    Basic extractor using PyPDf4 
    '''
    __xmp_fields = ['dc_contributor', 'dc_coverage', 'dc_creator', 'dc_date', 'dc_description', 'dc_format',
                    'dc_identifier', 'dc_language', 'dc_publisher', 'dc_relation', 'dc_rights', 'dc_source', 'dc_subject', 'dc_title',
                    'dc_type', 'pdf_keywords', 'pdf_pdfversion', 'pdf_producer', 'xmp_createDate', 'xmp_modifyDate',
                    'xmp_metadataDate', 'xmp_creatorTool', 'xmpmm_documentId', 'xmpmm_instanceId']

    class_alias = 'metadatos'
    def get_info(self, pdf:IO, passwor:str = None)->Dict[str,Any]:
        file_reader = PdfFileReader(pdf,strict=False)
        info:DocumentInformation =clean_info(file_reader.getDocumentInfo())

        try:
            xmp = file_reader.getXmpMetadata()
        except Exception:
            return info
            
        if xmp is not None:
            for x in self.__xmp_fields:
               info[x] = xmp.__getattribute__(x)
        return info