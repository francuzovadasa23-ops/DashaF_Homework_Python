import os
from dotenv import load_dotenv
import requests


load_dotenv()


class ProjectApi:
    def __init__(self, url):
        self.url = url
        self.token = os.getenv("TOKEN")

    def get_projects_list(self, token):
        auth = {
            'token': token,
        }
        resp = requests.get(self.url + '/projects', json=auth)
        return resp.json()

    def create_project(self, token, title, users_dict):
        project = {
            'title': title,
            'users': users_dict
        }
        headers = {
            'Authorization': f'Bearer {token}',
        }
        resp = requests.post(
            self.url + '/projects', json=project, headers=headers)
        return resp.json()

    def create_project_raw(self, token, title, users_dict):
        project = {
            'title': title,
            'users': users_dict
        }
        headers = {
            'Authorization': f'Bearer {token}',
        }
        resp = requests.post(
            self.url + '/projects', json=project, headers=headers)
        return resp

    def edit_project(self, token, id, new_title):
        url = f'{self.url}/projects/{id}'
        project = {
            'title': new_title,
        }
        headers = {
            'Authorization': f'Bearer {token}',
        }
        resp = requests.put(url, json=project, headers=headers)
        return resp.json()

    def edit_project_raw(self, token, id, new_title):
        url = f'{self.url}/projects/{id}'
        project = {
            'title': new_title,
        }
        headers = {
            'Authorization': f'Bearer {token}',
        }
        resp = requests.put(url, json=project, headers=headers)
        return resp

    def get_project(self, token, id):
        url = f'{self.url}/projects/{id}'
        headers = {
            'Authorization': f'Bearer {token}',
        }
        resp = requests.get(url, headers=headers)
        return resp.json()

    def get_project_raw(self, token, id):
        url = f'{self.url}/projects/{id}'
        headers = {
            'Authorization': f'Bearer {token}',
        }
        resp = requests.get(url, headers=headers)
        return resp
