# Create project

**URL** : `projects/create/`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `201 Created`

**Content** : `{[]}`

```json
{
  "id": 3,
  "name": "Сайт для книжного магазина",
  "status": "new",
  "priority": "high",
  "start_date": "2022-05-03",
  "end_date": "2022-08-01",
  "description": "Сайт для покупки книг с системой оплаты",
  "assigned_to": [],
  "department": [],
  "client": []
}
```