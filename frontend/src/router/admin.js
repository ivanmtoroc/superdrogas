import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store'
import admin from './modules/admin'
import landing from './modules/landing'
import Error404 from '@/components/errors/Error404'
import TenantForm from '@/components/landing/TenantForm'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { ...admin },
    { ...landing },
    {
      path: '/tenant-form',
      name: 'tenant-form',
      component: TenantForm
    },
    {
      path: '*',
      component: Error404
    }
  ]
})

router.beforeEach((to, from, next) => {
  const logged = store.getters['authentication/logged']
  switch (to.name) {
    case 'login':
      logged ? next({ name: 'home' }) : next()
      break
    case 'home':
    case 'users':
      logged ? next() : next({ name: 'login' })
      break
    case 'products':
    case 'batches':
    case 'brands':
    case 'categories':
      next({ name: 'home' })
      break
    default:
      next()
  }
})

export default router
