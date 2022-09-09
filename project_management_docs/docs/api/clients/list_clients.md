# List all clients
**URL** : `/clients/`

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
  "name": "ООО Магазин",
  "address": "г. Санкт-Петербург, Лиговский пр., 10",
  "contact_person": "Анастасия Захарова",
  "email": "client1@mail.com",
  "phone_number": "+79838029348"
},
{
  "id": 4,
  "name": "ООО Книги",
  "address": "г. Санкт-Петербург, ул. Северная, д.89",
  "contact_person": "Сергей Васильев",
  "email": "client2@mail.com",
  "phone_number": "+738423687234"
}]
```