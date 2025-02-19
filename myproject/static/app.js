let getTds = document.querySelectorAll('p')

getTds.forEach(function (p) {
    let p = row.querySelectorAll('p')
    let key = 0
    p.forEach(function (p) {
        if (p.textContent == 'Отклонено') {
            key = 1
        }
        if (p.textContent == 'В разработке') {
            key = 2
        }
        if (p.textContent == 'Новое') {
            key = 3
        }
    })

})