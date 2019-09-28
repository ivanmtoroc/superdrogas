<template>
  <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Configurations
        </h1>
      </div>
      <ol class="breadcrumb">
        <li>
          <router-link :to="{ name: 'home' }">Home</router-link>
        </li>
        <li class="active">
          Configurations
        </li>
      </ol>
    </section>
    <section class="content">
      <div class="row">
        <div class="col-sm-12">
          <div class="box">
            <div class="box-body">
              <div class="text-center">
                <button @click="downloadData()" class="btn btn-primary">
                  Download data
                </button>
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
import { mapActions } from 'vuex'

export default {
  name: 'configurations',
  methods: {
    ...mapActions('app', [
      'downloadData'
    ])
  }
}
</script>
