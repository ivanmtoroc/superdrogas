<template>
  <router-view />
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'app',
  methods: {
    ...mapActions('app', [
      'getTenantInformation'
    ])
  },
  created () {
    this.getTenantInformation()
  }
}
</script>

<style>
.error-block {
  color: red;
  font-size: 12px;
  margin-top: 10px !important;
  display: block !important;
}
.mt-10 {
  margin-top: 10px;
}
</style>
