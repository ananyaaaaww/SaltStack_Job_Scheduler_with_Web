from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated  # Example permission class
import requests 
import logging
import json 
import os

logger = logging.getLogger('django')

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
    return response.json()["return"]

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
    beautified_data = json.dumps(data, indent=4)
    print(beautified_data)

    if isinstance(data, list) and len(data) == 1:  # Check for list with one element
        minion_data = data[0]  # Access the single dictionary
        if isinstance(minion_data, dict):
            minion_status = minion_data.get("Minion1")  # Get value for "Minion1" key (or None if missing)
            if minion_status:
                # Check for enabled state and print accordingly
                if "enabled: true" in minion_status:
                    print(f"Minion1 Status:\n{minion_status}")
                else:
                    print("Minion1: NO JOB SCHEDULED")
            else:
                print("No data found for Minion1")
        else:
            print("Unexpected data format within list")
    else:
        print("Unexpected data format")

    return beautified_data  # You can still return the raw data if needed


def add_form_view(request):
    # For add job schedule page
    if request.method == 'POST':
        salt_function = request.POST.get('salt_function', '')
        target_minion = request.POST.get('target_minion', '')
        jobname = request.POST.get('jobname', '')
        commandname = request.POST.get('commandname','')
        scheduleType= request.POST.get('scheduleType','')
        intervalUnit=request.POST.get('intervalUnit','')
        intervalValue=request.POST.get('intervalValue','')
        cronExpression=request.POST.get('cronExpression','')
        res = add_job(target=target_minion, jobname=jobname,commandname=commandname,scheduleType=scheduleType,intervalUnit=intervalUnit,intervalValue=intervalValue,cronExpression=cronExpression)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        print("jobname:", jobname)
        print('command name:', commandname)
        print('scheduleType:',scheduleType)
        print('intervalUnit:',intervalUnit)
        print('intervalValue:',intervalValue)
        print('cronExpression:',cronExpression)
        return HttpResponse(res)
    return render(request, 'add.html')

def add_job(target,jobname,commandname,scheduleType,intervalUnit,intervalValue,cronExpression):
    # For adding jobs
    api_url = f"http://192.168.64.16:8000/run"
    print(scheduleType)
    data = {
        "client": "local",
        "tgt": target,
        "fun": "schedule.add",
        "arg": [jobname],
        "kwarg": {
            "function": commandname,                
        },
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    } 
    
    if scheduleType == "cron":
        # Add cron expression to kwarg
        data["kwarg"]["cron"] = cronExpression # Replace with user-provided cron expression
    elif scheduleType == "timeInterval":
        # Add interval and unit to kwarg (ensure schedule_value and schedule_unit have values)
        if intervalUnit is None or intervalValue is None:
           raise ValueError("Missing schedule_value or schedule_unit for time interval")
        data["kwarg"]["kwargs"] = {  # Nested dictionary for interval and unit
           "interval": intervalValue,
           "unit": intervalUnit
        }
    else:
        raise ValueError("Invalid schedule_type. Must be 'cron' or 'timeInterval'")

    response = requests.post(api_url, json=data)
    return response.json()["return"]

def modify_form_view(request):
    # For modify job schedule page
    if request.method == 'POST':
        salt_function = request.POST.get('salt_function', '')
        target_minion = request.POST.get('target_minion', '')
        jobname = request.POST.get('jobname', '')
        commandname = request.POST.get('commandname','')
        res = modify_job(target=target_minion, jobname=jobname,commandname=commandname)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        print("jobname:", jobname)
        print('command name:', commandname)
        return HttpResponse(res)
    return render(request, 'modify.html')

def modify_job(target,jobname,commandname):
    # For modifying jobs
    api_url = f"http://192.168.64.16:8000/run"

    data = {
        "client": "local",
        "tgt": target,
        "fun": "schedule.modify",
        "arg": [jobname],
        "kwarg": {
            "function": commandname,
            "seconds": 3600
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
        scriptarea = request.POST.get('scriptarea','')
        res = script_schedule(target=target_minion, jobname=jobname,scriptarea=scriptarea)
        print(res)
        print("Salt Function:",  salt_function)  
        print("Target Node:", target_minion)
        print("jobname:", jobname)
        print('scriptarea:', scriptarea)
        return HttpResponse(res)
    return render(request, 'script.html')

def script_schedule(target,jobname,scriptarea):
    # For schedule a script
    api_url = f"http://192.168.64.16:8000/run"

    data = {
        "client": "local",
        "tgt": target,
        "fun": "schedule.add",
        "arg": [jobname],
        "kwarg": {
            "function": "cmd.run",
            "job_args": scriptarea,
            "seconds": 3600
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