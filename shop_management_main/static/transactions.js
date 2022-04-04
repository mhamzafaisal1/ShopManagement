
document.addEventListener('DOMContentLoaded', () => {
    let date = document.getElementById('transactionPageHeaderDate');
    date.innerText = moment(date.innerText).format("dddd, MMMM Do YYYY")



    // toggler handler ;
    document.getElementById('makeNewTransactionButton').addEventListener('click', () => {
        let modal = document.querySelector('#newTransactionForm')
        modal.style.transform = 'translateX(0px)'
    })
    
    
    
    document.querySelector('#closeNewTransactionForm').addEventListener('click', () => {
        let modal = document.querySelector('#newTransactionForm')
        modal.style.transform = 'translateX(-2000px)'

    })
    
    
    document.querySelector('#newTransactionForm').addEventListener('submit', () => {
        let modal = document.querySelector('#newTransactionForm')
        modal.style.transform = 'translateX(-2000px)'
    })
})




