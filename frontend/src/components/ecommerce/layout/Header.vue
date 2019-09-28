<template>
  <header class="main-header">
    <nav class="navbar navbar-static-top">
      <div class="container-fluid">
        <div class="navbar-header">
          <router-link :to="{ name: 'landing' }" class="navbar-brand">
            <strong class="title">
              {{ tenant.name }}
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
        <div
          class="collapse navbar-collapse pull-left"
          id="navbar-collapse"
        >
          <ul class="nav navbar-nav nav-item">
            <li v-for="(category, index) in firstSixCategories" :key="index">
              <a>
                {{ category.name }}
              </a>
            </li>
          </ul>
        </div>
        <div class="navbar-custom-menu">
          <a v-if="customerLogged">
            <ul class="nav navbar-nav nav-item">
              <li>
                <button class="btn username">
                  {{ customer.first_name }} {{ customer.last_name }}
                </button>
              </li>
            </ul>
          </a>
          <router-link :to="{ name: 'shopping-cart' }">
            <ul class="nav navbar-nav nav-item">
              <li>
                <button class="btn btn-success btn-raised">
                  <i class="fa fa-shopping-cart"></i>
                  <span v-if="itemsOnCart != 0" class="badge bg-teal">
                    {{ itemsOnCart }}
                  </span>
                </button>
              </li>
            </ul>
          </router-link>
          <router-link v-if="!customerLogged" :to="{ name: 'login-signup-ecommerce' }">
            <ul class="nav navbar-nav nav-item">
              <li>
                <button class="btn btn-success btn-raised">
                  Login / Signup
                </button>
              </li>
            </ul>
          </router-link>
          <a v-else @click="logout({ isStaff: false })">
            <ul class="nav navbar-nav nav-item">
              <li>
                <button class="btn btn-danger btn-raised">
                  Logout
                </button>
              </li>
            </ul>
          </a>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

export default {
  name: 'header-ecommerce',
  computed: {
    ...mapState('app', [
      'tenant'
    ]),
    ...mapState('authentication', [
      'customer'
    ]),
    ...mapGetters('categories', [
      'firstSixCategories'
    ]),
    ...mapGetters('ecommerce', [
      'itemsOnCart'
    ]),
    ...mapGetters('authentication', [
      'customerLogged'
    ])
  },
  methods: {
    ...mapActions('categories', [
      'getCategories'
    ]),
    ...mapActions('authentication', [
      'logout'
    ])
  },
  mounted () {
    this.getCategories()
  }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,600,700,800");
.username {
  color: white;
}
.title {
  font-size: 30px;
  color: white;
}
.nav {
  height: auto;
  margin-bottom: 2rem;
}
.nav-item img {
  max-height: 3.5rem;
}
.active-bottom-border {
  border-bottom: 3px solid #00d1b2;
  color: #00d1b2;
  padding-bottom: calc(0.75rem - 8px);
}
.nav-item {
  margin-bottom: 0px !important;
}
.navbar-custom-menu ul {
  margin: 0px 5px;
}
.planContainer {
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
.plan .titleContainer {
  background-color: #f3f3f3;
  padding: 1em;
}
.plan .titleContainer .title {
  font-size: 1.45em;
  text-transform: uppercase;
  color: #1abc9c;
  font-weight: 700;
}
.plan .infoContainer {
  padding: 1em;
  color: #2d3b48;
  box-sizing: border-box;
}
.plan .infoContainer .price {
  font-size: 1.35em;
  padding: 1em 0;
  font-weight: 600;
  margin-top: 0;
  display: inline-block;
  width: 80%;
}
.plan .infoContainer .price p {
  font-size: 1.35em;
  display: inline-block;
  margin: 0;
}
.plan .infoContainer .price span {
  font-size: 1.0125em;
  display: inline-block;
}
.plan .infoContainer .desc {
  padding-bottom: 1em;
  border-bottom: 2px solid #f3f3f3;
  margin: 0 auto;
  width: 90%;
}
.plan .infoContainer .desc em {
  font-size: 1em;
  font-weight: 500;
}
.plan .infoContainer .features {
  font-size: 1em;
  list-style: none;
  padding-left: 0;
}
.plan .infoContainer .features li {
  padding: 0.5em;
}
.plan .infoContainer .selectPlan {
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
.plan .infoContainer .selectPlan:hover {
  background-color: #1abc9c;
  color: white;
}
@media screen and (max-width: 25em) {
  .planContainer {
    margin: 0;
  }
  .planContainer .plan {
    width: 100%;
    margin: 1em 0;
  }
}
</style>
