
#  Author:  Daniel Morvay
#  Creator Email:  morvayd@gmail.com

#
#  ---------- Install Additional Libraries ---------- 
#
#  Reference:  https://docling-project.github.io/docling/getting_started/installation/
#  docling install options [asr, vlm, easyocr, tesserocr, ocrmac, rapidocr]
pip install docling

#
#  ---------- Run Using Internet Connection ----------
#

#  Reference:  https://github.com/docling-project/docling

from docling.document_converter import DocumentConverter

#  source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL

source = "C:/Users/dan1/R/PythonWorkArea/docling testing/2408.09869v5.pdf"
converter = DocumentConverter()
result = converter.convert(source)
strExtract = result.document.export_to_markdown() 

#  Find docling models at ~/.cache/docling
#  Model Location Using the above code: C:\Users\morva\.cache\huggingface\hub\
#  huggingface/hub/models--ds4sd--docling--layout-heron/
#  huggingface/hub/models--ds4sd--docling-models/
#  huggingface/xet/https___cas_serv-tGqkUaZf_CBPHQ6h/
#  huggingface/xet/logs/

#
#  ---------- Prepare for Offline ----------
#

#  Need to download models (easyocr) - quotes are important
pip install "docling[easyocr]"
#  ---- better more robust ----
pip install easyocr
pip install rapidocr onnxruntime
#  If want to run the text extraction models using GPU only
pip install "docling-ocr-onnxtr[cpu]"

docling-tools models download
#  downloaded to ~/.cache/docling/models
#  ---- or ----
#  Python

#  Model Location using the above code:  /Users/dan1/.cache/docling/models/
#  /Users/dan1/.cache/docling/models/ds4sd--CodeFormulaV2
#  /Users/dan1/.cache/docling/models/ds4sd--docling-layout-heron
#  /Users/dan1/.cache/docling/models/ds4sd--docling-models
#  /Users/dan1/.cache/docling/models/ds4sd--DocumentFigureClassifier
#  /Users/dan1/.cache/docling/models/RapidOcr
#  /Users/dan1/.cache/huggingface/hub/models--ds4sd--docling--layout-heron/
#  /Users/dan1/.cache/huggingface/hub/models--ds4sd--docling-models
#  /Users/dan1/.cache/huggingface/hub/models--ds4sd--CodeFormulaV2
#  /Users/dan1/.cache/huggingface/hub/models-ds4sd--DocumentFigureClassifier

#  CLI
#  docling --artifacts-path=C:\Users\morva\.cache\docling\models <filename>

#
#  ---------- Run Using Internet Connection ----------
#

#  Allow EasyOCR to download the first time
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import EasyOcrOptions, PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

pipeline_options = PdfPipelineOptions()
doc_converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)

source = "https://arxiv.org/pdf/2408.09869"
result = doc_converter.convert(source)
strExtract = result.document.export_to_markdown() 

#
#  ---------- Using prefetched offline models ----------
#

#  Verify the models exist at the above cache location - no internet!
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import EasyOcrOptions, PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

artifacts_path = 'C:/Users/morva/.cache/docling/models'
pipeline_options = PdfPipelineOptions(artifacts_path=artifacts_path)
doc_converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)

source = "E:/docling/2408.09869v5.pdf"
result = doc_converter.convert(source)
strExtract = result.document.export_to_markdown() 

#  Verified offline operation! 
