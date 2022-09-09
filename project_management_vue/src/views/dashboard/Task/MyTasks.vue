<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">


      <div class="column is-6">
        <h2 class="subtitle">Сотрудники</h2>

        <table class="table is-fullwidth">
          <thead>
          <tr>
            <th>Название</th>
            <th>Описание</th>
            <th>Дедлайн</th>
            <th>Статус</th>
          </tr>
          </thead>

          <tbody>
          <tr v-for="task in tasks"
              v-bind:key="task.id">
            <td>{{ task.name }}</td>
            <td>{{ task.description }} </td>
            <th>{{task.end_date}}</th>
            <th>{{ task.status }}</th>
          </tr>
          </tbody>

        </table>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MyTasks",
  data(){
    return{
      tasks:[]
    }
  },
  mounted() {
    this.getTasks()
  },
  methods:{
    async getTasks(){
      this.$store.commit('setIsLoading', true)
      await axios
          .get('/api/v1/departments/get_my_tasks/')
          .then(response => {
            this.tasks = response.data
            console.log(this.tasks)
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