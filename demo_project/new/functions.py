def handle_uploaded_file(f):  
    # for file upload in device
    with open('/Users/ananya1.intern/Documents/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  