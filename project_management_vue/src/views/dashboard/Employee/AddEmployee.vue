<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title"> Добавить сотрудника </h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Email</label>
            <div class="control">
              <div class="select">
                <select v-model="username">
                  <option value="" selected>Выберите сотрудника</option>
                  <option
                      v-for="user in users_list"
                      v-bind:key="user.id"
                      v-bind:value="user.id"
                  >{{ user.username }}
                  </option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-info">Добавить</button>

            </div>
          </div>


        </form>


      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {toast} from "bulma-toast";

export default {
  name: "AddEmployee",

  data() {
    return {
      username: '',
      users_list: [],
      errors: []
    }
  },
  mounted() {
    this.getUsers()
  },

  methods: {
    async getUsers() {
      this.$store.commit('setIsLoading', true)

      await axios
          .get('/api/v1/users_list/')
          .then(response => {
            this.users_list = response.data
          })
          .catch(error => {
                console.log(error)
              }
          )

      this.$store.commit('setIsLoading', false)
    },


    async submitForm() {
      if (!this.errors.length) {
        this.$store.commit('setIsLoading', true)


        const emailData = {'email': this.username}
        axios
            .post('/api/v1/departments/add_employee/', emailData)
            .then(response => {
              this.$router.push({'name': 'Department'})
              toast({
                message: 'Сотрудник успешно добавлен',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 4000,
                position: 'top-center',
              })
              this.$router.push('/dashboard/department')
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