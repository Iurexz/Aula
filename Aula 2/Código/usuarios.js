document.addEventListener("DOMContentLoaded", carregarUsuarios)

function carregarUsuarios() {
    fetch('http://localhost:8080/usuario')
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao carregar os usuários');
        }
        return response.json();
    })
    .then(usuarios => { 
        const lista = document.getElementById('listaUsuarios')
        lista.innerHTML = ''; // Limpa a lista antes de adicionar novos itens

        if (usuarios.length === 0) {
            lista.innerHTML = '<li>Nenhum usuário encontrado</li>';
            return;
        }

        usuarios.forEach(usuario => {
            const item = document.createElement('li')
            item.innerHTML = ` <strong>Nome:</strong> ${usuario.nome}<br>
            <strong>E-mail:</strong> ${usuario.email}`
            lista.appendChild(item)
        })
    })
    .catch( erro => {
        document.getElementById('listaUsuarios').innerHTML = `<li>${erro.message}</li>`;


    })

    
}