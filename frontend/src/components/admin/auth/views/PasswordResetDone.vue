<template>
  <div>
    <h1 class="text-center">
      Done!
    </h1>
    <p>
      Your password is update! Go to
      <router-link :to="{ name: 'login' }">
        Login.
      </router-link>
    </p>
  </div>
</template>

<script>
export default {
  name: 'password-reset-done'
}
</script>
