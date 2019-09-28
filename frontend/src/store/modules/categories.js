import http from '@/utilities/http'
import template from '@/utilities/template'

const state = {
  categories: [],
  category: {},
  errors: {},
  isLoading: false
}

const getters = {
  isNewCategory: state => state.category.id === undefined,
  activeCategories: state => {
    var categories = []
    state.categories.forEach(category => {
      if (category.is_active) {
        categories.push({
          ...category,
          text: category.name
        })
      }
    })
    return categories
  },
  firstSixCategories: state => {
    return state.categories.slice(0, 6)
  }
}

const mutations = {
  SET_CATEGORIES: (state, newCategories) => {
    state.categories = newCategories
  },
  SET_CATEGORY: (state, newCategory) => {
    state.categories = [
      ...state.categories.filter(category => category.id !== newCategory.id),
      newCategory
    ]
  },
  SET_ERRORS: (state, newErrors) => {
    state.errors = newErrors || {}
  },
  ADD_CATEGORY: (state, newCategory) => {
    state.categories.unshift(newCategory)
  },
  GET_CATEGORY: (state, categoryId) => {
    state.category = state.categories.find(category => category.id === categoryId) || {}
  },
  SWITCH_CATEGORY_STATUS: state => {
    state.categories.forEach((category, index) => {
      if (category.id === state.category.id) {
        state.categories[index].is_active = !state.categories[index].is_active
      }
    })
  },
  SET_LOAD_STATUS: (state, newLoadStatus) => {
    state.isLoading = newLoadStatus
  },
  SET_NAME: (state, newName) => {
    state.category = { ...state.category, name: newName }
  },
  SET_DESCRIPTION: (state, newDescription) => {
    state.category = { ...state.category, description: newDescription }
  }
}

const actions = {
  getCategories: async ({ commit }) => {
    commit('SET_LOAD_STATUS', true)
    const response = await http.get('inventory/categories/')
    if (!response.error) {
      commit('SET_CATEGORIES', response.data)
    }
    commit('SET_LOAD_STATUS', false)
  },
  getCategory: ({ commit }, categoryId) => {
    commit('SET_ERRORS')
    commit('GET_CATEGORY', categoryId)
  },
  createCategory: async ({ state, commit }, event) => {
    if (event) event.preventDefault()
    commit('SET_ERRORS')
    const response = await http.post('inventory/categories/', state.category)
    if (!response.error) {
      template.destroy()
      commit('ADD_CATEGORY', response.data)
      template.hideModal('#category-form')
      commit('GET_CATEGORY')
    } else {
      commit('SET_ERRORS', response.data)
    }
  },
  updateCategory: async ({ state, commit }, event) => {
    if (event) event.preventDefault()
    commit('SET_ERRORS')
    const response = await http.patch(`inventory/categories/${state.category.id}/`, state.category)
    if (!response.error) {
      template.destroy()
      commit('SET_CATEGORY', response.data)
      template.hideModal('#category-form')
    } else {
      commit('SET_ERRORS', response.data)
    }
  },
  deleteCategory: async ({ state, commit }) => {
    const response = await http.delete(`inventory/categories/${state.category.id}/`)
    if (!response.error) {
      commit('SWITCH_CATEGORY_STATUS')
      template.hideModal('#category-status')
    }
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
