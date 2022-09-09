# Тестирование POST-запросов

## Создать проект

**URL** : `/projects/create/`

```
class ProjectCreateTest(TestCase):

    def test_create_project(self):
        url = reverse('project_app:projects_create')

        data = {"id": 3,
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

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)


class ClientCreateTest(TestCase):

    def test_create_client(self):
        self.maxDiff = None
        url = reverse('client_app:clients_create')

        data_request = {
            "name": "ООО Магазин",
            "address": "г. Санкт-Петербург, Лиговский пр., 10",
            "contact_person": "Анастасия Захарова",
            "email": "client1@mail.com",
            "phone_number": "+79838029348"
        }

        data_response_exp = {
            "name": "ООО Магазин",
            "address": "г. Санкт-Петербург, Лиговский пр., 10",
            "contact_person": "Анастасия Захарова",
            "email": "client1@mail.com",
            "phone_number": "+79838029348"
        }

        response = self.client.post(url, data_request, format='json')
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data_response_act = {k: v for k, v in response.data.items() if k not in ('date_joined', 'password')}

        self.assertEqual(data_response_act, data_response_exp)

```

## Создать задание

**URL** : `/tasks/create`

```
class ProjectTaskCreateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(
            project_name='Мобильное приложение'
        )

        Task.objects.create(
            name='Главная страница',
            project=Project.objects.get(id=1),
            status='new',
            description='описание для задания'
        )

    def test_create_task_for_project(self):
        self.maxDiff = None

        url = reverse('project_app:project')

        data = {
            "id": 1,
            "project_name": "Мобильное приложение",
            "project_status": "new",
            "priority": "high",
            "start_date": "2022-05-03",
            "end_date": "2022-08-01",
            "project_description": "",
            "assigned_to": [],
            "department": [],
            "client": [],
            "tasks": [{"id": 1,
                       "name": 'Главная страница',
                       "status": 'new',
                       "description": 'описание для задания'
                       }]

        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)
```

