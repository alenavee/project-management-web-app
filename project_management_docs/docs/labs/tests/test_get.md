# Тестирование GET-запросов

## Информация о клиенте

**URL** : `/projects/1/`

```
class ClientRetrieveTest(TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.user = User.objects.filter(pk=1)

    @classmethod
    def setUpTestData(cls):
        Client.objects.create(
            name="ООО Магазин",
            address="г. Санкт-Петербург, Лиговский пр., 10",
            contact_person="Анастасия Захарова",
            email="client1@mail.com",
            phone_number="+79838029348"
        )

    def test_retrieve_client(self):
        url = reverse('client_app:clients-detail', args=['1'])

        data = {
            "name": "ООО Магазин",
            "address": "г. Санкт-Петербург, Лиговский пр., 10",
            "contact_person": "Анастасия Захарова",
            "email": "client1@mail.com",
            "phone_number": "+79838029348"
        }

        response = self.client.force_login(user=self.user).get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)
```

## Информация о проекте

**URL** : `/projects/1/`

```
class ProjectRetrieveTest(TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.user = User.objects.filter(pk=1)
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(
            project_name="Сайт для книжного магазина",
            project_status="new",
            priority="high",
            start_date="2022-05-03",
            end_date="2022-08-01",
            project_description="Сайт для покупки книг с системой оплаты",
        )

    def test_retrieve_project(self):
        self.maxDiff = None

        url = reverse('project_app:projects-detail', args=['1'])

        data = {
            "id": 3,
            "project_name": "Сайт для книжного магазина",
            "project_status": "new",
            "priority": "high",
            "start_date": "2022-05-03",
            "end_date": "2022-08-01",
            "project_description": "Сайт для покупки книг с системой оплаты",
            "assigned_to": [],
            "department": [],
            "client": []
        }

        request_data = {k: v for k, v in data.items() if v is not None}
        response = self.client.force_login(user=self.user).get(url, request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(response_data, data)
```

## Поиск строки в названии проекта

**URL** : `/projects/filter/search/`

```
class ProjectFilterSearchTest(TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.user = User.objects.filter(pk=1)
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(
            project_name="Сайт для книжного магазина",
            project_status="new",
            priority="high",
            start_date="2022-05-03",
            end_date="2022-08-01",
            project_description="Сайт для покупки книг с системой оплаты",
        )

    def test_search_project(self):
        self.maxDiff = None
        url = reverse('project_app:projects_search')

        data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [{
                "id": 1,
                "project_name": "Сайт для книжного магазина",
                "project_status": "new",
                "priority": "high",
                "start_date": "2022-05-03",
                "end_date": "2022-08-01",
                "project_description": "Сайт для покупки книг с системой оплаты",
                "assigned_to": [],
                "department": [],
                "client": []}
            ]
        }

        response = self.client.force_login(user=self.user).get(url, {'search': 'Сайт'}, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)
```