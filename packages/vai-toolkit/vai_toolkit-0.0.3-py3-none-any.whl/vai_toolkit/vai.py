import requests
import json
from os.path import exists

# base_url = "http://localhost:1333/api/v1"
# base_url = "https://dev-cloud-api.virtuousai.com/api/v1"
base_url = "https://cloud-api.virtuousai.com/api/v1"

def upload_data(data, date, time, pipeline, userSecret, **optional_params):
    request_url = base_url + "/add-multiple-json-data"
    headers = {"pipeline": pipeline, "user-secret" : userSecret}
    allowNewColumns = False
    allowDuplicate = False
    allowNewCategory = False
    if ('allow_new_columns' in optional_params):
        allowNewColumns = optional_params['allow_new_columns']
    if ('allow_duplicate' in optional_params):
        allowDuplicate = optional_params['allow_duplicate']
    if ('allow_new_category' in optional_params):
        allowNewCategory = optional_params['allow_new_category']
    payload = json.dumps({ 
        "date": date,
        "data": data,
        "time" : time,
        "allowNewColumns" : allowNewColumns,
        "allowDuplicate" : allowDuplicate,
        "allowNewCategory" : allowNewCategory
    })
    response = requests.post(request_url, data=payload, headers=headers)
    res = json.loads(response.text)
    if ('message' in res):
        return res['message']
    else :
        return res

def explain(datasetData, modelId, dataset, pipeline, userSecret):
    request_url = base_url + "/explainability-predications-output"
    headers = {"pipeline": pipeline, "user-secret" : userSecret}

    payload = json.dumps({ 
        "datasetData": datasetData,
        "modelId": modelId,
        "dataset" : dataset
    })
    response = requests.post(request_url, data=payload, headers=headers)
    res = json.loads(response.text)
    if ('message' in res):
        return res['message']
    else :
        return res

def download_data(date, path, pipeline, userSecret):
    file_exists = exists(path)
    if(file_exists) :
        request_url = base_url + "/insight-download-multiple-dataset?date=" + date
        headers = {"pipeline": pipeline, "user-secret" : userSecret}
    
        response = requests.get(request_url, headers=headers)
        if(response.status_code == 200) :
            f = open(path, 'w', encoding='UTF8', newline='')
            f.write(response.text)
            f.close()
            return "File saved successfully"
        else :
            res = json.loads(response.text)
            if ('message' in res):
                return res['message']
            else :
                return res
    else :
        return "File path not exists"

def download_multiple_data(from_date, to_date, path, pipeline, userSecret):
    file_exists = exists(path)
    if(file_exists) :
        request_url = base_url + "/insight-download-multiple-dataset?fromDate=" + from_date + "&toDate=" + to_date
        headers = {"pipeline": pipeline, "user-secret" : userSecret}
    
        response = requests.get(request_url, headers=headers)
        if(response.status_code == 200) :
            f = open(path, 'wb')
            f.write(response.content)
            f.close()
            return "File saved successfully"
        else :
            res = json.loads(response.text)
            if ('message' in res):
                return res['message']
            else :
                return res
    else :
        return "File path not exists"
