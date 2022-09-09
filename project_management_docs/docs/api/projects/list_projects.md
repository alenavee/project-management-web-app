# List all projects
**URL** : `/projects/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** :

```json
[{
  "id": 3,
  "name": "Сайт для книжного магазина",
  "status": "new",
  "priority": "high",
  "start_date": "2022-05-03",
  "end_date": "2022-08-01",
  "description": "Сайт для покупки книг с системой оплаты",
  "assigned_to": [
    1
  ],
  "department": [],
  "client": []
},
{
  "id": 5,
  "name": "Мобильное приложение для сети кафе",
  "status": "finished",
  "priority": "low",
  "start_date": "2022-03-02",
  "end_date": "2022-06-01",
  "description": "Приложение для кафе с меню и возможностью сделать заказ",
  "assigned_to": [
        2
],
  "department": [],
  "client": []
}]
```