import http from '@/utilities/http'
import host from '@/utilities/host'
import admin from '@/router/admin'
import tenant from '@/router/tenant'

const USER = 'user'
const TOKEN = 'token'
const CUSTOMER = 'customer'
const CUSTOMER_TOKEN = 'customer_token'

const state = {
  user: localStorage.getItem(USER) ? JSON.parse(localStorage.getItem(USER)) : {},
  token: localStorage.getItem(TOKEN),
  customer: localStorage.getItem(CUSTOMER) ? JSON.parse(localStorage.getItem(CUSTOMER)) : {},
  customerToken: localStorage.getItem(CUSTOMER_TOKEN)
}

const getters = {
  logged: state => !!state.token,
  customerLogged: state => !!state.customerToken,
  customerId: state => state.customer.id
}

const mutations = {
  SET_USER: (state, newUser) => {
    let user = newUser || {}
    state.user = user
    localStorage.setItem(USER, JSON.stringify(user))
  },
  SET_TOKEN: (state, newToken) => {
    let token = newToken || null
    state.token = token
    localStorage.setItem(TOKEN, token)
  },
  SET_CUSTOMER: (state, newCustomer) => {
    let customer = newCustomer || {}
    state.customer = customer
    localStorage.setItem(CUSTOMER, JSON.stringify(customer))
  },
  SET_CUSTOMER_TOKEN: (state, newCustomerToken) => {
    let customerToken = newCustomerToken || null
    state.customerToken = customerToken
    localStorage.setItem(CUSTOMER_TOKEN, customerToken)
  }
}

const actions = {
  login: async ({ commit }, user) => {
    const response = await http.post('accounts/login/', user)
    if (!response.error) {
      if (user.is_staff) {
        commit('SET_USER', response.data.user)
        commit('SET_TOKEN', response.data.token)
        const router = host.isAdmin() ? admin : tenant
        router.push({ name: 'home' })
      } else {
        commit('SET_CUSTOMER', response.data.user)
        commit('SET_CUSTOMER_TOKEN', response.data.token)
        const router = host.isAdmin() ? admin : tenant
        router.push({ name: 'landing' })
      }
    } else {
      return response.data
    }

    return {}
  },
  logout: ({ commit }, { isStaff }) => {
    if (isStaff) {
      commit('SET_USER')
      commit('SET_TOKEN')
      localStorage.removeItem(USER)
      localStorage.removeItem(TOKEN)
      const router = host.isAdmin() ? admin : tenant
      router.push({ name: 'login' })
    } else {
      commit('SET_CUSTOMER')
      commit('SET_CUSTOMER_TOKEN')
      localStorage.removeItem(CUSTOMER)
      localStorage.removeItem(CUSTOMER_TOKEN)
      const router = host.isAdmin() ? admin : tenant
      router.push({ name: 'landing' })
    }
  },
  passwordRestEmail: async (_, email) => {
    await http.post('rest-auth/password/reset/', { email })
  },
  passwordRestNewPassword: async (_, form) => {
    const response = await http.post(`password-reset/confirm/${form.uid}/${form.token}/`, form)
    if (!response.error) {
      const router = host.isAdmin() ? admin : tenant
      router.push({ name: 'password-reset-done' })
    } else {
      return response.data
    }

    return {}
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
