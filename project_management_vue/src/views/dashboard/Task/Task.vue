<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">{{ task.name }}</h1>
        <div class="buttons">
          <button @click="deleteTask" class="button is-danger">Удалить</button>
        </div>
      </div>

      <div class="column is-4">
        <div class="box">
          <h2 class="subtitle">Данные</h2>

          <template v-if="task.employee">
            <p><strong>Ответственный: </strong>{{ task.employee.username }}</p></template>
          <p><strong>Статус:</strong> {{ task.status }}</p>
          <p><strong>Начало:</strong> {{ task.start_date }}</p>
          <p><strong>Окончание:</strong> {{ task.end_date }}</p>


        </div>
      </div>


      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Описание</h2>
          <p> {{ task.description }}</p>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {toast} from "bulma-toast";

export default {
  name: "Task",
  data() {
    return {
      task: {},
    }

  },
  mounted() {
    this.getTask()
  },
  methods: {
    async deleteTask() {
      this.$store.commit('setIsLoading', true)
      const taskID = this.$route.params.task_id
      const projectID = this.$route.params.id
      await axios
          .post(`/api/v1/tasks/delete_task/${projectID}/${taskID}/`)
          .then(response => {
            toast({
              message: 'Задание было удалено',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 4000,
              position: 'top-center',
            })
            console.log(response.data)
            this.$router.push(`/dashboard/projects/${projectID}`)
          })
          .catch(error => {
            console.log(error)
          })
      this.$store.commit('setIsLoading', false)
    },
    async getTask() {
      this.$store.commit('setIsLoading', true)

      const taskID = this.$route.params.task_id
      const projectID = this.$route.params.id
      /*await axios
          .get(`/api/v1/tasks/${taskID}`)
          .then(response => {
            this.task = response.data
          })
          .catch(error => {
            console.log(error)
          })*/

      await axios
          .get(`/api/v1/tasks/${taskID}/?project_id=${projectID}`)
          .then(response => {
            this.task = response.data
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