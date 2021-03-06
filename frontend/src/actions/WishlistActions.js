import axios from 'axios'
import {
    Wishlist_ADD_ITEM,
    Wishlist_REMOVE_ITEM,

} from '../constants/WishlistConstants'


export const addToWishlist = (id, qty) => async (dispatch, getState) => {
    const { data } = await axios.get(`/api/products/${id}`)

    dispatch({
        type: Wishlist_ADD_ITEM,
        payload: {
            product: data._id,
            name: data.name,
            image: data.image,
            price: data.price,
            qty
        }
    })
    localStorage.setItem('WishlistItems', JSON.stringify(getState().Wishlist.WishlistItems))
}



export const removeFromWishlist = (id) => (dispatch, getState) => {
    dispatch({
        type: Wishlist_REMOVE_ITEM,
        payload: id,
    })

    localStorage.setItem('WishlistItems', JSON.stringify(getState().Wishlist.WishlistItems))
}
