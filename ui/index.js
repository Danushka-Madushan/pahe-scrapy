const search = document.getElementById('search')
const namebox = document.getElementById('name')

const genArticle = (data) => {
    const div = document.createElement('div')
    div.className = 'article'
    div.innerHTML = `
    <div class="img">
        <img src="${data.poster}" class="poster" loading="lazy">
        <button class="download" id="${data.session}">Download</button>
    </div>
    <div class="info">
        <div class="section"></div>
            <button class="title">${data.title}</button>
        <div class="section">
            <button class="type">${data.type}</button>
            <button class="score">${data.score}</button>
            <button class="episodes">${data.episodes}</button>
        </div>
        <div class="section">
            <button class="status">${data.status}</button>
        </div>
        <div class="section">
            <button class="year">${data.year}</button> 
        </div>
    </div>
    `
    return div
}

search.onclick = async () => {
    document.getElementById('result').innerHTML = ''
    const response = await axios.get(`http://localhost:8000/api/search/${namebox.value}`)
    for (let each of response.data.content.data) {
        const item = genArticle(each)
        document.getElementById('result').appendChild(item)
    }
}

$(document.getElementById('result')).on('click', '.article .img .download', async function () { 
    const response = await axios.get(`http://localhost:8000/api/session/${this.id}`)
    console.log(response.data)
});
