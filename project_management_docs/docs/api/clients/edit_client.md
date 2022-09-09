# Edit client info or delete client

**URL** : `clients/edit/<int:pk>/`

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
  "name": "ООО Магазин",
  "address": "г. Санкт-Петербург, Лиговский пр., 10",
  "contact_person": "Анастасия Захарова",
  "email": "client1@mail.com",
  "phone_number": "+79838029348"
}
```


## Clients
* `cleints/` - list all clients
* `cleints/create/` - create a new client
* `cleints/edit/<int:pk>/` - update client info or delete clients