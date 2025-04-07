
from yougile_project import Yougile
gile = Yougile(base_url = "https://ru.yougile.com/api-v2", headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Barer '
} )
user = "5992b355-0fe7-4b4a-9d23-217353170272"

#создать компанию
def test_create_project():
    title = "Грозный 12"
    resp = gile.create_project(title,user)
    assert resp.status_code == 201


def test_negative_creat_progetc():
    title_negativ = ""
    resp = gile.create_project(title_negativ,user)
    assert resp.json()["message"] == ["title should not be empty"]
    assert resp.status_code == 400


# изменить проект
def test_edit():
    title = 'Москва'
    resp = gile.edit_project(title,user)
    assert resp.json().get("title") == None
    assert resp.status_code == 200

#Тест с неверным ID
def test_negative_edit():
    title = 'Москва'
    resp = gile.edit_project_negative(title,user)
    assert resp.status_code == 404


#Получть по ID
def test_get():
    title = "Калининград"
    resp = gile.get_project(title,user)
    assert resp.json().get("title") == title
    assert resp.status_code == 200


def test_get_negative():
    title = "Космос"
    resp = gile.get_project_negative(title,user)
    assert resp.json().get("title") == None
    assert resp.status_code == 404






