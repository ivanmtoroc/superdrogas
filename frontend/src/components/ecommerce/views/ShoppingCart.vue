<template>
  <div class="row">
    <div class="col-sm-12">
      <section class="content-header">
        <div class="list-inline">
          <h1>Shopping cart</h1>
        </div>
      </section>
      <section>
        <div class="row">
          <div class="col-sm-12">
            <div class="box">
              <div class="box-body">
                <div v-if="isCartEmpty" class="text-center">
                  <img class="cart-empty-img" src="@/static/images/shopping-cart.png" alt="Cart">
                  <p>Your shopping cart is empty!</p>
                </div>
                <div v-else>
                  <table id="table" class="table table-bordered table-striped">
                    <thead>
                      <tr>
                        <th>Name</th>
                        <th>Unit price</th>
                        <th>Quantity</th>
                        <th>Total price</th>
                        <th>Image</th>
                        <th>Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(product, index) in cartProducts" :key="index">
                        <td>{{ product.name }}</td>
                        <td>${{ product.price }}</td>
                        <td>{{ product.quantity }}</td>
                        <td>${{ product.quantity * product.price }}</td>
                        <td class="text-center">
                          <img class="product-img" :src="product.image" alt="Product">
                        </td>
                        <td class="text-center">
                          <a @click="deleteFromCart(product)" class="btn.btn-app btn-danger btn-sm action-btn">
                            <i class="fa fa-minus-square"></i>
                          </a>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <div class="pull-right">
                    <div class="total">
                      Total: <strong>${{ total }}</strong>
                    </div>
                    <router-link
                      v-if="!customerLogged"
                      :to="{ name: 'login-signup-ecommerce' }"
                      class="btn btn-raised btn-success action-btn margin-btn"
                    >
                      Login / Signup
                    </router-link>
                    <button v-else @click="checkout({ $event, saleType: 'OL' })" class="btn btn-raised btn-success action-btn margin-btn">
                      <i class="fa fa-money"></i>
                      Checkout
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'
import template from '@/utilities/template'

export default {
  name: 'shopping-cart',
  computed: {
    ...mapState('ecommerce', [
      'cartProducts'
    ]),
    ...mapGetters('ecommerce', [
      'isCartEmpty',
      'total'
    ]),
    ...mapGetters('authentication', [
      'customerLogged'
    ])
  },
  methods: {
    ...mapActions('ecommerce', [
      'deleteFromCart',
      'checkout'
    ])
  },
  mounted () {
    template.reload()
  },
  updated () {
    this.$nextTick(() => { template.reload() })
  }
}
</script>

<style scoped>
.total {
  font-size: 20px;
  display: inline;
}
.margin-btn {
  margin: 10px 5px 10px 20px;
}
.cart-empty-img {
  height: 250px;
}
.product-img {
  height: 80px;
}
</style>
