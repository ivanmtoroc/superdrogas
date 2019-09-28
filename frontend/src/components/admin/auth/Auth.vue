<template>
  <div class="login-page">
    <div class="login-box">
      <div class="login-box-body">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'auth'
}
</script>

<style scoped>
.login-page {
  background-image: url("~@/static/images/background.jpg");
  background-size: cover;
  display: flex;
  height: 100vh;
}
</style>
