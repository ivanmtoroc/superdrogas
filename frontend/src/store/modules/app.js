import http from '@/utilities/http'
import host from '@/utilities/host'

const state = {
  isAdmin: host.isAdmin(),
  app: '',
  tenant: {},
  report: {},
  sales: {}
}

const getters = {
  module: state => {
    switch (state.app) {
      case 'users':
      case 'customers':
        return 'accounts'
      case 'batches':
      case 'brands':
      case 'categories':
      case 'products':
        return 'inventory'
      default:
        return ''
    }
  },
  tenantExist: state => state.tenant.is_active || false
}

const mutations = {
  SET_APP: (state, newApp) => {
    state.app = newApp
  },
  SET_TENANT: (state, newTenant) => {
    state.tenant = newTenant
  },
  SET_REPORT: (state, newReport) => {
    state.report = newReport
  },
  SET_SALES: (state, newReport) => {
    state.sales = newReport
  }
}

const actions = {
  getTopProducts: async ({ commit }) => {
    const response = await http.get(`sales/products_report?schema_name=${host.getSubdomain()}`)
    commit('SET_REPORT', response.data)

    const response2 = await http.get(`sales/get_sales_report?schema_name=${host.getSubdomain()}`)
    commit('SET_SALES', response2.data)
  },
  updateApp: ({ commit }, newApp) => {
    commit('SET_APP', newApp)
  },
  getTenantInformation: async ({ commit }) => {
    if (!host.isAdmin()) {
      const response = await http.get(`tenant-info/${host.getSubdomain()}/`)
      commit('SET_TENANT', response.data)
    }
  },
  downloadData: async (context) => {
    const response = await http.get(`accounts/tenant_backup?schema_name=${host.getSubdomain()}`)
    var data = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(response.data))
    var download = document.getElementById('download')
    download.setAttribute('href', data)
    download.setAttribute('download', `${host.getSubdomain()}.json`)
    download.click()
  },
  downloadGeneralReport: async ({ state }) => {
    const response = await http.get(`sales/general_pdf_report?schema_name=${host.getSubdomain()}`)
    var blob = new Blob([response.data])
    var download = document.getElementById('download')
    download.href = window.URL.createObjectURL(blob)
    download.download = `${host.getSubdomain()}-report.pdf`
    download.click()
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
