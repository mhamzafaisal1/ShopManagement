
// adding transaction_days transaction click listener;
document.addEventListener('DOMContentLoaded', () => {
    let list = document.getElementsByClassName('transaction');
    for (item of list) {
        item.addEventListener('click', (e) => {
            console.log(e.target.id)
        })
    }
})