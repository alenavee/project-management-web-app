# List all tasks
**URL** : `/tasks/`

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
  "name": "Добавить главную страницу",
  "status": "finished",
  "start_date": "2022-09-03",
  "end_date": "2022-10-01",
  "description": "Отразить на странице основной каталог и переход в корзину для покупок",
  "employee": [],
  "project": [
    3
  ]
},
{
  "id": 4,
  "name": "Страница для просмотра товара",
  "status": "finished",
  "start_date": "2022-09-03",
  "end_date": "2022-10-01",
  "description": "Детализированная страница товара позволяет клиенту добавить товар в корзину",
  "employee": [
    1
  ],
  "project": [
    3
  ]
}]
```