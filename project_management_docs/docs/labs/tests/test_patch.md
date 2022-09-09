# Тестирование PUT-запросов

## Отредактировать проект

**URL** : `/projects/edit/`

```
class ProjectUpdateTest(TestCase):
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

    def test_update_project(self):
        self.maxDiff = None

        url = reverse('project_app:projects_edit', args=['1'])

        data = {
                "id": 1,
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

        response_retrieve = self.client.get(url, format='json')
        self.assertEqual(response_retrieve.status_code, status.HTTP_200_OK)
        self.assertEqual(response_retrieve.json(), data)

        data['project_priority'] = 'low'

        response_update = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        self.assertEqual(response_update.json(), data)
```

## Отредактировать клиента

**URL** : `/clients/edit/`

```
class class ClientUpdateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(
            name="ООО Магазин",
            address="г. Санкт-Петербург, Лиговский пр., 10",
            contact_person="Анастасия Захарова",
            email="client1@mail.com",
            phone_number="+79838029348"
        )

    def test_update_client(self):
        self.maxDiff = None

        url = reverse('project_app:clients_edit', args=['1'])
        today = str(datetime.date.today())

        data = {
            "name": "ООО Магазин",
            "address": "г. Санкт-Петербург, Лиговский пр., 10",
            "contact_person": "Анастасия Захарова",
            "email": "client1@mail.com",
            "phone_number": "+79838029348"
        }

        response_retrieve = self.client.get(url, format='json')
        self.assertEqual(response_retrieve.status_code, status.HTTP_200_OK)
        response_data = response_retrieve.json()
        response_data['date_joined'] = response_data['date_joined'][:10]
        self.assertEqual(response_data, data)

        data['phone_number'] = '+79342342'

        response_update = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)
        response_data = response_update.json()
        self.assertEqual(response_data, data)

```

