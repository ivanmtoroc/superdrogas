import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store'
import admin from './modules/admin'
import ecommerce from './modules/ecommerce'
// import host from '@/utilities/host'
import Error404 from '@/components/errors/Error404'
import DoesNotExistTenant from '@/components/errors/DoesNotExistTenant'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { ...admin },
    { ...ecommerce },
    {
      path: '/does-not-exist',
      name: 'does-not-exist',
      component: DoesNotExistTenant
    },
    {
      path: '*',
      component: Error404
    }
  ]
})

router.beforeEach((to, from, next) => {
  const logged = store.getters['authentication/logged']
  const customerLogged = store.getters['authentication/customerLogged']
  switch (to.name) {
    case 'login':
      logged ? next({ name: 'home' }) : next()
      break
    case 'home':
    case 'users':
    case 'products':
    case 'batches':
    case 'brands':
    case 'categories':
      logged ? next() : next({ name: 'login' })
      break
    case 'checkout':
      customerLogged ? next() : next({ name: 'login-signup-ecommerce' })
      break
    case 'login-signup-ecommerce':
      customerLogged ? next({ name: 'landing' }) : next()
      break
    default:
      next()
  }
})

// router.afterEach((to, from) => {
//   const tenantExist = store.getters['app/tenantExist']
//   console.log(tenantExist)
//   if (!tenantExist && to.path !== '/does-not-exist' && !host.isAdmin()) {
//     router.push({ name: 'does-not-exist' })
//   }
// })

export default router
