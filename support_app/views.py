from django.shortcuts import render
from .rag import get_answer

chat_history = []

def chat(request):

    if request.method == "POST":

        question = request.POST.get("question")

        result = get_answer(question)

        chat_history.append({
            "question": question,
            "answer": result["answer"],
            "pages": result["pages"],
            "confidence": result["confidence"]
        })

    return render(
        request,
        "support_app/chat.html",
        {
            "chat_history": chat_history
        }
    )