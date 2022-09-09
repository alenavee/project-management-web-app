# View project info

**URL** : ` projects/<int:pk>/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
  "id": 1,
  "assigned_to": [
    {
      "id": 1,
      "username": "emp1@mail.com",
      "first_name": "Иван",
      "last_name": "Иванов"
    }
  ],
  "name": "Сайт для книжного магазина",
  "status": "new",
  "priority": "high",
  "start_date": "2022-05-03",
  "end_date": "2022-08-01",
  "description": "Сайт для покупки книг с системой оплаты",
  "department": [],
  "client": []
}
```