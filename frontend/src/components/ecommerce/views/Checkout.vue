<template>
  <div class="row">
    <div class="col-sm-12">
      <section class="content-header">
        <div class="list-inline">
          <h1>Checkout</h1>
        </div>
      </section>
      <section class="content">
        <div class="row">
          <div class="col-sm-12">
            <div class="box">
              <div class="box-body text-center">
                <p>
                  Thank you for choosing us. :)
                </p>
                <p>
                  Download:
                </p>
                <button @click="downloadXML" class="btn btn-success">
                  XML
                </button>
                <button @click="downloadPDF" class="btn btn-success">
                  PDF
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
      <a id="download" style="display: none;"></a>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'checkout',
  methods: {
    ...mapActions('ecommerce', [
      'downloadXML',
      'downloadPDF'
    ])
  }
}
</script>
