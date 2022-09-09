<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Редактировать задание: {{task.name}}</h1>
      </div>
      <div class="column is-8">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Название</label>
            <div class="control">
              <input type="text" class="input" v-model="task.name">

            </div>
          </div>

          <div class="field">
            <label>Статус</label>
            <div class="control">
              <div class="select">
                <select v-model="task.status">
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
              <input type="date" class="input" v-model="task.start_date">

            </div>
          </div>

          <div class="field">
            <label>Дата окончания</label>
            <div class="control">
              <input type="date" class="input" v-model="task.end_date">

            </div>
          </div>


          <div class="field">
            <label>Описание</label>
            <div class="control">
              <input type="text" class="input" v-model="task.description">

            </div>
          </div>

          <div class="field">
            <label>Исполнитель</label>
            <div class="control">
              <div class="select">
                <select v-model="task.employee">
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
  name: "EditTask",
  data(){
    return {
      task: {},
      department: {
        employees: []
      }
    }
  },
  mounted() {
    this.getTasks()
    this.getDepartment()
  },
  methods: {
    async getTasks() {
      this.$store.commit('setIsLoading', true)

      const taskID = this.$route.params.task_id
      const projectID = this.$route.params.id
      axios
          .get(`/api/v1/tasks/${taskID}/?project_id=${projectID}`)
          .then(response => {
            this.task = response.data
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
          .patch(`/api/v1/tasks/${this.task.id}/?project_id=${projectID}`, this.task)
          .then(response =>{
            toast({
              message: 'Задание успешно изменено',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 4000,
              position: 'top-center',
            })

            this.$router.push({name: 'Project', params: {id: this.$route.params.id}})
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

    }
  }

}
</script>

<style scoped>

</style>