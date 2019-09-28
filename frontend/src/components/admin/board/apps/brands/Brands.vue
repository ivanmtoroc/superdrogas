<template>
  <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Brands
          <a
            @click="getBrand()"
            class="btn btn-primary btn-raised"
            data-toggle="modal"
            data-target="#brand-form"
          >
            Create brand
          </a>
        </h1>
      </div>
      <ol class="breadcrumb">
        <li>
          <router-link :to="{ name: 'home' }">Home</router-link>
        </li>
        <li class="active">
          Brands
        </li>
      </ol>
    </section>
    <section class="content">
      <div class="row">
        <div class="col-sm-12">
          <div class="box">
            <div class="box-body">
              <div v-if="isLoading" class="text-center">
                <spinner-component />
              </div>
              <table
                v-else
                id="table"
                class="table table-bordered table-striped"
              >
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Phone</th>
                    <th>Status</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(brand, index) in brands" :key="index">
                    <td>{{ brand.name }} </td>
                    <td>{{ brand.email }}</td>
                    <td>{{ brand.phone }}</td>
                    <td class="text-center">
                      <p
                        :class="`${ brand.is_active ? 'bg-green' : 'bg-red' }`"
                        class="badge p-bg"
                      >
                        {{ brand.is_active ? 'Active' : 'Inactive' }}
                      </p>
                    </td>
                    <td class="text-center">
                      <a
                        @click="getBrand(brand.id)"
                        class="btn.btn-app btn-primary btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#brand-form"
                      >
                        <i class="fa fa-edit"></i>
                      </a>
                      <a
                        @click="getBrand(brand.id)"
                        class="btn.btn-app btn-info btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#brand-detail"
                      >
                        <i class="fa fa-info-circle"></i>
                      </a>
                      <a
                        @click="getBrand(brand.id)"
                        :class="`${ brand.is_active ? 'btn-danger' : 'btn-success' }`"
                        class="btn.btn-app btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#brand-status"
                      >
                        <i :class="`${ brand.is_active ? 'fa fa-times-circle' : 'fa fa-plus-circle' }`"></i>
                      </a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </section>
    <brand-detail />
    <brand-form />
    <brand-status />
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import template from '@/utilities/template'
import BrandDetail from './modals/BrandDetail'
import BrandForm from './modals/BrandForm'
import BrandStatus from './modals/BrandStatus'

export default {
  name: 'brands',
  components: {
    BrandDetail,
    BrandForm,
    BrandStatus
  },
  computed: {
    ...mapState('brands', [
      'brands',
      'isLoading'
    ])
  },
  methods: {
    ...mapActions('brands', [
      'getBrands',
      'getBrand'
    ])
  },
  updated () {
    this.$nextTick(() => { template.reload() })
  }
}
</script>
