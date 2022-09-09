# View task info

**URL** : ` tasks/<int:pk>/`

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
  "employee": [
    {
      "id": 1,
      "username": "emp1@mail.com",
      "first_name": "Иван",
      "last_name": "Иванов"
    }
  ],
  "name": "Добавить главную страницу",
  "status": "finished",
  "start_date": "2022-09-03",
  "end_date": "2022-10-01",
  "description": "Отразить на странице основной каталог и переход в корзину для покупок",
  "project": [
    3
  ]
}
```