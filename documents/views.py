from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UploadedDocumentForm
from .models import UploadedDocument


@login_required
def document_list(request):
    documents = UploadedDocument.objects.filter(user=request.user)
    return render(request, "documents/list.html", {"documents": documents})


@login_required
def document_upload(request):
    if request.method == "POST":
        form = UploadedDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save()
            return redirect("document_list")
    else:
        form = UploadedDocumentForm()
    return render(request, "documents/upload.html", {"form": form})

