<template>
  <div>
    <carousel></carousel>
    <div class="row">
      <h2 class="text-center section-title">
        Top products
      </h2>
      <div v-for="(product, index) in mostSelledProducts" :key="index" class="col-sm-2">
        <product :product="product"></product>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import Carousel from '@/components/ecommerce/components/Carousel'
import Product from '@/components/ecommerce/components/Product'

export default {
  name: 'shopping',
  components: {
    Carousel,
    Product
  },
  computed: {
    ...mapGetters('products', [
      'mostSelledProducts'
    ])
  },
  methods: {
    ...mapActions('products', [
      'getProducts'
    ])
  },
  mounted () {
    this.getProducts()
  }
}
</script>

<style scoped>
.mtb {
  margin-top: 70px;
  margin-bottom: 70px;
}
.section-title {
  margin: 40px 0px;
  font-size: 40px;
}
</style>
