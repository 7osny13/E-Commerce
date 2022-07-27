import { createStore, combineReducers, applyMiddleware } from 'redux'
import thunk from 'redux-thunk'
import { composeWithDevTools } from 'redux-devtools-extension'
import {   productListReducer , productDetailsReducer} from './reducers/productReducers'
import { cartReducer } from './reducers/cartReducers'
import { WishlistReducer } from './reducers/WishlistReducers'

import {
    userLoginReducer,
    userRegisterReducer,
    userDetailsReducer,
    userUpdateProfileReducer,


} from './reducers/userReducers'

import {
  orderCreateReducer,
  orderDetailsReducer,
  orderPayReducer,
  orderListMyReducer,
 
} from './reducers/orderReducers'

const reducer = combineReducers({
    productList: productListReducer,
    productDetails: productDetailsReducer,
    cart: cartReducer,
    Wishlist:WishlistReducer,

    orderCreate: orderCreateReducer,
    orderDetails: orderDetailsReducer,
    orderPay: orderPayReducer,
    orderListMy: orderListMyReducer,
    
    userLogin: userLoginReducer,
    userRegister: userRegisterReducer,
    userDetails: userDetailsReducer,
    userUpdateProfile: userUpdateProfileReducer,
    
})

const cartItemsFromStorage = localStorage.getItem('cartItems') ?
    JSON.parse(localStorage.getItem('cartItems')) : []

const WishlistItemsFromStorage = localStorage.getItem('WishlistItems') ?
JSON.parse(localStorage.getItem('WishlistItems')) : []



const userInfoFromStorage = localStorage.getItem('userInfo') ?
    JSON.parse(localStorage.getItem('userInfo')) : null

const shippingAddressFromStorage = localStorage.getItem('shippingAddress') ?
JSON.parse(localStorage.getItem('shippingAddress')) : {}

const initialState = {
  cart: { 
    cartItems: cartItemsFromStorage,
    shippingAddress: shippingAddressFromStorage,  },
  Wishlist: {
    WishlistItems: WishlistItemsFromStorage,
}, 
  userLogin: { userInfo: userInfoFromStorage },
}

const middleware = [thunk]

const store = createStore(reducer, initialState,
    composeWithDevTools(applyMiddleware(...middleware)))

export default store
