<template>
  <modal-component id="tenant-form" :title="`${ isNewTenant ? 'Create' : 'Update' } tenant`">
    <form>
      <div class="row">
        <input-component
          class="col-md-6"
          id="schema_name"
          v-model="schema_name"
          placeholder="Schema name"
          :inputErrors="errors.schema_name"
        />
        <input-component
          class="col-md-6"
          id="name"
          v-model="name"
          placeholder="Name"
          :inputErrors="errors.name"
        />
        <input-component
          class="col-md-6"
          id="prefix"
          v-model="prefix"
          placeholder="Prefix"
          :inputErrors="errors.prefix"
        />
        <input-component
          class="col-md-6"
          id="nit"
          v-model="nit"
          placeholder="NIT"
          :inputErrors="errors.nit"
        />
        <input-component
          class="col-md-6"
          id="phone"
          v-model="phone"
          placeholder="Phone"
          :inputErrors="errors.phone"
        />
        <input-component
          class="col-md-6"
          id="email"
          v-model="email"
          placeholder="Email"
          :inputErrors="errors.email"
        />
        <input-component
          class="col-md-6"
          id="address"
          v-model="address"
          placeholder="Address"
          :inputErrors="errors.address"
        />
        <input-component
          class="col-md-6"
          id="description"
          v-model="description"
          placeholder="Description"
          :inputErrors="errors.description"
        />
        <div class="form-group col-sm-12">
          <label>Package</label>
          <select2
            id="package"
            :options="packages"
            v-model="pack"
          >
          </select2>
          <span v-if="errors.package" class="help-block error-block">
            This field is required.
          </span>
        </div>
      </div>
      <div class="pull-right">
        <button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button>
        <button v-if="isNewTenant" @click="createTenant($event)" type="submit" class="btn btn-success">Create</button>
        <button v-else @click="updateTenant($event)" type="submit" class="btn btn-primary">Update</button>
      </div>
    </form>
  </modal-component>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  name: 'tenant-form',
  data () {
    return {
      packages: [
        { id: 'STT', text: 'Starter' },
        { id: 'STD', text: 'Standart' },
        { id: 'PRM', text: 'Premium' }
      ]
    }
  },
  computed: {
    ...mapState('tenants', [
      'tenant',
      'errors'
    ]),
    ...mapGetters('tenants', [
      'isNewTenant'
    ]),
    schema_name: {
      get () {
        return this.tenant.schema_name
      },
      set (value) {
        this.$store.commit('tenants/SET_SCHEMA_NAME', value)
      }
    },
    name: {
      get () {
        return this.tenant.name
      },
      set (value) {
        this.$store.commit('tenants/SET_NAME', value)
      }
    },
    prefix: {
      get () {
        return this.tenant.prefix
      },
      set (value) {
        this.$store.commit('tenants/SET_PREFIX', value)
      }
    },
    nit: {
      get () {
        return this.tenant.nit
      },
      set (value) {
        this.$store.commit('tenants/SET_NIT', value)
      }
    },
    phone: {
      get () {
        return this.tenant.phone
      },
      set (value) {
        this.$store.commit('tenants/SET_PHONE', value)
      }
    },
    email: {
      get () {
        return this.tenant.email
      },
      set (value) {
        this.$store.commit('tenants/SET_EMAIL', value)
      }
    },
    address: {
      get () {
        return this.tenant.address
      },
      set (value) {
        this.$store.commit('tenants/SET_ADDRESS', value)
      }
    },
    description: {
      get () {
        return this.tenant.description
      },
      set (value) {
        this.$store.commit('tenants/SET_DESCRIPTION', value)
      }
    },
    pack: {
      get () {
        return this.tenant.package
      },
      set (value) {
        this.$store.commit('tenants/SET_PACKAGE', value)
      }
    }
  },
  methods: {
    ...mapActions('tenants', [
      'createTenant',
      'updateTenant'
    ])
  }
}
</script>
