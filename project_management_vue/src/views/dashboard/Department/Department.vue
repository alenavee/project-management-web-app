<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title"> {{ department.name }}</h1>

        <template v-if="!this.$store.state.department.id">

          <h1 class="title">Вы не состоите ни в одном отделе. Добавьте новый или дождитесь приглашения</h1>
          <router-link :to="{'name': 'AddDepartment'}" class="button is-primary mt-3">Добавить отдел</router-link>

        </template>

        <template v-if="department.lead.id === $store.state.user.id">

        <router-link :to="{'name': 'AddEmployee'}" class="button is-primary">Добавить сотрудника</router-link>
        </template>
      </div>
      <template v-if="this.$store.state.department.id">

      <div class="column is-6">
        <h2 class="subtitle">Сотрудники</h2>

        <table class="table is-fullwidth">
          <thead>
          <tr>
            <th>ФИО</th>
            <th>Email</th>
          </tr>
          </thead>

          <tbody>
          <tr v-for="employee in department.employees"
          v-bind:key="employee.id">
            <td>{{ employee.first_name }} {{ employee.last_name }}</td>
            <td>{{ employee.username }} </td>
          </tr>
          </tbody>

        </table>

      </div>
      </template>

    </div>

  </div>

</template>

<script>
import axios from "axios";

export default {
  name: "Department",
  data(){
    return{
      department:{
        employees: [],
        lead: {}
      }
    }
  },
  mounted() {
    this.getDepartment()
  },
  methods:{
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