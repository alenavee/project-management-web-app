<template>
  <div>
    <div class="column is-8 is-offset-3">
      <h1 class="title">Сайт для управления проектами внутри организации</h1>
      <div class="column is-7 is-offset-1">
        <p>Сайт предоставляет функции для сотрудников компании отслеживать выполнение рабочих задач. Все пользователи
          работают внутри отделов(команд) и все проекты отражаются для определенной команды сотрудников, которая над
          ними
          работает.</p>
        <br>
        <p>
          Для каждого проекта отражается список задач, где видно описание задания, даты начала и окончания, а также имя
          сотрудника, ответственного за выполнение.</p>
        <p><br>
          Проекты заказываются клиентами; полный список клиентов и их контактных данных можно найти на отдельной
          странице "Клиенты"</p>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',

  data: () => ({
    ecosystem: [
      {
        text: 'vuetify-loader',
        href: 'https://github.com/vuetifyjs/vuetify-loader',
      },
      {
        text: 'github',
        href: 'https://github.com/vuetifyjs/vuetify',
      },
      {
        text: 'awesome-vuetify',
        href: 'https://github.com/vuetifyjs/awesome-vuetify',
      },
    ],
    importantLinks: [
      {
        text: 'Documentation',
        href: 'https://vuetifyjs.com',
      },
      {
        text: 'Chat',
        href: 'https://community.vuetifyjs.com',
      },
      {
        text: 'Made with Vuetify',
        href: 'https://madewithvuejs.com/vuetify',
      },
      {
        text: 'Twitter',
        href: 'https://twitter.com/vuetifyjs',
      },
      {
        text: 'Articles',
        href: 'https://medium.com/vuetify',
      },
    ],
    whatsNext: [
      {
        text: 'Explore components',
        href: 'https://vuetifyjs.com/components/api-explorer',
      },
      {
        text: 'Select a layout',
        href: 'https://vuetifyjs.com/getting-started/pre-made-layouts',
      },
      {
        text: 'Frequently Asked Questions',
        href: 'https://vuetifyjs.com/getting-started/frequently-asked-questions',
      },
    ],
  }),
}
</script>
