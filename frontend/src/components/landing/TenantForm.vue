<template>

  <body class="hold-transition layout-top-nav fixed">
    <div class="wrapper">
      <header class="main-header">
        <nav class="navbar navbar-static-top">
          <div class="container">
            <div class="navbar-header">
              <router-link
                :to="{ name: 'landing' }"
                class="navbar-brand"
              >
                <strong class="title">
                  Super Drogas
                </strong>
              </router-link>
              <button
                type="button"
                class="navbar-toggle collapsed"
                data-toggle="collapse"
                data-target="#navbar-collapse"
              >
                <i class="fa fa-bars"></i>
              </button>
            </div>
            <div class="navbar-custom-menu">
              <router-link :to="{ name: 'home' }">
                <ul class="nav navbar-nav nav-item">
                  <li>
                    <button class="btn btn-success btn-raised">
                      Admin
                    </button>
                  </li>
                </ul>
              </router-link>
            </div>
          </div>
        </nav>
      </header>
      <div class="content-wrapper">
        <div class="container">
          <section class="content">
            <div class="row">
              <div class="col-sm-12">
                <div class="box">
                  <div class="box-body cart">
                    <div v-if="tenantCreated">
                      <h1>Tenant successfully created!</h1>
                    </div>
                    <div v-else>
                      <h1>Create your pharmacy</h1>
                      <form>
                        <div class="row">
                          <input-component
                            class="col-md-6"
                            id="schema_name"
                            v-model="schema_name"
                            placeholder="Schema name"
                            :label="false"
                            :inputErrors="errors.schema_name"
                          />
                          <input-component
                            class="col-md-6"
                            id="name"
                            v-model="name"
                            placeholder="Name"
                            :label="false"
                            :inputErrors="errors.name"
                          />
                          <input-component
                            class="col-md-6"
                            id="prefix"
                            v-model="prefix"
                            placeholder="Prefix"
                            :label="false"
                            :inputErrors="errors.prefix"
                          />
                          <input-component
                            class="col-md-6"
                            id="nit"
                            v-model="nit"
                            placeholder="NIT"
                            :label="false"
                            :inputErrors="errors.nit"
                          />
                          <input-component
                            class="col-md-6"
                            id="phone"
                            v-model="phone"
                            placeholder="Phone"
                            :label="false"
                            :inputErrors="errors.phone"
                          />
                          <input-component
                            class="col-md-6"
                            id="email"
                            v-model="email"
                            placeholder="Email"
                            :label="false"
                            :inputErrors="errors.email"
                          />
                          <input-component
                            class="col-md-6"
                            id="address"
                            v-model="address"
                            placeholder="Address"
                            :label="false"
                            :inputErrors="errors.address"
                          />
                          <input-component
                            class="col-md-6"
                            id="description"
                            v-model="description"
                            placeholder="Description"
                            :label="false"
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
                            <span
                              v-if="errors.package"
                              class="help-block error-block"
                            >
                              This field is required.
                            </span>
                          </div>
                        </div>
                        <div class="pull-right">
                          <button
                            @click="createTenant($event)"
                            type="submit"
                            class="btn btn-success"
                          >Create</button>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </div>
      <footer class="main-footer navbar-fixed-bottom">
        <div class="container">
          <strong>Copyright &copy; 2019 | <a>Super Drogas</a></strong>.
          All rights reserved.
          <div class="pull-right hidden-xs">
            Universidad del Valle
          </div>
        </div>
      </footer>
    </div>
  </body>
</template>

<script>
import { mapState, mapActions } from 'vuex'

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
      'errors',
      'tenantCreated'
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
      'createTenant'
    ])
  }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,600,700,800");
.cart {
  padding: 30px;
}
.pt-section {
  padding: 70px;
}
.title {
  color: white;
  font-size: 30px;
}
.nav-item {
  margin-bottom: 0px !important;
}
.plan-container {
  display: flex;
  flex-wrap: wrap;
  margin: 1em;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
}
.plan {
  background: white;
  width: 20em;
  box-sizing: border-box;
  text-align: center;
  margin: 1em;
  margin-bottom: 1em;
}
.plan .title-container {
  background-color: #f3f3f3;
  padding: 1em;
}
.plan .title-container .title {
  font-size: 1.45em;
  text-transform: uppercase;
  color: #1abc9c;
  font-weight: 700;
}
.plan .info-container {
  padding: 1em;
  color: #2d3b48;
  box-sizing: border-box;
}
.plan .info-container .price {
  font-size: 1.35em;
  padding: 1em 0;
  font-weight: 600;
  margin-top: 0;
  display: inline-block;
  width: 80%;
}
.plan .info-container .price p {
  font-size: 1.35em;
  display: inline-block;
  margin: 0;
}
.plan .info-container .price span {
  font-size: 1.0125em;
  display: inline-block;
}
.plan .info-container .desc {
  padding-bottom: 1em;
  border-bottom: 2px solid #f3f3f3;
  margin: 0 auto;
  width: 90%;
}
.plan .info-container .desc em {
  font-size: 1em;
  font-weight: 500;
}
.plan .info-container .features {
  font-size: 1em;
  list-style: none;
  padding-left: 0;
}
.plan .info-container .features li {
  padding: 0.5em;
}
.plan .info-container .selectPlan {
  border: 2px solid #1abc9c;
  padding: 0.75em 1em;
  border-radius: 2.5em;
  cursor: pointer;
  transition: all 0.25s;
  margin: 1em auto;
  box-sizing: border-box;
  max-width: 70%;
  display: block;
  font-weight: 700;
}
.plan .info-container .selectPlan:hover {
  background-color: #1abc9c;
  color: white;
}
@media screen and (max-width: 25em) {
  .plan-container {
    margin: 0;
  }
  .plan-container .plan {
    width: 100%;
    margin: 1em 0;
  }
}
</style>
