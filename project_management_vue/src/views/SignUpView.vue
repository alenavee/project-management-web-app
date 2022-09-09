<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Регистрация аккаунта</h1>
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Email</label>
            <div class="control">
              <input type="email" name="email" class="input" v-model="username">

            </div>
          </div>


          <div class="field">
            <label>Пароль</label>
            <div class="control">
              <input type="password" name="password1" class="input" v-model="password1">

            </div>
          </div>

          <div class="field">
            <label>Повторите пароль</label>
            <div class="control">
              <input type="password" name="password2" class="input" v-model="password2">

            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{error}}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-info">Зарегистрироваться</button>

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
  name: 'SignUp',
  data() {
    return {
      username: '',
      password1: '',
      password2: '',
      errors: []
    }
  },
  methods: {
    async submitForm() {

      this.errors = []
      if (this.username === '') {
        this.errors.push('Логин не может быть пустым')
      }
      if (this.password1 === '') {
        this.errors.push('Слишком короткий пароль')
      }
      if (this.password1 !== this.password2) {
        this.errors.push('Пароли не совпадают')
      }
      if (!this.errors.length) {
        this.$store.commit('setIsLoading', true)
        const formData = {
          username: this.username,
          password: this.password1,
          first_name: this.first_name,
          last_name: this.last_name
        }
        await axios
            .post('/api/v1/users/', formData)
            .then(response => {
              toast({
                message: 'Аккаунт был успешно создан. Используйте логин и пароль для того, чтобы войти',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 5000,
                position: 'top-center',
              })

              this.$router.push('/login')
            })
            .catch(error => {
              if (error.response) {
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
              } else if (error.message) {
                this.errors.push('Что-пошло не так. Попробуйте еще раз')
              }
            })

        this.$store.commit('setIsLoading', false)
      }
    }
  }
}
</script>

<style scoped>

</style>