<template>
  <div>
    <h1 class="text-center">
      Enter your new password
    </h1>
    <form @submit.prevent="formHandler()">
      <input-component
        id="password"
        v-model="form.new_password1"
        placeholder="New password"
        type="password"
        :label="false"
        :inputErrors="errors.new_password1"
      >
        <span class="glyphicon glyphicon-lock form-control-feedback"></span>
      </input-component>
      <input-component
        id="password_confirmation"
        v-model="form.new_password2"
        placeholder="Confirm new password"
        type="password"
        :label="false"
        :inputErrors="errors.new_password2"
      >
        <span class="glyphicon glyphicon-lock form-control-feedback"></span>
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
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'password-reset-new-password',
  data () {
    return {
      form: {
        new_password1: '',
        new_password2: '',
        uid: this.$route.params.uid,
        token: this.$route.params.token
      },
      errors: {}
    }
  },
  methods: {
    ...mapActions('authentication', [
      'passwordRestNewPassword'
    ]),
    async formHandler () {
      this.errors = await this.passwordRestNewPassword(this.form)
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
