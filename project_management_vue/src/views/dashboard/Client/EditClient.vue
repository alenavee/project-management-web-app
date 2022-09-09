<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Редактировать информацию о клиенте: {{client.name}}</h1>
      </div>


      <div class="column is-8">

        <div class="column is-8">
          <form @submit.prevent = "submitForm">

            <div class="field">
              <label>Название организации</label>
              <div class="control">
                <input type="text" class="input" v-model="client.name">

              </div>
            </div>

            <div class="field">
              <label>Адрес</label>
              <div class="control">
                <input type="text" class="input" v-model="client.address">

              </div>
            </div>

            <div class="field">
              <label>Контактное лицо</label>
              <div class="control">
                <input type="text" class="input" v-model="client.contact_person">

              </div>
            </div>

            <div class="field">
              <label>Email</label>
              <div class="control">
                <input type="text" class="input" v-model="client.email">

              </div>
            </div>

            <div class="field">
              <label>Телефон</label>
              <div class="control">
                <input type="text" class="input" v-model="client.phone_number">

              </div>
            </div>




            <div class='buttons'>
              <div class="control">
                <button class="button is-success">Изменить</button>
                  <button class="button is-danger" @click="deleteClient">Удалить</button>
              </div>
            </div>


          </form>

      </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from "axios";
import {toast} from "bulma-toast";

export default {
  name: "EditClient",
  data(){
    return {
      client: {},
      department: {
        employees: []
      }
    }
  },
  mounted() {
    this.getClients()
    this.getDepartment()
  },
  methods: {
    async deleteClient() {
      const clientID = this.$route.params.id
      this.$store.commit('setIsLoading', true)
      await axios
          .post(`/api/v1/clients/delete_client/${clientID}/`)
          .then(response => {
            toast({
              message: 'Информация о клиенте удалена',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 4000,
              position: 'top-center',
            })
            console.log(response.data)
            this.$router.push('/dashboard/clients')
          })
          .catch(error => {
            console.log(error)
          })
      this.$store.commit('setIsLoading', false)
    },

    async getClients() {
      this.$store.commit('setIsLoading', true)

      const clientID = this.$route.params.id
      axios
          .get(`/api/v1/clients/${clientID}/`)
          .then(response => {
            this.client = response.data
          })
          .catch(error => {
                console.log(error)
              }
          )
      this.$store.commit('setIsLoading', false)
    },
    async submitForm(){
      this.$store.commit('setIsLoading', true)
      const clientID = this.$route.params.id

      axios
          .patch(`/api/v1/clients/${clientID}/`, this.client)
          .then(response =>{
            toast({
              message: 'Данные о клиенте были успешно сохранены',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 4000,
              position: 'top-center',
            })

            this.$router.push(`/dashboard/clients/`)
          })
          .catch(error => {
            console.log(error)
          })
      this.$store.commit('setIsLoading', false)

    },
    async getDepartment(){
      this.$store.commit('setIsLoading', true)
      await axios
          .get('/api/v1/departments/get_my_department/')
          .then(response => {
            this.department = response.data
          })
          .catch(error => {
            console.log(error)
          })

      this.$store.commit('setIsLoading', false)

    }
  }

}
</script>

<style scoped>

</style>