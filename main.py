from src.document_loader import load_pdf_document, load_docx_document
from src.chatbot import setup_openai_api, ask_openai
from src.rabbitmq_client import send_message_to_queue


def main():
    # Configurar a API da OpenAI
    setup_openai_api(api_key="sua_key")

    # Carregar documentos (exemplo)
    pdf_document = load_pdf_document("docs/SeuCurriculo.pdf")
    # docx_document = load_docx_document('docs/seu_documento.docx')

    # Exemplo de interação com o chatbot
    resposta = ask_openai("Quais são as principais ideias deste documento?")
    print(resposta)

    # Enviar mensagem para RabbitMQ (exemplo)
    send_message_to_queue("Mensagem de exemplo")


if __name__ == "__main__":
    main()
