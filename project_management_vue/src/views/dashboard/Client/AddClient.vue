<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-6">
        <h1 class="title">Добавить клиента</h1>
      </div>

      <div class="column is-8">
        <form @submit.prevent = "submitForm">

          <div class="field">
            <label>Название организации</label>
            <div class="control">
              <input type="text" class="input" v-model="name">

            </div>
          </div>

          <div class="field">
            <label>Адрес</label>
            <div class="control">
              <input type="text" class="input" v-model="address">

            </div>
          </div>

          <div class="field">
            <label>Контактное лицо</label>
            <div class="control">
              <input type="text" class="input" v-model="contact_person">

            </div>
          </div>

          <div class="field">
            <label>Email</label>
            <div class="control">
              <input type="text" class="input" v-model="email">

            </div>
          </div>

          <div class="field">
            <label>Телефон</label>
            <div class="control">
              <input type="text" class="input" v-model="phone_number">

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
  name: "AddClient",
  data(){
    return{
      name:'',
      address:'',
      contact_person:'',
      email:'',
      phone_number:'',
    }
  },
  methods:{
    async submitForm(){
      this.$store.commit('setIsLoading', true)
      console.log('submit form')
      const client = {
        name:this.name,
        address: this.address,
        contact_person: this.contact_person,
        email: this.email,
        phone_number: this.phone_number,
      }
      await axios
          .post('/api/v1/clients/', client)
          .then(response =>{
            toast({
              message: 'Клиент был успешно добавлен',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 4000,
              position: 'top-center',
            })

            console.log(response)
            this.$router.push('/dashboard/clients')
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