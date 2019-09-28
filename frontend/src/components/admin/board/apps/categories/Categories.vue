<template>
  <div>
    <section class="content-header">
      <div class="list-inline">
        <h1>
          Categories
          <a
            @click="getCategory()"
            class="btn btn-primary btn-raised"
            data-toggle="modal"
            data-target="#category-form"
          >
            Create category
          </a>
        </h1>
      </div>
      <ol class="breadcrumb">
        <li>
          <router-link :to="{ name: 'home' }">Home</router-link>
        </li>
        <li class="active">
          Categories
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
                    <th>Description</th>
                    <th>Status</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(category, index) in categories" :key="index">
                    <td>{{ category.name }} </td>
                    <td>{{ category.description }}</td>
                    <td class="text-center">
                      <p
                        :class="`${ category.is_active ? 'bg-green' : 'bg-red' }`"
                        class="badge p-bg"
                      >
                        {{ category.is_active ? 'Active' : 'Inactive' }}
                      </p>
                    </td>
                    <td class="text-center">
                      <a
                        @click="getCategory(category.id)"
                        class="btn.btn-app btn-primary btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#category-form"
                      >
                        <i class="fa fa-edit"></i>
                      </a>
                      <a
                        @click="getCategory(category.id)"
                        class="btn.btn-app btn-info btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#category-detail"
                      >
                        <i class="fa fa-info-circle"></i>
                      </a>
                      <a
                        @click="getCategory(category.id)"
                        :class="`${ category.is_active ? 'btn-danger' : 'btn-success' }`"
                        class="btn.btn-app btn-sm action-btn"
                        data-toggle="modal"
                        data-target="#category-status"
                      >
                        <i :class="`${ category.is_active ? 'fa fa-times-circle' : 'fa fa-plus-circle' }`"></i>
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
    <category-detail />
    <category-form />
    <category-status />
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import template from '@/utilities/template'
import CategoryDetail from './modals/CategoryDetail'
import CategoryForm from './modals/CategoryForm'
import CategoryStatus from './modals/CategoryStatus'

export default {
  name: 'categories',
  components: {
    CategoryDetail,
    CategoryForm,
    CategoryStatus
  },
  computed: {
    ...mapState('categories', [
      'categories',
      'isLoading'
    ])
  },
  methods: {
    ...mapActions('categories', [
      'getCategories',
      'getCategory'
    ])
  },
  created () {
    this.getCategories()
  },
  updated () {
    this.$nextTick(() => { template.reload() })
  }
}
</script>
