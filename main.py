from fastapi import FastAPI
import requests
from datetime import datetime

app = FastAPI()

cookies = {
    'renderCtx': '%7B%22pageId%22%3A%22256f9290-63af-455e-8f4a-1cbb83adcb31%22%2C%22schema%22%3A%22Published%22%2C%22viewType%22%3A%22Published%22%2C%22brandingSetId%22%3A%22439164cc-6713-4d9c-8d42-f31ed1a81787%22%2C%22audienceIds%22%3A%226Au2p000000kB4L%2C6Au2p000000Xbun%2C6Au2p000000TNPF%2C6Au2p0000008Qm1%2C6Au2p0000008QnE%22%7D',
    'CookieConsentPolicy': '0:1',
    'LSKey-c^$CookieConsentPolicy': '0:1',
    'pctrk': 'cfa5297f-eb05-454d-957a-9c1f1f19abda',
    'sfdc-stream': '^!O0+HqbMSrCBsoH8kWVaS7rStzXXjEecNmnWfgs+JTSavM6E5sV52GCd3aPcE91WhYkSemv8ITaf2XcE=',
    'PicassoLanguage72f1cb12-99d8-40bf-b387-a4fd57a5d99dPublished': 'bfea51f0-5f75-4422-9370-8b8b86d241a5',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://careers.emeal.nttdata.com',
    'referer': 'https://careers.emeal.nttdata.com/s/jobs?language=pt_BR',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-b3-sampled': '0',
    'x-b3-spanid': '6ad5e6f84e1633b1',
    'x-b3-traceid': 'df0f913fe03ac46a',
    'x-sfdc-page-scope-id': '3e802523-bcbe-41f9-8a54-db5a07cd7c61',
    'x-sfdc-request-id': '37000200000a0163e5',
}

params = {
    'r': '6',
    'other.JobOffer.getOffersFilterMulti': '1',
}

data = {
    'message': '{"actions":[{"id":"6616;a","descriptor":"apex://JobOfferController/ACTION$getOffersFilterMulti","callingDescriptor":"markup://c:JobOfferFrida","params":{"param":"{\\"country\\":\\"Brasil\\",\\"office\\":\\"\\",\\"speciality\\":\\"\\",\\"experient\\":\\"\\",\\"modality\\":\\"\\",\\"text\\":\\"\\"}"}}]}',
    'aura.context': '{"mode":"PROD","fwuid":"c1ItM3NYNWFUOE5oQkUwZk1sYW1vQWg5TGxiTHU3MEQ5RnBMM0VzVXc1cmcxMS4zMjc2OC4z","app":"siteforce:communityApp","loaded":{"APPLICATION@markup://siteforce:communityApp":"1237_QCP5Ih0RUYVLF144CXYCOA"},"dn":[],"globals":{},"uad":true}',
    'aura.pageURI': '/s/jobs?language=pt_BR',
    'aura.token': 'null',
}

@app.get("/get-offers")
def get_offers():
    response = requests.post(
        'https://careers.emeal.nttdata.com/s/sfsites/aura',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    return {
        "status_code": response.status_code,
        "data": response.json() if response.headers.get('Content-Type') == 'application/json' else response.text
    }

#GUPY API ESTAGIARIO

headers = {
    'Accept': 'application/json',
    'Cache-Control': 'no-cache',
}

params = {
    'jobName': 'estagiario^',
    'workplaceType': 'remote',
    'offset': '0',
}


@app.get("/gupy-jobs")
def gupy_jobs():
    response = requests.get('https://portal.api.gupy.io/api/v1/jobs', params=params, headers=headers)
    return {
        "status_code": response.status_code,
        "data": response.json() if response.headers.get('Content-Type') == 'application/json' else response.text
    }
    
#GUPY API ESTAGIO

headers = {
    'Accept': 'application/json',
    'Cache-Control': 'no-cache',
}

params = {
    'jobName': 'estagio^',
    'workplaceType': 'remote',
    'offset': '0',
}


@app.get("/gupy-jobs-estagio")
def gupy_jobs():
    response = requests.get('https://portal.api.gupy.io/api/v1/jobs', params=params, headers=headers)
    return {
        "status_code": response.status_code,
        "data": response.json() if response.headers.get('Content-Type') == 'application/json' else response.text
    }
    
    
# NTT DATA API ESTAGIARIO

datet = datetime.today().strftime('%Y-%m-%d')
cookies = {
    'TS018608fa': '01a760ec214fbb69eae9c1db2ed9d7217dd9afe0ab9edba22ec8792ee176a3abfa33329a7ea09922111f46c1aad9039ff94a89da4e',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'pt-BR',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://platform.senior.com.br',
    'priority': 'u=1, i',
    'referer': 'https://platform.senior.com.br/hcmrs/hcm/curriculo/?tenant=fhcombr&tenantdomain=fh.com.br&fromRecruitment=false',
    'sec-ch-ua': '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-tenant': 'fhcombr',
    'x-tenantdomain': 'fh.com.br',
    # 'Cookie': 'TS018608fa=01a760ec214fbb69eae9c1db2ed9d7217dd9afe0ab9edba22ec8792ee176a3abfa33329a7ea09922111f46c1aad9039ff94a89da4e',
}

json_data = {
    'q': '',
    'hqId': '',
    'currentDate': datet,
    'order': 'HIGHLIGHT',
    'page': 0,
    'size': 35,
}

@app.get("/ntt-conexos")
def gupy_jobs():
    response = requests.post(
    'https://platform.senior.com.br/t/senior.com.br/bridge/1.0/anonymous/rest/hcm/vacancymanagement/queries/searchPublicVacancies',
    cookies=cookies,
    headers=headers,
    json=json_data,
    )
    return {
        "status_code": response.status_code,
        "data": response.json() if response.headers.get('Content-Type') == 'application/json' else response.text
    }