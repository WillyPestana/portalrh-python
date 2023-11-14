from langchain.document_loaders import PyPDFLoader, Docx2txtLoader


def load_pdf_document(path):
    pdf_loader = PyPDFLoader(path)
    return pdf_loader.load()


def load_docx_document(path):
    docx_loader = Docx2txtLoader(path)
    return docx_loader.load()
