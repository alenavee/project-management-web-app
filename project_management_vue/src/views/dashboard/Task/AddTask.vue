<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Добавить задание</h1>
      </div>

      <div class="column is-6">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Название</label>
            <div class="control">
              <input type="text" class="input" v-model="name">

            </div>
          </div>

          <div class="field">
            <label>Статус</label>
            <div class="control">
              <div class="select">
                <select v-model="status">
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
            <label>Описание</label>
            <div class="control">
              <v-textarea outlined v-model="description"></v-textarea>

            </div>
          </div>

          <div class="field">
            <label>Исполнитель</label>
            <div class="control">
              <div class="select">
                <select v-model="employee">
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
import project from "@/views/dashboard/Project/Project";

export default {
  name: "AddTask",
  data() {
    return {
      name: '',
      status: 'new',
      start_date: '',
      end_date: '',
      description: '',
      employee: '',
      department: {
        employees: []
      }
    }
  },
  mounted() {
    this.getDepartment()
  },
  methods: {
    async submitForm() {
      this.$store.commit('setIsLoading', true)
      console.log('submit form')

      const task = {
        project_id: this.$route.params.id,
        name: this.name,
        status: this.status,
        start_date: this.start_date,
        end_date: this.end_date,
        description: this.description,
        employee: this.employee
      }
      await axios
          .post('/api/v1/tasks/', task)
          .then(response => {
            toast({
              message: 'Задание было успешно добавлено',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 4000,
              position: 'top-center',
            })

            console.log(response)
            this.$router.push({name: 'Project', params: {id: this.$route.params.id}})
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
    }
  }
}
</script>

<style scoped>

</style>