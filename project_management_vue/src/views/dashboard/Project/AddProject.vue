<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Добавить проект</h1>
      </div>

      <div class="column is-6">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Название</label>
            <div class="control">
              <input type="text" class="input" v-model="project_name">

            </div>
          </div>

          <div class="field">
            <label>Статус</label>
            <div class="control">
              <div class="select">
                <select v-model="project_status">
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
                <select v-model="priority">
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
              <input type="date" class="input" v-model="start_date">

            </div>
          </div>

          <div class="field">
            <label>Дата окончания</label>
            <div class="control">
              <input type="date" class="input" v-model="end_date">

            </div>
          </div>

          <div class="field">
            <label>Руководитель</label>
            <div class="control">
              <div class="select">
                <select v-model="assigned_to">
                  <option value="" selected>Выберите сотрудника</option>
                  <option
                      v-for="employee in department.employees"
                      v-bind:key="employee.id"
                      v-bind:value="employee.id"
                  >{{ employee.username }}
                  </option>
                </select>
              </div>
            </div>
          </div>



          <div class="field">
            <label>Клиент</label>
            <div class="control">
              <div class="select">
                <select v-model="client">
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
              <v-textarea outlined v-model="project_description"></v-textarea>

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
  name: "AddProject",
  data() {
    return {
      project_name: '',
      project_status: 'new',
      priority: 'medium',
      start_date: '',
      end_date: '',
      client: '',
      project_description: '',
      assigned_to: '',


      clients: [],
      department: {
        employees: []
      }
    }
  },
  mounted() {
    this.getDepartment()
    this.getClients()
  },
  methods: {
    async submitForm() {
      this.$store.commit('setIsLoading', true)
      console.log('submit form')
      const project = {
        project_name: this.project_name,
        project_status: this.project_status,
        priority: this.priority,
        start_date: this.start_date,
        end_date: this.end_date,
        client: this.client,
        assigned_to: this.assigned_to,
        project_description: this.project_description
      }
      await axios
          .post('/api/v1/projects/', project)
          .then(response => {
            toast({
              message: 'Проект был успешно добавлен',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 4000,
              position: 'top-center',
            })

            console.log(response)
            this.$router.push('/dashboard/projects')
          })

          .catch(error => {
            console.log(error.response.data)
          })

      this.$store.commit('setIsLoading', false)
    },
    async getDepartment() {
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