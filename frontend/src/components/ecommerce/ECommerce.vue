<template>
  <body class="hold-transition layout-top-nav fixed">
    <div class="wrapper bg-color">
      <header-component></header-component>
      <div class="container-fluid m">
        <router-view></router-view>
      </div>
      <footer-component></footer-component>
    </div>
  </body>
</template>

<script>
import HeaderComponent from '@/components/ecommerce/layout/Header'
import FooterComponent from '@/components/ecommerce/layout/Footer'

export default {
  name: 'ecommerce',
  components: {
    HeaderComponent,
    FooterComponent
  }
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,600,700,800");
.m {
  margin-top: 70px;
  margin-bottom: 70px;
}
.bg-color {
  background-color: #EEE;
}
.nav-item {
  margin-bottom: 0px !important;
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
