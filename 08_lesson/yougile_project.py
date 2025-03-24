import requests


class Yougile:
    def __init__(self, base_url, headers):
        self.url = base_url + '/projects'
        self.headers = headers

    def create_project(self, title, id_user):
        body = {
            "title": title,
            "users": { id_user: "admin" }
        }
        resp = requests.post(self.url, json=body, headers=self.headers)
        return resp

    def edit_project(self, title, id_user):
        resp = self.create_project(title,id_user)
        project_id = resp.json()
        new_id = project_id['id']
        url_with_id = f'{self.url}/{new_id}'
        resp = requests.put(url_with_id, headers= self.headers)
        return resp

    def edit_project_negative(self, title, id_user):
        resp = self.create_project(title,id_user)
        project_id = resp.json()
        new_id = project_id['id']
        url_with_id = f'{self.url}/{new_id}//'
        resp = requests.put(url_with_id, headers= self.headers)
        return resp


    def get_project(self,title,id_user):
        resp = self.create_project(title, id_user)
        project_id = resp.json()
        new_id = project_id['id']
        url_with_id = f'{self.url}/{new_id}'
        resp = requests.get(url_with_id, headers=self.headers)
        return resp

    def get_project_negative(self,title,id_user):
        resp = self.create_project(title, id_user)
        project_id = resp.json()
        new_id = project_id['id']
        url_with_id = f'{self.url}/{new_id}///'
        resp = requests.get(url_with_id, headers=self.headers)
        return resp