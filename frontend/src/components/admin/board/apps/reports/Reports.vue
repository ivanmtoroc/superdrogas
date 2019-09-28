<template>
  <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Reports
        </h1>
      </div>
      <ol class="breadcrumb">
        <li>
          <router-link :to="{ name: 'home' }">Home</router-link>
        </li>
        <li class="active">
          Reports
        </li>
      </ol>
    </section>
    <section class="content">
      <div class="row">
        <div class="col-sm-12">
          <div class="box">
            <div class="box-body text-center">
              <button @click="downloadGeneralReport" class="btn btn-success">
                Download general report
              </button>
              <div>
                <img
                  :src="`https://chart.googleapis.com/chart?cht=p3&chs=800x300&chd=t:${report.cantidad}&chl=${report.nombres}&chtt=5%20Productos%20mas%20vendidos`"
                  alt="Report"
                  height="400"
                >
              </div>
              <span>
                <br><br><br><br>
              </span>
              <div>
                <img
                  :src="`https://chart.googleapis.com/chart?cht=lc&chs=800x300&chd=t:${sales.valores}&chl=1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31&chtt=Compras totales diarias`"
                  alt="Report"
                  height="400"
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <a id="download" style="display: none;"></a>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'reports',
  computed: {
    ...mapState('app', [
      'report',
      'sales'
    ])
  },
  methods: {
    ...mapActions('app', [
      'downloadGeneralReport',
      'getTopProducts'
    ])
  },
  mounted () {
    this.getTopProducts()
  }
}
</script>
