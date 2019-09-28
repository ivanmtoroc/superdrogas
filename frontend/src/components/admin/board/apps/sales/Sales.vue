<template>
  <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Sales
        </h1>
      </div>
      <ol class="breadcrumb">
        <li>
          <router-link :to="{ name: 'home' }">Home</router-link>
        </li>
        <li class="active">
          Sales
        </li>
      </ol>
    </section>
    <section class="content">
      <div class="row">
        <div class="col-sm-6">
          <div class="box">
            <div class="box-body">
              <table
                id="table"
                class="table table-bordered table-striped"
              >
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Brand</th>
                    <th>Price</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(product, index) in products" :key="index">
                    <td>{{ product.name }}</td>
                    <td>{{ product.brand }}</td>
                    <td>{{ product.price }}</td>
                    <td class="text-center">
                      <a
                        @click="addToCart(product)"
                        class="btn.btn-app btn-primary btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#sale-form"
                      >
                        <i class="fa fa-plus-circle"></i>
                      </a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="col-sm-6">
          <div class="box">
            <div class="box-body">
              <table id="table-sale" class="table table-bordered table-striped">
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Unit price</th>
                    <th>Quantity</th>
                    <th>Total price</th>
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
                      <a
                        @click="deleteFromCart(product)"
                        class="btn.btn-app btn-danger btn-sm action-btn"
                      >
                        <i class="fa fa-minus-circle"></i>
                      </a>
                    </td>
                  </tr>
                  <div class="box-footer">
                    <a @click="checkout()" class="btn btn-raised btn-success action-btn">
                      <i class="fa fa-money"></i>
                      Checkout
                    </a>
                  </div>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import template from '@/utilities/template'

export default {
  name: 'sales',
  methods: {
    ...mapActions('products', [
      'getProducts',
      'getProduct'
    ]),
    ...mapActions('ecommerce', [
      'addToCart',
      'deleteFromCart',
      'checkout'
    ])
  },
  computed: {
    ...mapState('products', [
      'products'
    ]),
    ...mapGetters('ecommerce', [
      'cartProducts',
      'itemsOnCart'
    ])
  },
  created () {
    this.getProducts()
  },
  updated () {
    this.$nextTick(() => { template.reload() })
  }
}
</script>
