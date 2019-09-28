import ECommerce from '@/components/ecommerce/ECommerce'
import LandingPage from '@/components/ecommerce/views/LandingPage'
import LoginSignup from '@/components/ecommerce/views/LoginSignup'
import ShoppingCart from '@/components/ecommerce/views/ShoppingCart'
import Checkout from '@/components/ecommerce/views/Checkout'

export default {
  path: '',
  component: ECommerce,
  children: [
    {
      path: '',
      name: 'landing',
      component: LandingPage
    },
    {
      path: 'login-signup',
      name: 'login-signup-ecommerce',
      component: LoginSignup
    },
    {
      path: 'shopping-cart',
      name: 'shopping-cart',
      component: ShoppingCart
    },
    {
      path: 'checkout',
      name: 'checkout',
      component: Checkout
    }
  ]
}
