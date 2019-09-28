<template>
  <body class="hold-transition layout-top-nav fixed">
    <div class="wrapper">
      <header class="main-header">
        <nav class="navbar navbar-static-top">
          <div class="container">
            <div class="navbar-header">
              <a class="navbar-brand">
                <strong class="title">Super Drogas</strong>
              </a>
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-collapse">
                <i class="fa fa-bars"></i>
              </button>
            </div>
            <div id="navbar-collapse" class="collapse navbar-collapse pull-left">
              <ul class="nav navbar-nav nav-item">
                <li><a href="#functionality">Functionality</a></li>
                <li><a href="#pricing">Pricing</a></li>
              </ul>
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
      <div class="content-wrapper" style="background-color: #ffffff !important;">
        <div class="container">
          <section class="content">
            <div class="row">
              <div class="col-md-6">
                <h1>
                  <b>
                    The management and administration tool for your drugstore
                    within the reach of your needs
                  </b>
                </h1>
                <p>
                  Super Drugs is a web application (software as a service), perfect for managing your
                  pharmacy that allows you to manage users, inventory, customers and much more.
                </p>
                <p>
                  All this following an economic subscription model with different packages that you
                  can choose at your convenience.
                </p>
              </div>
              <div class="col-md-6">
                <img src="@/static/images/landing-01.svg" alt="landing-01" style="width: 65%; margin-left: 50px;">
              </div>
            </div>
          </section>
          <section class="content pt-section" id="functionality">
            <div class="row">
              <h2 class="text-center">
                Super Drogas is designed for the cloud
              </h2>
              <div class="col-md-6">
                <img src="@/static/images/landing-02.png" alt="landing-02" width="80%">
              </div>
              <div class="col-md-6">
                <h1>
                  <b>
                    Better investment and better administration
                  </b>
                </h1>
                <p>
                  Super drugs allows you to manage your pharmacy staff, customer data,
                  inventory of your products and suppliers, on-site and online sales through
                  an ecommerce and many more at an economical subscription price and from the
                  comfort of the web.
                </p>
              </div>
            </div>
          </section>
          <section class="content pt-section" id="pricing">
            <h2 class="text-center">Pricing</h2>
            <div class="plan-container">
              <div class="plan">
                <div class="title-container">
                  <div class="title">Starter</div>
                </div>
                <div class="info-container">
                  <div class="price">
                    <p>$10</p><span>/mo</span>
                  </div>
                  <div class="p desc">
                    <em>Great for small pharmacies.</em>
                  </div>
                  <ul class="features">
                    <li>Users</li>
                    <li>Inventory</li>
                    <li>On-site sales</li>
                    <li>Reports (text only)</li>
                    <li>Security and access</li>
                  </ul>
                  <router-link :to="{ name: 'tenant-form' }">
                    <button class="btn btn-raised btn-success">
                      Select package
                    </button>
                  </router-link>
                </div>
              </div>
              <div class="plan">
                <div class="title-container">
                  <div class="title">Standard</div>
                </div>
                <div class="info-container">
                  <div class="price">
                    <p>$20</p><span>/mo</span>
                  </div>
                  <div class="p desc">
                    <em>Recommended for pharmacies with large sales.</em>
                  </div>
                  <ul class="features">
                    <li><strong>Starter pack features</strong></li>
                    <li>Customers</li>
                    <li>Customization</li>
                    <li>Reports</li>
                  </ul>
                  <router-link :to="{ name: 'tenant-form' }">
                    <button class="btn btn-raised btn-success">
                      Select package
                    </button>
                  </router-link>
                </div>
              </div>
              <div class="plan">
                <div class="title-container">
                  <div class="title">Premium</div>
                </div>
                <div class="info-container">
                  <div class="price">
                    <p>$25</p><span>/mo</span>
                  </div>
                  <div class="p desc">
                    <em>Ideal package for medium and large pharmacies that want to increase their billing.</em>
                  </div>
                  <ul class="features">
                    <li><strong>Standard pack features</strong></li>
                    <li>Ecommerce</li>
                    <li>Online sales</li>
                  </ul>
                  <router-link :to="{ name: 'tenant-form' }">
                    <button class="btn btn-raised btn-success">
                      Select package
                    </button>
                  </router-link>
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
export default {
  name: 'landing'
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,600,700,800");
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
