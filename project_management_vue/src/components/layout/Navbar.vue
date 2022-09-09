<template>
  <nav class="navbar is-light">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item">
        <strong>Project Management</strong>
      </router-link>
    </div>

    <div class="navbar-menu">
      <div class="navbar-end">
        <template v-if="$store.state.isAuthenticated">
          <router-link to="/dashboard/projects/" class="navbar-item">Проекты</router-link>
          <router-link to="/dashboard/department/" class="navbar-item">Отдел</router-link>
          <router-link to="/dashboard/clients/" class="navbar-item">Клиенты</router-link>
        </template>
        <div class="navbar-item">
          <div class="buttons">

            <template v-if="!$store.state.isAuthenticated">

              <router-link to="/sign-up" class="button is-info">
                <strong>Регистрация</strong>
              </router-link>
              <router-link to="/login" class="button is-light">Войти</router-link>
            </template>
            <template v-else>
              <router-link to="/dashboard/my-account" class="button is-info">Мой аккаунт</router-link>
            </template>
          </div>
        </div>
      </div>
    </div>

  </nav>
</template>

<script>
export default {
  name: "Navbar"
}
</script>

<style scoped>

</style>