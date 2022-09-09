<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Редактировать информацию о сотруднике</h1>
      </div>

      <div class="column is-2">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Имя</label>
            <div class="control">
              <input type="text" class="input" v-model="user.first_name">
            </div>
          </div>

          <div class="field">
            <label>Фамилия</label>
            <div class="control">
              <input type="text" class="input" v-model="user.last_name">
            </div>
          </div>


          <div class="field">
            <div class="control">
              <button class="button is-success">Сохранить изенения</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
  name: 'EditEmployee',
  data() {
    return {
      user: {},
    }
  },
  mounted() {
    this.getUser()
  },
  methods: {
    async getUser() {
      this.$store.commit('setIsLoading', true)
      const userID = this.$route.params.id
      await axios
          .get(`/api/v1/departments/employee/${userID}/`)
          .then(response => {
            this.user = response.data
          })
          .catch(error => {
            console.log(error)
          })
      this.$store.commit('setIsLoading', false)
    },
    async submitForm() {

      this.$store.commit('setIsLoading', true)
      const userID = this.$route.params.id
      await axios
          .put(`/api/v1/departments/employee/${userID}/`, this.user)
          .then(response => {
            toast({
              message: 'Информация о сотруднике изменена',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'top-center',
            })
            this.$router.push({name: 'MyAccount'})
          })
          .catch(error => {
            console.log(error)
          })
      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>