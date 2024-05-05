def handle_uploaded_file(f):  
    # for file upload in device
    with open('new/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  