# Edit project info or delete project

**URL** : `projects/edit/<int:pk>/`

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


## Projects
* `projects/` - list all projects
* `projects/create/` - create a new project
* `projects/<int:pk>/` - view project info
* `projects/edit/<int:pk>/` - update project info or delete project