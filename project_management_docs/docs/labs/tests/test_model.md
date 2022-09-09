# Тестирование моделей

## Название поля в модели

**Model** : `Project`

```
class ProjectNameModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Project.objects.create(
            project_name='Приложение',
        )

    def test_field_value(self):
        subject_instance = Project.objects.get(id=1)
        self.assertEquals(subject_instance.project_name, 'Приложение')
```

## Максимальная длина поля

**Model** : `Project`

```
class ProjectNameLengthModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Project.objects.create(
            project_name='Мобильное приложение для магазина'
        )

    def test_max_length(self):
        group_instance = Project.objects.get(id=1)
        max_length = group_instance._meta.get_field('project_name').max_length
        self.assertEquals(max_length, 255)
```

## Тип данных

**Model** : `Task`

```
class TaskFieldTypeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):


        Project.objects.create(
            project_name='Мобильное приложение'
        )

        Task.objects.create(
            name='Главная страница',
            project=Project.objects.get(id=1),
            status='new',
            description='описание для задания'
            )

    def test_field_type(self):
        pair_instance = Task.objects.get(id=1)
        description_field = pair_instance._meta.get_field('description')
        self.assertTrue(isinstance(description_field, TextField))
```
