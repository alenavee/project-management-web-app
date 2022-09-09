<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Мой аккаунт</h1>
      </div>
      <div class="column is-12 mt-3">
       <p><strong>Имя: </strong>{{user.first_name}} {{user.last_name}}</p>
        <strong>Email: </strong>{{user.username}}
      </div>

      <div class="column is-12">
        <div class="buttons">
          <router-link :to="{ name: 'EditEmployee', params: { id: $store.state.user.id }}" class="button is-light">
            Редактировать
          </router-link>
          <button @click="logout()" class="button is-danger">Выйти</button>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {

  name: "MyAccount",
  data() {
    return {
      user: {}
    }
  },
  mounted() {
    this.getUser()
  },
  methods: {
    async getUser() {
      this.$store.commit('setIsLoading', true)
      const userID = this.$store.state.user.id
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

    async logout() {
      await axios
          .post('/api/v1/token/logout/')
          .then(response => {
            console.log('Logget out')
          })
          .catch(error => {
            console.log(JSON.stringify(error))
          })

      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('token')
      localStorage.removeItem('username')
      localStorage.removeItem('userid')
      localStorage.removeItem('department_name')
      localStorage.removeItem('department_id')
      this.$store.commit('removeToken')

      this.$router.push('/')
    }

  }
}
</script>

<style scoped>

</style>