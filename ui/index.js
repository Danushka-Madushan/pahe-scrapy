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

const zeroPad = (num, places) => String(num).padStart(places, '0')

const genEpisode = (data, session) => {
    const div = document.createElement('div')
    div.className = 'episode'
    div.innerHTML = `
    <div class="imgsection">
        <img src="${data.snapshot}" alt="" class="epimg">
    </div>
        <div class="content">
            <div class="ep-info">
                <button class="epid">${zeroPad(data.episode, 2)}</button>
                <button class="duration">${data.duration}</button>
                <button class="bd">${data.disc.length == 0 ? 'OG' : data.disc}</button>
                <button class="audio">${String(data.audio).toUpperCase()}</button>
                <button data-id="${data.session}" data-ssid="${session}" class="epdown" id="epdown">Download</button>
            </div>
        <div class="ep-links"></div>
    </div>
    `
    return div
}

const getAnimeList = async () => {
    $(namebox).blur();
    document.getElementById('result').innerHTML = ''
    const response = await axios.get(`/api/search/${namebox.value}`)
    for (let each of response.data.content.data) {
        const item = genArticle(each)
        document.getElementById('result').appendChild(item)
    }
}

$(namebox).on('keyup', async function (e) {
    if (e.key === 'Enter' || e.keyCode === 13) {
        await getAnimeList()
    }
});

search.onclick = async () => {
    await getAnimeList()
}

$(document.getElementById('result')).on('click', '.article .img .download', async function () {
    const response = await axios.get(`/api/session/${this.id}`)
    if (response.data.status == 200) {
        document.getElementById('result').innerHTML = ''
        for (let each of response.data.content.data) {
            const item = genEpisode(each, this.id)
            document.getElementById('result').appendChild(item)
        }
    }
})

$(document.getElementById('result')).on('click', '.episode .content .ep-info .epdown', async function () {
    const session = this.dataset.ssid
    const playid = this.dataset.id
    const response = await axios.get(`/api/links/${session}/${playid}`)
    if (response.data.status == 200) {
        this.innerText = 'Sucess'  
        this.parentNode.parentNode.children[1].innerHTML = `
        <button data-link="${response.data.content.link}" class="epdownplus" id="windown">${response.data.content.info}</button>
        `
    }
})

$(document.getElementById('result')).on('click', '.episode .ep-links .epdownplus', async function () {
    window.open(this.dataset.link)
})
