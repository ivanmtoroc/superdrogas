import http from '@/utilities/http'
import admin from '@/router/admin'
import tenant from '@/router/tenant'
import host from '@/utilities/host'
import template from '@/utilities/template'
import store from '@/store'

const router = host.isAdmin() ? admin : tenant

const state = {
  cartProducts: [],
  saleInvoice: {},
  productsInvoice: [],
  formData: new FormData()
}

const getters = {
  itemsOnCart: state => (state.cartProducts) ? state.cartProducts.length : 0,
  isCartEmpty: state => (state.cartProducts) ? state.cartProducts.length === 0 : false,
  total: (state) => {
    var total = 0
    for (let i = 0; i < state.cartProducts.length; i++) {
      total += state.cartProducts[i].quantity * state.cartProducts[i].price
    }
    return total
  }
}

const mutations = {
  ADD_TO_CART: (state, newProduct) => {
    let product = state.cartProducts.find(product => product.id === newProduct.id)
    if (!product) {
      state.cartProducts.push({ ...newProduct, quantity: 1 })
    } else {
      state.cartProducts = [
        ...state.cartProducts.filter(product => product.id !== newProduct.id),
        { ...product, quantity: product.quantity + 1 }
      ]
    }
  },
  DELETE_FROM_CART: (state, newProduct) => {
    newProduct.quantity--
    if (newProduct.quantity === 0) {
      state.cartProducts = [
        ...state.cartProducts.filter(product => product.id !== newProduct.id)
      ]
    } else {
      state.cartProducts = [
        ...state.cartProducts.filter(product => product.id !== newProduct.id),
        newProduct
      ]
    }
  },
  SET_SALE_INVOICE: (state, newSaleInvoice) => {
    state.saleInvoice = newSaleInvoice
  },
  ADD_PRODUCT_INVOICE: (state, newProductInvoice) => {
    state.productsInvoice.unshift(newProductInvoice)
  },
  BUILD_REQUEST (state, { getters, saleType }) {
    if (saleType === 'OS') {
      state.formData.append('user_id', '1010059777')
    }
    state.formData.append('client_id', store.getters['authentication/customerId'])
    state.formData.append('sale_type', saleType)
    state.formData.append('total_amount', getters.total)
    state.formData.append('is_active', true)
  },
  BUILD_REQUEST_PRODUCTS (state, { i, saleId }) {
    state.formData.append('sale_invoice_id', saleId)
    state.formData.append('product_id', state.cartProducts[i].id)
    state.formData.append('quantity', state.cartProducts[i].quantity)
    state.formData.append('unit_price', state.cartProducts[i].price)
    state.formData.append('is_active', true)
  }
}

const actions = {
  addToCart: ({ commit }, product) => {
    commit('ADD_TO_CART', product)
  },
  deleteFromCart: ({ commit }, product) => {
    template.destroy()
    commit('DELETE_FROM_CART', product)
  },
  checkout: async ({ state, commit, getters }, { event, saleType }) => {
    if (event) event.preventDefault()
    commit('BUILD_REQUEST', { getters, saleType })
    const response = await http.post('sales/sales_invoice/', state.formData)
    const saleId = response.data.id
    if (!response.error) {
      commit('SET_SALE_INVOICE', response.data)
      for (var i = 0; i < getters.itemsOnCart; i++) {
        commit('BUILD_REQUEST_PRODUCTS', { i, saleId })
        var responseProduct = await http.post('sales/product_on_sale/', state.formData)
        if (!responseProduct.error) {
          commit('ADD_PRODUCT_INVOICE', responseProduct.data)
        }
      }

      router.push({ name: 'checkout' })
    }
  },
  downloadXML: async ({ state }) => {
    const response = await http.get(`sales/xml?sale_id=${state.saleInvoice.id}`)
    var data = 'data:text/json;charset=utf-8,' + encodeURIComponent(response.data)
    var download = document.getElementById('download')
    download.setAttribute('href', data)
    download.setAttribute('download', `${host.getSubdomain()}.xml`)
    download.click()
  },
  downloadPDF: async ({ state }) => {
    const response = await http.get(`sales/pdf?sale_id=${state.saleInvoice.id}`)
    var blob = new Blob([response.data])
    var download = document.getElementById('download')
    download.href = window.URL.createObjectURL(blob)
    download.download = `${host.getSubdomain()}.pdf`
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
