# Edit task info or delete task

**URL** : `tasks/edit/<int:pk>/`

**Method** : `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
  "id": 3,
  "name": "Добавить главную страницу",
  "status": "finished",
  "start_date": "2022-09-03",
  "end_date": "2022-10-01",
  "description": "Отразить на странице основной каталог и переход в корзину для покупок",
  "employee": [],
  "project": []
}
```


## Tasks
* `tasks/` - list all tasks
* `tasks/create/` - create a new task
* `tasks/<int:pk>/` - view task info
* `tasks/edit/<int:pk>/` - update task info or delete task