
// add new product model listener toggler
document.addEventListener('DOMContentLoaded', () => {

    document.getElementById('openNewProductForm').addEventListener('click', () => {
        let modal = document.querySelector('#newProductForm')
        modal.style.transform = 'translateX(0px)'
    })
    
    
    
    document.querySelector('#closeNewProductForm').addEventListener('click', () => {
        let modal = document.querySelector('#newProductForm')
        modal.style.transform = 'translateX(-2000px)'
        // let modal = document.querySelector('#newProductForm')
        // modal.style.transform = 'translateX(2000px)'
       
        // setTimeout(() => {
        //     modal.style.display = 'none'
        //     modal.style.transform = 'translateX(-2000px)'
        //     setTimeout(() => {
        //         modal.style.display = 'flex'
        //     }, 1100)
        // },1100)
    })
    
    
    document.querySelector('#newProductForm').addEventListener('submit', () => {
        let modal = document.querySelector('#newProductForm')
        modal.style.transform = 'translateX(-2000px)'
    })
    })