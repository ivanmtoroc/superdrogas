<template>
  <div>
    <h1 class="text-center">
      Password reset
    </h1>
    <form v-if="!sent" @submit.prevent="formHandler()">
      <input-component
        id="email"
        v-model="email"
        placeholder="Email"
        type="email"
        :label="false"
        :inputErrors="errors.email"
      >
        <span class="glyphicon glyphicon-envelope form-control-feedback"></span>
      </input-component>
      <div class="row footer">
        <div class="col-md-6 pull-right">
          <button type="submit" class="btn bg-navy btn-block">
            Send
            <i class="fa fa-sign-in"></i>
          </button>
        </div>
      </div>
    </form>
    <p v-else>
      The email was sent. Please check your inbox.
    </p>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'password-reset',
  data () {
    return {
      email: '',
      sent: false,
      errors: {}
    }
  },
  methods: {
    ...mapActions('authentication', [
      'passwordRestEmail'
    ]),
    async formHandler () {
      await this.passwordRestEmail(this.email)
      this.sent = true
    }
  }
}
</script>

<style scoped>
.fp {
  margin: 10px 0px;
}
.footer {
  padding-top: 10px;
}
</style>
