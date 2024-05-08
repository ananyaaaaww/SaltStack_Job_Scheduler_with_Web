from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated  # Example permission class
import requests 
import logging
import json 
import os
from new.functions import handle_uploaded_file  
from new.forms import StudentForm  

logger = logging.getLogger('django')

def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"testfile.html",{'form':student})  

def home_form_view(request):
    # For home page
    if request.method == 'POST':
        salt_function = request.POST.get('salt_function', '')
        target_minion = request.POST.get('target_minion', '')
        jobname = request.POST.get('jobname', '')
        commandname = request.POST.get('commandname','')
        res = add_job(target=target_minion, function=salt_function,jobname=jobname,commandname=commandname)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        print("jobname:", jobname)
        print('command name:', commandname)
        return HttpResponse(res)
    return render(request, 'home.html') 

def delete_form_view(request):
    # For delete schedule page
    if request.method == 'POST':
        salt_function = request.POST.get('salt_function', '')
        target_minion = request.POST.get('target_minion', '')
        jobname = request.POST.get('jobname', '')
        res = deletejob(target=target_minion, jobname=jobname)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        print("jobname:", jobname)
        return HttpResponse(res)
    return render(request, 'delete.html')

def deletejob(target, jobname):
    # For delete job 
    api_url = f"http://192.168.64.16:8000/run"

    data = {
        "client": "local",
        "tgt": target,
        "fun": "schedule.delete",
        "arg": [jobname],
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    } 

    response = requests.post(api_url, json=data)
    data = response.json()["return"]
    data1=data[0]
    return data1

def enable_form_view(request):
    # For enable schedule page
    if request.method == 'POST':
        salt_function = request.POST.get('salt_function', '')
        target_minion = request.POST.get('target_minion', '')
        jobname = request.POST.get('jobname', '')
        res = enablejob(target=target_minion, jobname=jobname)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        print("jobname:", jobname)
        return HttpResponse(res)
    return render(request, 'enable.html')

def enablejob(target, jobname):
    # For enable job 
    api_url = f"http://192.168.64.16:8000/run"

    data = {
        "client": "local",
        "tgt": target,
        "fun": "schedule.enable_job",
        "arg": [jobname],
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    } 

    response = requests.post(api_url, json=data)
    return response.json()["return"]

def disable_form_view(request):
    # For disable schedule page
    if request.method == 'POST':
        salt_function = request.POST.get('salt_function', '')
        target_minion = request.POST.get('target_minion', '')
        jobname = request.POST.get('jobname', '')
        res = disablejob(target=target_minion, jobname=jobname)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        print("jobname:", jobname)
        return HttpResponse(res)
    return render(request, 'disable.html')

def disablejob(target, jobname):
    # For disable job 
    api_url = f"http://192.168.64.16:8000/run"

    data = {
        "client": "local",
        "tgt": target,
        "fun": "schedule.disable_job",
        "arg": [jobname],
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    } 

    response = requests.post(api_url, json=data)
    return response.json()["return"]

def status_form_view(request):
    # For job status schedule page
    if request.method == 'POST':
        salt_function = request.POST.get('salt_function', '')
        target_minion = request.POST.get('target_minion', '')
        jobname = request.POST.get('jobname', '')
        res = statusjob(target=target_minion, jobname=jobname)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        print("jobname:", jobname)
        return HttpResponse(res)
    return render(request, 'job_status.html')

def statusjob(target, jobname):
    # For job status 
    api_url = f"http://192.168.64.16:8000/run"

    data = {
        "client": "local",
        "tgt": target,
        "fun": "schedule.job_status", 
        "arg": [jobname],
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    } 

    response = requests.post(api_url, json=data)
    return response.json()["return"]

def runjob_form_view(request):
    # For run job schedule page
    if request.method == 'POST':
        salt_function = request.POST.get('salt_function', '')
        target_minion = request.POST.get('target_minion', '')
        jobname = request.POST.get('jobname', '')
        res = runjob(target=target_minion, jobname=jobname)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        print("jobname:", jobname)
        return HttpResponse(res)
    return render(request, 'run_job.html')

def runjob(target, jobname):
    # For run job 
    api_url = f"http://192.168.64.16:8000/run"

    data = {
        "client": "local",
        "tgt": target,
        "fun": "schedule.run_job", 
        "arg": [jobname], 
        "force": "True",
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    } 

    response = requests.post(api_url, json=data)
    return response.json()["return"]

def purge_form_view(request):
    # For Purge job schedule page
    if request.method == 'POST':
        salt_function = request.POST.get('salt_function', '')
        target_minion = request.POST.get('target_minion', '')
        res = purgejob(target=target_minion)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        return HttpResponse(res)
    return render(request, 'purge.html')

def purgejob(target):
    # For purge jobs
    api_url = f"http://192.168.64.16:8000/run"

    data = {
        "client": "local",
        "tgt": target,
        "fun": "schedule.purge",
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    }

    response = requests.post(api_url, json=data)
    return response.json()["return"]

def reload_form_view(request):
    # For reload job schedule page
    if request.method == 'POST':
        salt_function = request.POST.get('salt_function', '')
        target_minion = request.POST.get('target_minion', '')
        res = reloadjob(target=target_minion)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        return HttpResponse(res)
    return render(request, 'reload.html')

def reloadjob(target):
    # For reload jobs
    api_url = f"http://192.168.64.16:8000/run"

    data = {
        "client": "local",
        "tgt": target,
        "fun": "schedule.reload",
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    }

    response = requests.post(api_url, json=data)
    return response.json()["return"]

