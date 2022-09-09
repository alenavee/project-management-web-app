<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Редактировать: {{project.project_name}}</h1>
      </div>
    <div class="column is-12">

      <form @submit.prevent = "submitForm">
        <div class="field">
          <label>Название проекта</label>
          <div class="control">
            <input type="text" class="input" v-model="project.project_name">

          </div>
        </div>

        <div class="field">
          <label>Статус</label>
          <div class="control">
            <div class="select">
              <select v-model="project.project_status">
                <option value="new">New</option>
                <option value="inprogress">In progress</option>
                <option value="cancelled">Cancelled</option>
                <option value="finished">Finished</option>
                <option value="frozen">Frozen</option>
              </select>
            </div>


          </div>
        </div>

        <div class="field">
          <label>Приоритет</label>
          <div class="control">
            <div class="select">
              <select v-model="project.priority">
                <option value="medium">Medium</option>
                <option value="high">High</option>
                <option value="low">Low</option>
              </select>
            </div>
          </div>
        </div>

        <div class="field">
          <label>Дата начала</label>
          <div class="control">
            <input type="date" class="input" v-model="project.start_date">

          </div>
        </div>

        <div class="field">
          <label>Дата окончания</label>
          <div class="control">
            <input type="date" class="input" v-model="project.end_date">

          </div>
        </div>

        <div class="field">
          <label>Руководитель</label>
          <div class="control">
            <div class="select">
              <select v-model="project.assigned_to.username">
                <option value="" selected>Выберите сотрудника</option>
                <option
                    v-for="employee in department.employees"
                    v-bind:key="employee.id"
                    v-bind:value="employee.id"
                >{{ employee.username }}</option>
              </select>
            </div>
          </div>
        </div>





        <div class="field">
          <label>Клиент</label>
          <div class="control">
            <div class="select">
              <select v-model="project.client.name">
                <option value="" selected>Выберите клиента</option>
                <option
                    v-for="client in clients"
                    v-bind:key="client.id"
                    v-bind:value="client.id"
                >{{ client.name }}
                </option>
              </select>
            </div>
          </div>
        </div>

        <div class="field">
          <label>Описание</label>
          <div class="control">
            <input type="text" class="input" v-model="project.project_description">

          </div>
        </div>

        <div class='field'>
          <div class="control">
            <button class="button is-success">Изменить</button>
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
  name: "EditProject",
  data(){
    return {
      project: {},
      clients:[],
      department: {
        employees: []
      }
    }
  },
  mounted() {
    this.getProjects()
    this.getDepartment()
    this.getClients()
  },
  methods: {
    async getProjects() {
      this.$store.commit('setIsLoading', true)

      const projectID = this.$route.params.id
      axios
          .get(`/api/v1/projects/${projectID}/`)
          .then(response => {
            this.project = response.data
          })
          .catch(error => {
                console.log(error)
              }
          )
      this.$store.commit('setIsLoading', false)
    },
    async submitForm(){
      this.$store.commit('setIsLoading', true)
      const projectID = this.$route.params.id

      axios
          .patch(`/api/v1/projects/${projectID}/`, this.project)
          .then(response =>{
            toast({
              message: 'Данные проекта были успешно сохранены',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 4000,
              position: 'top-center',
            })

            this.$router.push(`/dashboard/projects/${projectID}/`)
          })
          .catch(error => {
            console.log(error)
          })
      this.$store.commit('setIsLoading', false)

    },
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

    },
    async getClients() {
      this.$store.commit('setIsLoading', true)
      await axios
          .get('/api/v1/clients/')
          .then(response => {
            this.clients = response.data
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