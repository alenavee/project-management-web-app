<template>
  <div class="container">
    <div class="columns is-multiline">

      <template v-if="!this.$store.state.department.id">
        <div class="column is-12">

          <h1 class="title">Присоединитесь к отделу для добавления клиентов</h1>
        </div>
      </template>
      <template v-if="this.$store.state.department.id">
        <div class="column is-12">
          <h1 class="title">Клиенты</h1>

          <div class="buttons">
            <router-link to="/dashboard/clients/add" class="button is-light">Добавить клиента</router-link>

          </div>
        </div>

        <form @submit.prevent="submitForm">
          <div class="field has-addons">
            <div class="control">
              <input type="text" class="input" v-model="query">
            </div>
            <div class="control">
              <button class="button is-light">Поиск</button>
            </div>
          </div>
        </form>


        <div class="column is-12">
          <template v-if="clients.length">

            <table class="table is-fullwidth">
              <thead>
              <tr>
                <th>Название организации</th>
                <th>Контактное лицо</th>
                <th>Email</th>
                <th>Адрес</th>
                <th>Номер телефона</th>
                <th></th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="client in clients" v-bind:key="client.id">
                <td>{{ client.name }}</td>
                <td>{{ client.contact_person }}</td>
                <td>{{ client.email }}</td>
                <td>{{ client.address }}</td>
                <td>{{ client.phone_number }}</td>

                <td>
                  <router-link :to="{ name: 'EditClient', params: { id: client.id }}" class="button is-info">
                    Редактировать
                  </router-link>

                </td>

              </tr>
              </tbody>

            </table>
          </template>

          <template v-else>
            <p>Клиентов пока нет</p>
          </template>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Clients",

  data() {
    return {
      clients: [],
      client: {},
      query:'',
    }
  },
  mounted() {
    this.getClients()
  },
  methods: {

    async getClients() {
      this.$store.commit('setIsLoading', true)

      await axios
          .get(`/api/v1/clients/?search=${this.query}`)
          .then(response => {
            this.clients = response.data
          })
          .catch(error => {
                console.log(error)
              }
          )

      this.$store.commit('setIsLoading', false)
    },
    submitForm(){
      this.getClients()
    }
  }
}
</script>

<style scoped>

</style>