def list_form_view(request):
    # For list job schedule page
    if request.method == 'POST':
        salt_function = request.POST.get('salt_function', '')
        target_minion = request.POST.get('target_minion', '')
        res = listjob(target=target_minion)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        return HttpResponse(res)
    return render(request, 'list.html')

def listjob(target):
    # For list of jobs
    api_url = f"http://192.168.64.16:8000/run"

    data = {
        "client": "local",
        "tgt": target,
        "fun": "schedule.list",
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    }

    response = requests.post(api_url, json=data)
    data = response.json()["return"]
    data1 = (data[0][target])

    # Return the formatted data
    return data1 

def add_form_view(request):
    # For add job schedule page
    if request.method == 'POST':
        salt_function = request.POST.get('salt_function', '')
        target_minion = request.POST.get('target_minion', '')
        jobname = request.POST.get('jobname', '')
        commandname = request.POST.get('commandname','')
        intervalUnit = request.POST.get('intervalUnit','')
        intervalValue = request.POST.get('intervalValue','')
        res = add_job(target=target_minion, jobname=jobname,commandname=commandname,intervalUnit=intervalUnit,intervalValue=intervalValue)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        print("jobname:", jobname)
        print('command name:', commandname)
        print('intervalUnit:',intervalUnit)
        print('intervalValue:',intervalValue)
        return HttpResponse(res)
    return render(request, 'add.html')

def add_job(target,jobname,commandname,intervalUnit,intervalValue):
    # For adding jobs
    api_url = f"http://192.168.64.16:8000/run"
    data = {
        "client": "local",
        "tgt": target,
        "fun": "schedule.add",
        "arg": [jobname],
        "kwarg": {
            "function": commandname,  
            intervalUnit: intervalValue,         
        },
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    }

    response = requests.post(api_url, json=data)
    data= response.json()["return"]
    return data

def modify_form_view(request):
    # For modify job schedule page
    if request.method == 'POST':
        salt_function = request.POST.get('salt_function', '')
        target_minion = request.POST.get('target_minion', '')
        jobname = request.POST.get('jobname', '')
        commandname = request.POST.get('commandname','')
        intervalUnit = request.POST.get('intervalUnit','')
        intervalValue = request.POST.get('intervalValue','')
        res = modify_job(target=target_minion, jobname=jobname,commandname=commandname, intervalUnit=intervalUnit,intervalValue=intervalValue)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        print("jobname:", jobname)
        print('command name:', commandname)
        print('intervalUnit:',intervalUnit)
        print('intervalValue:',intervalValue)
        return HttpResponse(res)
    return render(request, 'modify.html')

def modify_job(target,jobname,commandname,intervalUnit,intervalValue):
    # For modifying jobs
    api_url = f"http://192.168.64.16:8000/run"

    data = {
        "client": "local",
        "tgt": target,
        "fun": "schedule.modify",
        "arg": [jobname],
        "kwarg": {
            "function": commandname,
            intervalUnit: intervalValue, 
        },
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    } 

    response = requests.post(api_url, json=data)
    return response.json()["return"]

def script_form_view(request):
    # For schedule a script page
    if request.method == 'POST':
        salt_function = request.POST.get('salt_function', '')
        target_minion = request.POST.get('target_minion', '')
        jobname = request.POST.get('jobname', '')
        intervalUnit = request.POST.get('intervalUnit','')
        intervalValue = request.POST.get('intervalValue','')
        res = script_schedule(target=target_minion, jobname=jobname, intervalUnit=intervalUnit,intervalValue=intervalValue)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        print("jobname:", jobname)
        print('intervalUnit:',intervalUnit)
        print('intervalValue:',intervalValue)
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
        else:  
            student = StudentForm()  
        return HttpResponse(res)
    return render(request, 'script.html')

def filetransfer(file):
    api_url = "http://192.168.64.16:8000/run"
    local_file_path = "/Users/ananya1.intern/Documents/test/" + file

# Read the content of the local file
    try:
        with open(local_file_path, "r") as f:
            file_content = f.read()
    except FileNotFoundError:
        print(f"File '{local_file_path}' not found.")
        exit()
    data = {
        "client": "wheel",
        "fun": "file_roots.write",
        "path": "file.sh",  # Specify the path where you want to write the file
        "saltenv": "base",
        "data": file_content,  # Content of the file you want to write
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    }
    
    response = requests.post(api_url, json=data)
    return response.json()["return"]

def script_schedule(target,jobname, intervalUnit, intervalValue):
    # For schedule a script
    api_url = f"http://192.168.64.16:8000/run"

    data = {
        "client": "local",
        "tgt": target,
        "fun": "schedule.add",
        "arg": [jobname],
        "kwarg": {
            "function": "cmd.run",
            "job_args": ['/home/ubuntu/test/file.sh'],
            intervalUnit: intervalValue, 
        },
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    } 

    response = requests.post(api_url, json=data)
    return response.json()["return"]

class SaltFunctionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Extract function name, target(s), and arguments from request data
        function_name = request.data['function']
        target = request.data['target']
        jobname = request.data['jobname']
        commandname = request.data['commandname']

        # Authentication: Include API token or other credentials in headers
        salt_api_token = os.environ.get('SALT_API_TOKEN')
        headers = {'Authorization': f'Token {salt_api_token}'} # Example using token authentication

        # Salt API URL (replace with your actual master address and port)
        salt_api_url = 'http://192.168.64.16:8000'

        # Construct the Salt API request payload
        data = {
            'client': 'local',  # Use a specific client if needed
            'tgt': target,
            'fun': function_name,
            'jobname': jobname,
            'commandname':commandname,
        }