<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-6">
        <h1 class="title">Добавить отдел</h1>
      </div>
      <div class="column is-8">
        <form @submit.prevent = "submitForm">
          <div class="field">
            <label>Название</label>
            <div class="control">
              <input type="text" class="input" v-model="name">

            </div>
          </div>
          <div class='field'>
            <div class="control">
              <button class="button is-success">Добавить</button>
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
  name: "AddDepartment",
  data(){
    return {
      name: '',
    }
    },
  methods:{
    async submitForm(){
      this.$store.commit('setIsLoading', true)
      console.log('submit form')
      const department = {
        name: this.name,
      }
      await axios
          .post('/api/v1/departments/', department)
          .then(response =>{
            toast({
              message: 'Отдел был успешно добавлен',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 4000,
              position: 'top-center',
            })

            this.$store.commit('setDepartment', {'id': response.data.id, 'name': this.name})
            this.$router.push('/dashboard/department')
          })

          .catch(error =>{
            console.log(error.response.data)
          })

      this.$store.commit('setIsLoading', false)
    }
  }
}

</script>

<style scoped>

</style>