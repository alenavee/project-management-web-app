<template>
  <div class="container">
    <div class="columns is-multiline">
      <template v-if="!this.$store.state.department.id">
        <div class="column is-12">

          <h1 class="title">Присоединитесь к отделу для работы над проектами</h1>
        </div>
      </template>

      <template v-if="this.$store.state.department.id">
        <div class="column is-12">

          <h1 class="title">Проекты</h1>

          <router-link to="/dashboard/projects/add" class="button is-success">Добавить проект</router-link>
        </div>

        <hr>

        <div class="column is-3">
          <form @submit.prevent="submitForm">
            <div class="field has-addons">
              <div class="control">
                <input type="text" class="input" v-model="query">
              </div>
              <div class="control">
                <button class="button is-light">Поиск</button>
              </div>
            </div>
          </form>
        </div>

        <div class="column is-3">
          <form @submit.prevent="submitFormDate">
            <div id='app'>
              <button ref='calendarTrigger' type='button'>Change</button>
            </div>
            <div class="control">
              <button class="button is-light">Фильтр по дате начала</button>
            </div>
          </form>
        </div>

        <div class="column is-10">
          <label class="checkbox">
            <input type="checkbox" id="checkbox" v-model="checked" @change="check($event)">
          Упорядочить по дате начала
        </label>
        </div>
      </template>

    </div>

    <div class="field">
      <label>Статус</label>
      <div class="control">
        <div class="select">
          <select v-model="project_status">
            <option value="">Любой</option>
            <option value="new">New</option>
            <option value="inprogress">In progress</option>
            <option value="cancelled">Cancelled</option>
            <option value="finished">Finished</option>
            <option value="frozen">Frozen</option>
          </select>
        </div>


      </div>
    </div>


        <div class=" column is-10">
            <table class="table is-fullwidth">
              <thead>
              <tr>
                <th>Название</th>
                <th>Статус</th>
                <th>Руководитель</th>
                <th>Клиент</th>
                <th>Дата начала</th>
                <th></th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="project in projects" v-bind:key="project.id">
                <td>{{ project.project_name }}</td>
                <td>{{ project.project_status }}</td>
                <td>
                  <template v-if="project.assigned_to">{{ project.assigned_to.first_name }} {{
                      project.assigned_to.last_name
                    }}
                  </template>
                </td>

                <td>{{ project.client.name }}</td>

                <td>{{ project.start_date }}</td>

                <td>
                  <router-link :to="{ name: 'Project', params: { id: project.id }}" class="button is-info">Открыть
                  </router-link>
                </td>

              </tr>
              </tbody>

            </table>

            <div class="buttons">
              <button class="button is-light" @click="goToPreviousPage()" v-if="showPreviousButton">Назад</button>
              <button class="button is-light" @click="goToNextPage()" v-if="showNextButton">Следующие</button>
            </div>




    </div>
  </div>
</template>


<script>

import axios from "axios";
import bulmaCalendar from 'bulma-calendar/dist/js/bulma-calendar.min.js';

export default {
  name: "Projects",

  data() {
    return {
      projects: [],
      showNextButton: false,
      showPreviousButton: false,
      currentPage: 1,
      query: '',

      date: new Date(),
      date1: '',
      date2: '',
      calendar: bulmaCalendar,

      checked: true,
      ordering: '',

      project_status:'',

    }
  },


  computed: {
    niceDate() {
      if (this.date) {
        return this.date.toLocaleDateString()

      }
    }
  },

  mounted() {
    this.getProjects()
    this.calendar = bulmaCalendar.attach(this.$refs.calendarTrigger, {
      isRange: true,
      type: "date",
      weekStart: 1
    })[0]
    this.calendar.on('select', e => (this.date = e.start || null))
  },
  methods: {

    goToNextPage() {
      this.currentPage += 1
      this.getProjects()
    },
    goToPreviousPage() {
      this.currentPage -= 1
      this.getProjects()
    },

    async getProjects() {
      this.$store.commit('setIsLoading', true)

      this.showNextButton = false
      this.showPreviousButton = false

      await axios
          .get(`/api/v1/projects/?page=${this.currentPage}&search=${this.query}&start_date_after=${this.date1}&start_date_before=${this.date2}&ordering=${this.ordering}&project_status=${this.project_status}`) //&search=${this.query}
          .then(response => {
            this.projects = response.data.results

            if (response.data.next) {
              this.showNextButton = true
            }
            if (response.data.previous) {
              this.showPreviousButton = true
            }

          })
          .catch(error => {
                console.log(error)
              }
          )

      this.$store.commit('setIsLoading', false)
    },
    submitForm() {
      console.log(this.query)
      console.log(this.project_status)
      this.getProjects()
    },
    submitFormDate() {
      console.log(this.query)

      this.date1 = this.calendar.startDate
      this.date2 = this.calendar.endDate

      this.date1 = this.date1.toISOString().slice(0, 10)
      this.date2 = this.date2.toISOString().slice(0, 10)
      console.log(this.date1)
      console.log(this.date2)
      this.getProjects()
      this.date1 = ''
      this.date2 = ''
    },
    check: function(e) {
      if (this.checked === true) {
        this.ordering = 'start_date'
        this.getProjects()
      }else{
        this.ordering =''
        this.getProjects()
      }
    }
  }
}
</script>

<style lang="scss">
@import 'bulma-calendar/dist/css/bulma-calendar.min.css';

</style>