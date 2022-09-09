<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">{{ project.project_name }}</h1>

        <div class="buttons">
          <router-link v-if="project.id" :to="{ name: 'EditProject', params: { id: project.id }}"
                       class="button is-light">
            Редактировать
          </router-link>
          <button @click="deleteProject" class="button is-danger">Удалить</button>
        </div>
      </div>

      <div class="column is-4">
        <div class="box">
          <h2 class="subtitle">Данные</h2>

          <template v-if="project.assigned_to">
            <p><strong>Руководитель: </strong>{{ project.assigned_to.first_name }} {{ project.assigned_to.last_name }}
            </p></template>
          <p><strong>Статус:</strong> {{ project.project_status }}</p>
          <p><strong>Приоритет:</strong> {{ project.priority }}</p>
          <p><strong>Начало:</strong> {{ project.start_date }}</p>
          <p><strong>Окончание:</strong> {{ project.end_date }}</p>
          <p><strong>Клиент:</strong> {{ project.client.name }}</p>


        </div>
      </div>


      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Описание</h2>
          <p> {{ project.project_description }}</p>

        </div>
      </div>

      <hr>
      <div class="column is-12">
        <h2 class="subtitle">Задания</h2>

        <router-link v-if="project.id" :to="{ name: 'AddTask', params:{id: project.id}}" class="button is-success mb-6">
          Добавить задание
        </router-link>

        <div
            class="box"
            v-for="task in tasks"
            v-bind:key="task.id">
          <h3 class="is-size-4">{{ task.name }}</h3>

          <strong>Описание: </strong><p>{{ task.description }}</p>
         <strong>Исполнитель: </strong> <p>{{task.employee.first_name}} {{task.employee.last_name}} {{task.employee.username}}</p>
          <strong>Статус: </strong> <p>{{task.status}}</p>

            <router-link v-if="project.id" :to="{ name: 'EditTask', params:{id: project.id, task_id: task.id}}"
                         class="button is-light mt-6">Редактировать
            </router-link>
            &nbsp;
            <router-link v-if="project.id" :to="{ name: 'Task', params:{id: project.id, task_id: task.id}}"
                         class="button is-info mt-6">Открыть
            </router-link>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {toast} from "bulma-toast";

export default {
  name: "Project",
  data() {
    return {
      project: {},
      client: {},
      tasks: []
    }

  },
  mounted() {
    this.getProject()

  },
  methods: {
    async deleteProject() {
      this.$store.commit('setIsLoading', true)
      const projectID = this.$route.params.id
      await axios
          .post(`/api/v1/projects/delete_project/${projectID}/`)
          .then(response => {
            toast({
              message: 'Проект удален',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 4000,
              position: 'top-center',
            })
            console.log(response.data)
            this.$router.push('/dashboard/projects')
          })
          .catch(error => {
            console.log(error)
          })
      this.$store.commit('setIsLoading', false)
    },
    async getProject() {
      this.$store.commit('setIsLoading', true)

      const projectID = this.$route.params.id
      await axios
          .get(`/api/v1/projects/${projectID}`)
          .then(response => {
            this.project = response.data
          })
          .catch(error => {
            console.log(error)
          })

      await axios
          .get(`/api/v1/tasks/?project_id=${projectID}`)
          .then(response => {
            this.tasks = response.data
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